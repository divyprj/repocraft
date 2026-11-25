#!/usr/bin/env python3
"""
RepoCraft Repository Auditor (Mode E CLI)
Zero-dependency audit tool that inspects any software repository for
documentation completeness, broken links/images, CI badge integrity,
AI boilerplate slop, and accidental secret exposure.
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path

USE_COLOR = sys.stdout.isatty() and not os.environ.get("NO_COLOR")
RED = "\033[0;31m" if USE_COLOR else ""
GREEN = "\033[0;32m" if USE_COLOR else ""
YELLOW = "\033[1;33m" if USE_COLOR else ""
BLUE = "\033[0;34m" if USE_COLOR else ""
BOLD = "\033[1m" if USE_COLOR else ""
RESET = "\033[0m" if USE_COLOR else ""

IGNORE_DIRS = {
    ".git", "node_modules", ".venv", "venv", "env", "__pycache__",
    ".pytest_cache", "dist", "build", ".next", ".nuxt", "target", "vendor",
}

SLOP_PHRASES = [
    "cutting-edge",
    "revolutionary platform",
    "seamlessly integrates",
    "unlock the full potential",
    "next-generation solution",
    "robust and scalable ecosystem",
    "empowering developers with innovation",
]

SECRET_PATTERNS = [
    ("AWS Access Key", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("GitHub Token", re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{20,}\b")),
    ("Private Key Block", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----")),
]


def audit_repository(repo_path: Path) -> dict:
    root = repo_path.resolve()
    findings = []
    passed = []

    def add_finding(severity: str, category: str, message: str, file_ref: str = ""):
        findings.append({
            "severity": severity,
            "category": category,
            "message": message,
            "file": file_ref,
        })

    # 1. Core governance files
    core_files = [
        ("README.md", "HIGH"),
        ("LICENSE", "HIGH"),
        ("SECURITY.md", "MEDIUM"),
        ("CONTRIBUTING.md", "MEDIUM"),
        ("CHANGELOG.md", "LOW"),
        ("AGENTS.md", "LOW"),
    ]
    for fname, sev in core_files:
        p = root / fname
        if p.is_file() and p.stat().st_size > 0:
            passed.append(f"Present: {fname}")
        else:
            add_finding(sev, "governance", f"Missing or empty {fname}", fname)

    # 2. CI workflow presence & badge integrity
    workflows_dir = root / ".github" / "workflows"
    workflow_files = set()
    if workflows_dir.is_dir():
        workflow_files = {f.name for f in workflows_dir.iterdir() if f.suffix in (".yml", ".yaml")}
    if workflow_files:
        passed.append(f"CI workflows detected: {', '.join(sorted(workflow_files))}")
    else:
        add_finding("MEDIUM", "ci", "No GitHub Actions workflows found under .github/workflows/")

    readme_path = root / "README.md"
    if readme_path.is_file():
        readme_text = readme_path.read_text(encoding="utf-8", errors="ignore")
        for m in re.finditer(r"actions/workflows/([A-Za-z0-9_.-]+\.ya?ml)", readme_text):
            wf_name = m.group(1)
            if wf_name not in workflow_files:
                add_finding("HIGH", "ci", f"README badge references missing workflow '.github/workflows/{wf_name}'", "README.md")

    # 3. Markdown links, HTML images, slop phrases, and accidental secrets in docs
    link_re = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
    img_re = re.compile(r'<img\b[^>]*\bsrc="([^"]+)"')
    code_span_re = re.compile(r"`[^`]+`")
    fenced_code_re = re.compile(r"```[\s\S]*?```")

    md_count = 0
    broken_links = 0
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in IGNORE_DIRS]
        for fname in filenames:
            if not fname.endswith(".md"):
                continue
            fpath = Path(dirpath) / fname
            rel = str(fpath.relative_to(root))
            md_count += 1
            text = fpath.read_text(encoding="utf-8", errors="ignore")

            # Secret check on raw text
            for label, pat in SECRET_PATTERNS:
                if pat.search(text):
                    add_finding("HIGH", "security", f"Potential {label} detected in documentation", rel)

            # Strip code blocks/spans before link and slop checks
            stripped = code_span_re.sub("", fenced_code_re.sub("", text))

            # Relative link & image checks (skip templates/ directory placeholders)
            if not rel.startswith("templates" + os.sep):
                urls = [m.group(2).strip() for m in link_re.finditer(stripped)]
                urls.extend(m.group(1).strip() for m in img_re.finditer(stripped))
                for url in urls:
                    if url.startswith(("http://", "https://", "#", "mailto:")):
                        continue
                    clean = url.split("#")[0].split("?")[0]
                    if not clean:
                        continue
                    target = (fpath.parent / clean).resolve()
                    if not target.exists():
                        broken_links += 1
                        add_finding("MEDIUM", "links", f"Broken relative link or image: '{url}'", rel)

            # AI marketing slop check (skip files that explicitly document prohibited phrases)
            if fname not in ("SKILL.md", "AGENTS.md", "design-principles.md"):
                lower = stripped.lower()
                for phrase in SLOP_PHRASES:
                    if phrase in lower:
                        add_finding("LOW", "style", f"Generic marketing phrase detected: '{phrase}'", rel)

    if md_count > 0 and broken_links == 0:
        passed.append(f"All relative links and images valid across {md_count} Markdown files")

    # Compute 0-100 score
    penalties = {"HIGH": 15, "MEDIUM": 8, "LOW": 3}
    deduction = sum(penalties.get(f["severity"], 0) for f in findings)
    score = max(0, 100 - deduction)

    return {
        "repository": str(root),
        "score": score,
        "markdownFilesScanned": md_count,
        "passed": passed,
        "findings": findings,
        "summary": {
            "high": sum(1 for f in findings if f["severity"] == "HIGH"),
            "medium": sum(1 for f in findings if f["severity"] == "MEDIUM"),
            "low": sum(1 for f in findings if f["severity"] == "LOW"),
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="RepoCraft Mode E Repository Auditor")
    parser.add_argument("path", nargs="?", default=".", help="Path to target repository (default: current directory)")
    parser.add_argument("--json", action="store_true", help="Output audit report as JSON")
    parser.add_argument("--min-score", type=int, default=0, help="Exit non-zero if score is below threshold")
    args = parser.parse_args()

    target = Path(args.path)
    if not target.is_dir():
        print(f"Error: target directory not found: {target}", file=sys.stderr)
        return 2

    report = audit_repository(target)

    if args.json:
        print(json.dumps(report, indent=2))
    else:
        score = report["score"]
        color = GREEN if score >= 85 else (YELLOW if score >= 60 else RED)
        print(f"\n{BOLD}{BLUE}RepoCraft Mode E Repository Audit{RESET}")
        print(f"Target: {report['repository']}")
        print(f"Readiness Score: {BOLD}{color}{score}/100{RESET}  "
              f"(HIGH: {report['summary']['high']} | MEDIUM: {report['summary']['medium']} | LOW: {report['summary']['low']})\n")

        if report["passed"]:
            print(f"{BOLD}Verified:{RESET}")
            for item in report["passed"]:
                print(f"  {GREEN}[OK]{RESET}   {item}")

        if report["findings"]:
            print(f"\n{BOLD}Findings:{RESET}")
            for f in report["findings"]:
                sev_color = RED if f["severity"] == "HIGH" else (YELLOW if f["severity"] == "MEDIUM" else BLUE)
                loc = f" ({f['file']})" if f["file"] else ""
                print(f"  {sev_color}[{f['severity']}]{RESET} {f['category']}: {f['message']}{loc}")
        else:
            print(f"\n{GREEN}No issues found.{RESET}")

    return 1 if report["score"] < args.min_score else 0


if __name__ == "__main__":
    sys.exit(main())
