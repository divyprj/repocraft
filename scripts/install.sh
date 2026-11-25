#!/usr/bin/env bash
#
# RepoCraft Installer
# Cross-platform installation script for Claude Code, Cursor, Codex, Antigravity, and OpenCode
#
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

# Defaults
AGENT="all"
SCOPE="global"
TARGET_DIR=""
DRY_RUN=false
FORCE=false
SYMLINK=false
UNINSTALL=false

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

print_info() {
    printf "${BLUE}[INFO]${NC} %s\n" "$1"
}

print_success() {
    printf "${GREEN}[SUCCESS]${NC} %s\n" "$1"
}

print_warning() {
    printf "${YELLOW}[WARN]${NC} %s\n" "$1"
}

print_error() {
    printf "${RED}[ERROR]${NC} %s\n" "$1" >&2
}

usage() {
    cat << 'EOF'
RepoCraft Installer
Usage: ./scripts/install.sh [OPTIONS]

Options:
  --agent AGENT       Target agent: claude, cursor, codex, antigravity, opencode, or all (default: all)
  --scope SCOPE       Installation scope: project or global (default: global)
  --target-dir PATH   Custom destination directory (overrides default agent paths)
  --symlink           Symlink to this clone instead of copying (auto-updates on git pull)
  --dry-run           Preview actions without writing or deleting any files
  --force             Overwrite existing destination directories or symlinks if present
  --uninstall         Remove RepoCraft from the target agent directories
  --help              Display this help message

Examples:
  ./scripts/install.sh --agent claude --scope global
  ./scripts/install.sh --agent all --scope project
  ./scripts/install.sh --agent all --scope global --symlink
  ./scripts/install.sh --agent cursor --dry-run
  ./scripts/install.sh --agent all --uninstall
EOF
    exit 0
}

require_value() {
    if [[ $# -lt 2 || -z "${2:-}" ]]; then
        print_error "Option '$1' requires a value."
        exit 1
    fi
}

# Parse CLI arguments
while [[ $# -gt 0 ]]; do
    case "$1" in
        --agent)
            require_value "$1" "${2:-}"
            AGENT="$2"
            shift 2
            ;;
        --scope)
            require_value "$1" "${2:-}"
            SCOPE="$2"
            shift 2
            ;;
        --target-dir)
            require_value "$1" "${2:-}"
            TARGET_DIR="$2"
            shift 2
            ;;
        --symlink)
            SYMLINK=true
            shift
            ;;
        --dry-run)
            DRY_RUN=true
            shift
            ;;
        --force)
            FORCE=true
            shift
            ;;
        --uninstall)
            UNINSTALL=true
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

# Validate agent and scope options
case "$AGENT" in
    claude|cursor|codex|antigravity|opencode|all) ;;
    *)
        print_error "Invalid agent '$AGENT'. Must be one of: claude, cursor, codex, antigravity, opencode, all."
        exit 1
        ;;
esac

case "$SCOPE" in
    project|global) ;;
    *)
        print_error "Invalid scope '$SCOPE'. Must be one of: project, global."
        exit 1
        ;;
esac

# Validate source skill
if [[ ! -f "${REPO_ROOT}/SKILL.md" ]]; then
    print_error "Source SKILL.md not found at ${REPO_ROOT}/SKILL.md"
    exit 1
fi

get_agent_paths() {
    local agent="$1"
    local scope="$2"

    if [[ -n "$TARGET_DIR" ]]; then
        echo "$TARGET_DIR"
        return
    fi

    if [[ "$scope" == "global" ]]; then
        local user_home="${HOME:-${USERPROFILE:-}}"
        case "$agent" in
            claude)
                echo "${user_home}/.claude/skills/repocraft"
                ;;
            cursor)
                echo "${user_home}/.cursor/skills/repocraft"
                ;;
            codex)
                echo "${user_home}/.agents/skills/repocraft"
                ;;
            antigravity)
                echo "${user_home}/.gemini/config/skills/repocraft"
                ;;
            opencode)
                echo "${user_home}/.config/opencode/skills/repocraft"
                ;;
        esac
    else
        case "$agent" in
            claude)
                echo ".claude/skills/repocraft"
                ;;
            cursor)
                echo ".cursor/skills/repocraft"
                ;;
            codex)
                echo ".agents/skills/repocraft"
                ;;
            antigravity)
                echo ".agents/skills/repocraft"
                ;;
            opencode)
                echo ".opencode/skills/repocraft"
                ;;
        esac
    fi
}

