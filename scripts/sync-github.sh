#!/usr/bin/env bash
#
# RepoCraft GitHub Metadata Synchronizer
# Uses GitHub CLI (gh) to populate repository description, topics, and releases.
#
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

# Formatting (respects NO_COLOR and non-TTY output)
if [[ -t 1 && -z "${NO_COLOR:-}" ]]; then
    RED='\033[0;31m'
    GREEN='\033[0;32m'
    BLUE='\033[0;34m'
    YELLOW='\033[1;33m'
    NC='\033[0m'
else
    RED='' GREEN='' BLUE='' YELLOW='' NC=''
fi

print_info() { printf "${BLUE}[INFO]${NC} %s\n" "$1"; }
print_success() { printf "${GREEN}[SUCCESS]${NC} %s\n" "$1"; }
print_warning() { printf "${YELLOW}[WARN]${NC} %s\n" "$1"; }
print_error() { printf "${RED}[ERROR]${NC} %s\n" "$1" >&2; }

# Defaults for RepoCraft
DEFAULT_DESC="Universal AI coding agent skill for repository engineering, architecture diagrams, ADRs, governance, and factual documentation across Claude Code, Cursor, Codex, Antigravity, and OpenCode."
DEFAULT_TOPICS="agent-skills,ai-agents,devops,documentation,software-architecture,codex,claude-code,cursor,antigravity,opencode"

REPO=""
DESC="$DEFAULT_DESC"
TOPICS="$DEFAULT_TOPICS"
RELEASE_TAG=""
DRY_RUN=false

usage() {
    cat << 'EOF'
RepoCraft GitHub Metadata Synchronizer
Usage: ./scripts/sync-github.sh [OPTIONS]

Options:
  --repo REPO         Target repository (e.g. owner/repo). Defaults to git remote origin.
  --description DESC  Repository description (max 350 chars).
  --topics TOPICS     Comma-separated list of repository topics.
  --release TAG       Create a GitHub release for the specified git tag using CHANGELOG.md.
  --dry-run           Preview changes without executing gh commands.
  --help              Display this help message.

Examples:
  ./scripts/sync-github.sh
  ./scripts/sync-github.sh --release v1.1.0
  ./scripts/sync-github.sh --dry-run
EOF
    exit 0
}

while [[ $# -gt 0 ]]; do
    case "$1" in
        --repo)
            REPO="${2:-}"
            shift 2
            ;;
        --description)
            DESC="${2:-}"
            shift 2
            ;;
        --topics)
            TOPICS="${2:-}"
            shift 2
            ;;
        --release)
            RELEASE_TAG="${2:-}"
            shift 2
            ;;
        --dry-run)
            DRY_RUN=true
            shift
            ;;
        --help|-h)
            usage
            ;;
        *)
            print_error "Unknown option: $1"
            usage
            ;;
    esac
done

# Check if gh CLI is installed
if ! command -v gh >/dev/null 2>&1; then
    print_error "GitHub CLI (gh) is not installed."
    print_info "Install gh CLI: https://cli.github.com/ or use the GitHub Web UI."
    exit 1
fi

# Check if gh CLI is authenticated
if ! gh auth status >/dev/null 2>&1; then
    print_error "GitHub CLI (gh) is not authenticated."
    print_info "Run 'gh auth login' to authenticate your GitHub account."
    exit 1
fi

# Detect repository if not provided
if [[ -z "$REPO" ]]; then
    if git -C "$REPO_ROOT" remote get-url origin >/dev/null 2>&1; then
        REMOTE_URL="$(git -C "$REPO_ROOT" remote get-url origin)"
        REPO="$(echo "$REMOTE_URL" | sed -E 's/.*github\.com[:\/](.*)(\.git)?/\1/' | sed 's/\.git$//')"
    fi
fi

if [[ -z "$REPO" ]]; then
    print_error "Could not detect GitHub repository. Specify with --repo <owner/repo>."
    exit 1
fi

# Build portable repeated --add-topic flags for all gh CLI versions
TOPIC_ARGS=()
IFS=',' read -r -a TOPIC_LIST <<< "$TOPICS"
for raw_topic in "${TOPIC_LIST[@]}"; do
    topic="$(echo "$raw_topic" | xargs)"
    if [[ -n "$topic" ]]; then
        TOPIC_ARGS+=("--add-topic" "$topic")
    fi
done

print_info "Target repository: $REPO"
print_info "Description: $DESC"
print_info "Topics: $TOPICS"

if [[ "$DRY_RUN" == true ]]; then
    print_info "[DRY-RUN] Would run: gh repo edit $REPO --description \"$DESC\" ${TOPIC_ARGS[*]}"
    if [[ -n "$RELEASE_TAG" ]]; then
        print_info "[DRY-RUN] Would run: gh release create $RELEASE_TAG --title \"RepoCraft $RELEASE_TAG\" --notes-file \"${REPO_ROOT}/CHANGELOG.md\""
    fi
    print_success "Dry-run completed."
    exit 0
fi

# Update repository description and topics
print_info "Updating repository metadata..."
gh repo edit "$REPO" --description "$DESC" "${TOPIC_ARGS[@]}"
print_success "Repository description and topics updated successfully."

# Create release if requested
if [[ -n "$RELEASE_TAG" ]]; then
    CHANGELOG_FILE="${REPO_ROOT}/CHANGELOG.md"
    if [[ -f "$CHANGELOG_FILE" ]]; then
        print_info "Publishing release for tag $RELEASE_TAG from CHANGELOG.md..."
        gh release create "$RELEASE_TAG" \
            --title "RepoCraft ${RELEASE_TAG}: Universal Repository Engineering Skill" \
            --notes-file "$CHANGELOG_FILE" \
            --repo "$REPO"
        print_success "GitHub release $RELEASE_TAG published successfully."
    else
        print_warning "CHANGELOG.md not found. Creating release without notes file."
        gh release create "$RELEASE_TAG" \
            --title "RepoCraft ${RELEASE_TAG}: Universal Repository Engineering Skill" \
            --repo "$REPO"
        print_success "GitHub release $RELEASE_TAG published successfully."
    fi
fi

print_success "GitHub synchronization completed."
