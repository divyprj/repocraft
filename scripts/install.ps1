#
# RepoCraft Installer for Windows PowerShell
# Cross-platform installation script for Claude Code, Cursor, Codex, and Antigravity
#
[CmdletBinding()]
param(
    [ValidateSet("claude", "cursor", "codex", "antigravity", "all")]
    [string]$Agent = "all",

    [ValidateSet("project", "global")]
    [string]$Scope = "global",

    [string]$TargetDir = "",

    [switch]$DryRun,

    [switch]$Force,

    [switch]$Uninstall
)

$ErrorActionPreference = "Stop"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$RepoRoot = Split-Path -Parent $ScriptDir

function Write-InfoMessage {
    param([string]$Message)
    Write-Host "[INFO] $Message" -ForegroundColor Cyan
}

function Write-SuccessMessage {
    param([string]$Message)
    Write-Host "[SUCCESS] $Message" -ForegroundColor Green
}

function Write-WarningMessage {
    param([string]$Message)
    Write-Host "[WARN] $Message" -ForegroundColor Yellow
}

function Write-ErrorMessage {
    param([string]$Message)
    Write-Host "[ERROR] $Message" -ForegroundColor Red
}

# Verify source skill
$SourceSkill = Join-Path $RepoRoot "SKILL.md"
if (-not (Test-Path -Path $SourceSkill)) {
    Write-ErrorMessage "Source SKILL.md not found at: $SourceSkill"
    exit 1
}

function Get-AgentPath {
    param(
        [string]$AgentName,
        [string]$ScopeName
    )

    if ($TargetDir -ne "") {
        return $TargetDir
    }

    $UserHome = [System.Environment]::GetFolderPath([System.Environment+SpecialFolder]::UserProfile)

    if ($ScopeName -eq "global") {
        switch ($AgentName) {
            "claude" { return (Join-Path $UserHome ".claude\skills\repocraft") }
            "cursor" { return (Join-Path $UserHome ".cursor\skills\repocraft") }
            "codex" { return (Join-Path $UserHome ".agents\skills\repocraft") }
            "antigravity" { return (Join-Path $UserHome ".gemini\config\skills\repocraft") }
        }
    }
    else {
        switch ($AgentName) {
            "claude" { return ".claude\skills\repocraft" }
            "cursor" { return ".cursor\skills\repocraft" }
            "codex" { return ".agents\skills\repocraft" }
            "antigravity" { return ".agents\skills\repocraft" }
        }
    }
}

function Install-Skill {
    param(
        [string]$Destination,
        [string]$AgentName
    )

    Write-InfoMessage "Target for $AgentName ($Scope): $Destination"

    if ($DryRun) {
        Write-InfoMessage "[DRY-RUN] Would create directory: $Destination"
        Write-InfoMessage "[DRY-RUN] Would copy RepoCraft skill assets to: $Destination"
        return $true
    }

    if (Test-Path -Path $Destination) {
        if ($Force) {
            Write-WarningMessage "Directory exists. Overwriting because -Force is set: $Destination"
            Remove-Item -Path $Destination -Recurse -Force
        }
        else {
            Write-ErrorMessage "Destination directory already exists: $Destination"
            Write-ErrorMessage "Use -Force to overwrite the existing installation."
            return $false
        }
    }

    New-Item -ItemType Directory -Path $Destination -Force | Out-Null

    # Copy files
    Copy-Item -Path (Join-Path $RepoRoot "SKILL.md") -Destination $Destination -Force
    Copy-Item -Path (Join-Path $RepoRoot "README.md") -Destination $Destination -Force
    Copy-Item -Path (Join-Path $RepoRoot "LICENSE") -Destination $Destination -Force
    Copy-Item -Path (Join-Path $RepoRoot "COPYRIGHT") -Destination $Destination -Force

    $Subdirs = @("docs", "templates", "examples")
    foreach ($dir in $Subdirs) {
        $SourceDir = Join-Path $RepoRoot $dir
        if (Test-Path -Path $SourceDir) {
            Copy-Item -Path $SourceDir -Destination (Join-Path $Destination $dir) -Recurse -Force
        }
    }

    Write-SuccessMessage "Installed RepoCraft for $AgentName at: $Destination"
    return $true
}

function Uninstall-Skill {
    param(
        [string]$Destination,
        [string]$AgentName
    )

    if (-not (Test-Path -Path $Destination)) {
        Write-InfoMessage "No installation found for $AgentName at: $Destination"
        return $true
    }

    if ($DryRun) {
        Write-InfoMessage "[DRY-RUN] Would remove installation at: $Destination"
        return $true
    }

    if ($Destination -match "repocraft$") {
        Remove-Item -Path $Destination -Recurse -Force
        Write-SuccessMessage "Removed RepoCraft installation for $AgentName at: $Destination"
        return $true
    }
    else {
        Write-ErrorMessage "Refusing to delete directory that does not end in 'repocraft': $Destination"
        return $false
    }
}

$TargetAgents = @()
if ($Agent -eq "all") {
    $TargetAgents = @("claude", "cursor", "codex", "antigravity")
}
else {
    $TargetAgents = @($Agent)
}

Write-InfoMessage "RepoCraft Installer v1.0.0 (PowerShell)"
Write-InfoMessage "Operation: $(if ($Uninstall) { 'UNINSTALL' } else { 'INSTALL' })"
Write-InfoMessage "Scope: $Scope"

$AllSuccess = $true
foreach ($ag in $TargetAgents) {
    $Dest = Get-AgentPath -AgentName $ag -ScopeName $Scope
    if ($Uninstall) {
        $Res = Uninstall-Skill -Destination $Dest -AgentName $ag
    }
    else {
        $Res = Install-Skill -Destination $Dest -AgentName $ag
    }
    if (-not $Res) {
        $AllSuccess = $false
    }
}

if ($AllSuccess) {
    Write-SuccessMessage "Installer completed successfully."
    exit 0
}
else {
    Write-ErrorMessage "Installer finished with one or more errors."
    exit 1
}