install_to_path() {
    local target="$1"
    local agent="$2"

    print_info "Target for $agent ($SCOPE): $target"

    if [[ "$DRY_RUN" == true ]]; then
        if [[ "$SYMLINK" == true ]]; then
            print_info "[DRY-RUN] Would create symlink: $target -> ${REPO_ROOT}"
        else
            print_info "[DRY-RUN] Would create directory: $target"
            print_info "[DRY-RUN] Would copy RepoCraft skill assets to: $target"
        fi
        return 0
    fi

    if [[ -e "$target" || -L "$target" ]]; then
        if [[ "$FORCE" == true ]]; then
            print_warning "Destination exists. Overwriting because --force is enabled: $target"
            rm -rf "$target"
        else
            print_error "Destination already exists: $target"
            print_error "Use --force to overwrite the existing installation."
            return 1
        fi
    fi

    if [[ "$SYMLINK" == true ]]; then
        mkdir -p "$(dirname "$target")"
        ln -s "${REPO_ROOT}" "$target"
        print_success "Symlinked RepoCraft for $agent at: $target -> ${REPO_ROOT}"
        return 0
    fi

    mkdir -p "$target"

    # Copy canonical skill and documentation
    cp "${REPO_ROOT}/SKILL.md" "${target}/"
    cp "${REPO_ROOT}/README.md" "${target}/"
    cp "${REPO_ROOT}/LICENSE" "${target}/"
    cp "${REPO_ROOT}/COPYRIGHT" "${target}/"

    # Copy docs, templates, and examples if they exist
    if [[ -d "${REPO_ROOT}/docs" ]]; then
        cp -r "${REPO_ROOT}/docs" "${target}/"
    fi
    if [[ -d "${REPO_ROOT}/templates" ]]; then
        cp -r "${REPO_ROOT}/templates" "${target}/"
    fi
    if [[ -d "${REPO_ROOT}/examples" ]]; then
        cp -r "${REPO_ROOT}/examples" "${target}/"
    fi

    print_success "Installed RepoCraft for $agent at: $target"
}

uninstall_from_path() {
    local target="$1"
    local agent="$2"

    if [[ ! -e "$target" && ! -L "$target" ]]; then
        print_info "No installation found for $agent at: $target"
        return 0
    fi

    if [[ "$DRY_RUN" == true ]]; then
        print_info "[DRY-RUN] Would remove installation at: $target"
        return 0
    fi

    # Safety check: ensure target ends with repocraft
    if [[ "$target" =~ repocraft$ ]]; then
        rm -rf "$target"
        print_success "Removed RepoCraft installation for $agent at: $target"
    else
        print_error "Refusing to delete directory that does not end in 'repocraft': $target"
        return 1
    fi
}

# Determine target agents list
TARGET_AGENTS=()
if [[ "$AGENT" == "all" ]]; then
    TARGET_AGENTS=("claude" "cursor" "codex" "antigravity" "opencode")
else
    TARGET_AGENTS=("$AGENT")
fi

print_info "RepoCraft Installer v1.1.0"
print_info "Operation: $(if [[ "$UNINSTALL" == true ]]; then echo "UNINSTALL"; else echo "INSTALL"; fi)"
print_info "Scope: $SCOPE"

# Deduplicate shared destination paths (e.g., codex + antigravity share .agents/skills/repocraft in project scope)
SEEN_PATHS=()
path_already_seen() {
    local candidate="$1"
    local seen
    for seen in "${SEEN_PATHS[@]:-}"; do
        if [[ "$seen" == "$candidate" ]]; then
            return 0
        fi
    done
    return 1
}

exit_code=0
for ag in "${TARGET_AGENTS[@]}"; do
    dest="$(get_agent_paths "$ag" "$SCOPE")"
    if path_already_seen "$dest"; then
        print_info "Skipping duplicate shared path for $ag: $dest (already handled)"
        continue
    fi
    SEEN_PATHS+=("$dest")
    if [[ "$UNINSTALL" == true ]]; then
        uninstall_from_path "$dest" "$ag" || exit_code=1
    else
        install_to_path "$dest" "$ag" || exit_code=1
    fi
done

if [[ $exit_code -eq 0 ]]; then
    print_success "Installer completed successfully."
else
    print_error "Installer finished with one or more errors."
fi

exit $exit_code
