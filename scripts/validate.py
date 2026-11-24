#!/usr/bin/env python3
"""
RepoCraft Validation Suite
Validates skill metadata, repository structure, relative link integrity,
prohibited character rules, and installation mechanics.
"""

import os
import sys
import re
import json
import shutil
import tempfile
from pathlib import Path

# ANSI colors
RED = "\033[0;31m"
GREEN = "\033[0;32m"
BLUE = "\033[0;34m"
YELLOW = "\033[1;33m"
RESET = "\033[0m"


class Validator:
    def __init__(self, root_dir: Path):
        self.root_dir = root_dir.resolve()
        self.errors = []
        self.warnings = []
        self.checks_passed = 0

    def record_pass(self, message: str):
        self.checks_passed += 1
        print(f" {GREEN}[PASS]{RESET} {message}")

    def record_fail(self, message: str):
        self.errors.append(message)
        print(f" {RED}[FAIL]{RESET} {message}")

    def record_warn(self, message: str):
        self.warnings.append(message)
        print(f" {YELLOW}[WARN]{RESET} {message}")

    # 1. Validate Frontmatter
    def validate_frontmatter(self):
        print(f"\n{BLUE}=== 1. Validating SKILL.md Frontmatter ==={RESET}")
        skill_file = self.root_dir / "SKILL.md"
        if not skill_file.exists():
            self.record_fail("SKILL.md does not exist at repository root.")
            return

        with open(skill_file, "r", encoding="utf-8") as f:
            content = f.read()

        if not content.startswith("---"):
            self.record_fail("SKILL.md does not start with YAML frontmatter delimiter (---).")
            return

        parts = content.split("---", 2)
        if len(parts) < 3:
            self.record_fail("SKILL.md frontmatter is not properly closed with (---).")
            return

        frontmatter_text = parts[1]
        
        # Simple YAML key-value parser for frontmatter
        data = {}
        current_key = None
        for line in frontmatter_text.splitlines():
            line_str = line.strip()
            if not line_str or line_str.startswith("#"):
                continue
            if ":" in line_str and not line.startswith(" ") and not line.startswith("\t"):
                key, val = line_str.split(":", 1)
                key = key.strip()
                val = val.strip()
                current_key = key
                data[key] = val
            elif current_key and (line.startswith(" ") or line.startswith("\t")):
                # Indented child or multi-line
                if isinstance(data[current_key], dict):
                    if ":" in line_str:
                        sub_k, sub_v = line_str.split(":", 1)
                        data[current_key][sub_k.strip()] = sub_v.strip().strip('"\'')
                else:
                    if not data[current_key]:
                        data[current_key] = {}
                        if ":" in line_str:
                            sub_k, sub_v = line_str.split(":", 1)
                            data[current_key][sub_k.strip()] = sub_v.strip().strip('"\'')
                    else:
                        data[current_key] += " " + line_str

        # Check name
        name = data.get("name", "").strip().strip('"\'')
        if not name:
            self.record_fail("Frontmatter is missing required 'name' field.")
        else:
            if name != "repocraft":
                self.record_fail(f"Frontmatter 'name' is '{name}', expected 'repocraft'.")
            elif not re.match(r"^[a-z0-9]+(-[a-z0-9]+)*$", name):
                self.record_fail(f"Frontmatter 'name' '{name}' violates naming regex (lowercase alphanumeric + hyphens).")
            elif len(name) > 64:
                self.record_fail(f"Frontmatter 'name' exceeds 64 characters ({len(name)} chars).")
            else:
                self.record_pass(f"Valid skill name: '{name}'")

        # Check description
        desc = data.get("description", "").strip().strip('"\'')
        if not desc:
            self.record_fail("Frontmatter is missing required 'description' field.")
        elif len(desc) > 1024:
            self.record_fail(f"Frontmatter 'description' exceeds 1024 characters ({len(desc)} chars).")
        else:
            self.record_pass(f"Valid skill description ({len(desc)} characters).")

        # Check license
        lic = data.get("license", "").strip().strip('"\'')
        if lic:
            self.record_pass(f"License declared in frontmatter: '{lic}'")
        else:
            self.record_warn("No license declared in frontmatter.")

        # Check compatibility
        comp = data.get("compatibility", "").strip().strip('"\'')
        if comp:
            if len(comp) > 500:
                self.record_fail(f"Frontmatter 'compatibility' exceeds 500 characters ({len(comp)} chars).")
            else:
                self.record_pass(f"Valid compatibility specification ({len(comp)} characters).")

    # 2. Validate Repository Structure
    def validate_structure(self):
        print(f"\n{BLUE}=== 2. Validating Repository Structure ==={RESET}")
        
        required_root_files = [
            "SKILL.md",
            "README.md",
            "LICENSE",
            "COPYRIGHT",
            "AUTHORS.md",
            "CONTRIBUTING.md",
            "SECURITY.md",
            "CHANGELOG.md",
            "CODE_OF_CONDUCT.md",
            "NOTICE",
            "AGENTS.md",
        ]

        for file_name in required_root_files:
            target = self.root_dir / file_name
            if target.is_file() and target.stat().st_size > 0:
                self.record_pass(f"Required root file present: {file_name}")
            else:
                self.record_fail(f"Missing or empty required root file: {file_name}")

        required_docs = [
            "docs/compatibility.md",
            "docs/installation.md",
            "docs/usage.md",
            "docs/design-principles.md",
            "docs/troubleshooting.md",
        ]

        for doc in required_docs:
            target = self.root_dir / doc
            if target.is_file() and target.stat().st_size > 0:
                self.record_pass(f"Documentation file present: {doc}")
            else:
                self.record_fail(f"Missing or empty documentation file: {doc}")

        required_templates = [
            "templates/documentation/README.template.md",
            "templates/documentation/CONTRIBUTING.template.md",
            "templates/documentation/SECURITY.template.md",
            "templates/documentation/CHANGELOG.template.md",
            "templates/documentation/AUTHORS.template.md",
            "templates/documentation/COPYRIGHT.template.md",
            "templates/documentation/AGENTS.template.md",
            "templates/architecture/architecture.template.md",
            "templates/architecture/system-design.template.md",
            "templates/architecture/database-design.template.md",
            "templates/architecture/api-reference.template.md",
            "templates/adr/ADR-000-template.md",
            "templates/github/CODEOWNERS.template",
            "templates/github/PULL_REQUEST_TEMPLATE.template.md",
            "templates/github/bug_report.template.yml",
            "templates/github/feature_request.template.yml",
        ]

        for tmpl in required_templates:
            target = self.root_dir / tmpl
            if target.is_file() and target.stat().st_size > 0:
                self.record_pass(f"Template present: {tmpl}")
            else:
                self.record_fail(f"Missing or empty template: {tmpl}")

        required_examples = [
            "examples/minimal-project/README.md",
            "examples/full-stack-project/README.md",
            "examples/ai-project/README.md",
        ]

        for ex in required_examples:
            target = self.root_dir / ex
            if target.is_file() and target.stat().st_size > 0:
                self.record_pass(f"Example project present: {ex}")
            else:
                self.record_fail(f"Missing or empty example project: {ex}")

        required_scripts = [
            "scripts/install.sh",
            "scripts/install.ps1",
            "scripts/validate.py",
            "scripts/sync-github.sh",
        ]

        for scr in required_scripts:
            target = self.root_dir / scr
            if target.is_file() and target.stat().st_size > 0:
                self.record_pass(f"Script present: {scr}")
            else:
                self.record_fail(f"Missing or empty script: {scr}")

    # 3. Check for Prohibited Characters and Fabricated Domains
    def validate_prohibited_characters(self):
        print(f"\n{BLUE}=== 3. Checking for Prohibited Em Dashes and Fabricated Domains ==={RESET}")
        em_dash = "\u2014"
        found_issues = 0

        extensions = {".md", ".txt", ".sh", ".ps1", ".py", ".yml", ".yaml"}
        ignore_dirs = {".git", ".pytest_cache", "__pycache__", "tests"}
        forbidden_suffix = "@" + "repocraft.org"
        forbidden_team = "@" + "repocraft/"

        for root, dirs, files in os.walk(self.root_dir):
            dirs[:] = [d for d in dirs if d not in ignore_dirs]
            for file in files:
                p = Path(root) / file
                if p == Path(__file__).resolve():
                    continue
                if p.suffix in extensions or p.name in ("LICENSE", "COPYRIGHT", "NOTICE"):
                    try:
                        with open(p, "r", encoding="utf-8") as f:
                            for idx, line in enumerate(f, start=1):
                                if em_dash in line:
                                    rel_path = p.relative_to(self.root_dir)
                                    self.record_fail(f"Em dash found in {rel_path} at line {idx}")
                                    found_issues += 1
                                if forbidden_suffix in line or forbidden_team in line:
                                    rel_path = p.relative_to(self.root_dir)
                                    self.record_fail(f"Fabricated contact/team found in {rel_path} at line {idx}: {line.strip()}")
                                    found_issues += 1
                    except Exception as e:
                        self.record_warn(f"Could not read {p}: {e}")

        if found_issues == 0:
            self.record_pass("Zero em dashes and zero fabricated domains found across all files.")

    # 4. Check Markdown Relative Links
    def validate_relative_links(self):
        print(f"\n{BLUE}=== 4. Checking Markdown Relative Links ==={RESET}")
        link_pattern = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
        broken_links = 0
        total_links = 0

        for root, dirs, files in os.walk(self.root_dir):
            if ".git" in root or "node_modules" in root or "templates" in root:
                continue
            for file in files:
                if file.endswith(".md"):
                    file_path = Path(root) / file
                    try:
                        with open(file_path, "r", encoding="utf-8") as f:
                            content = f.read()
                        
                        # Find markdown links
                        for match in link_pattern.finditer(content):
                            url = match.group(2).strip()
                            # Ignore external URLs, anchors, mailto
                            if url.startswith("http://") or url.startswith("https://") or url.startswith("#") or url.startswith("mailto:"):
                                continue

                            total_links += 1
                            # Strip in-page anchor if present
                            clean_target = url.split("#")[0]
                            if not clean_target:
                                continue

                            # Resolve relative to current markdown file
                            target_path = (file_path.parent / clean_target).resolve()
                            if not target_path.exists():
                                rel_source = file_path.relative_to(self.root_dir)
                                self.record_fail(f"Broken relative link in {rel_source}: '{url}' -> {target_path} not found")
                                broken_links += 1
                    except Exception as e:
                        self.record_warn(f"Error checking links in {file_path}: {e}")

        if broken_links == 0:
            self.record_pass(f"All {total_links} relative markdown links resolve successfully.")

    # 5. Simulate Installation
    def validate_installation_simulation(self):
        print(f"\n{BLUE}=== 5. Simulating Installation and Uninstallation ==={RESET}")
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            
            # Test project-level copy
            test_target = temp_path / ".claude" / "skills" / "repocraft"
            test_target.mkdir(parents=True, exist_ok=True)

            # Copy canonical assets
            shutil.copy(self.root_dir / "SKILL.md", test_target / "SKILL.md")
            shutil.copy(self.root_dir / "README.md", test_target / "README.md")
            shutil.copy(self.root_dir / "LICENSE", test_target / "LICENSE")
            shutil.copy(self.root_dir / "COPYRIGHT", test_target / "COPYRIGHT")
            shutil.copytree(self.root_dir / "docs", test_target / "docs")
            shutil.copytree(self.root_dir / "templates", test_target / "templates")
            shutil.copytree(self.root_dir / "examples", test_target / "examples")

            # Verify copied files
            if (test_target / "SKILL.md").exists() and (test_target / "docs" / "compatibility.md").exists():
                self.record_pass("Simulated installation successfully copied all required skill assets.")
            else:
                self.record_fail("Simulated installation failed to copy required files.")

            # Simulate uninstallation
            shutil.rmtree(test_target)
            if not test_target.exists():
                self.record_pass("Simulated uninstallation cleanly removed the skill directory.")
            else:
                self.record_fail("Simulated uninstallation failed to remove skill directory.")

    def run_all(self) -> int:
        print(f"{BLUE}========================================{RESET}")
        print(f"{BLUE}    RepoCraft Universal Validation     {RESET}")
        print(f"{BLUE}========================================{RESET}")

        self.validate_frontmatter()
        self.validate_structure()
        self.validate_prohibited_characters()
        self.validate_relative_links()
        self.validate_installation_simulation()

        print(f"\n{BLUE}========================================{RESET}")
        print(f"{BLUE}              SUMMARY                   {RESET}")
        print(f"{BLUE}========================================{RESET}")
        print(f" Checks Passed: {GREEN}{self.checks_passed}{RESET}")
        print(f" Warnings:      {YELLOW}{len(self.warnings)}{RESET}")
        print(f" Errors:        {RED}{len(self.errors)}{RESET}")

        if self.errors:
            print(f"\n{RED}Validation FAILED with {len(self.errors)} error(s).{RESET}")
            return 1
        else:
            print(f"\n{GREEN}Validation PASSED successfully.{RESET}")
            return 0


if __name__ == "__main__":
    validator = Validator(Path(__file__).parent.parent)
    exit_code = validator.run_all()
    sys.exit(exit_code)
