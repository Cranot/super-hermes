# Super Hermes — Install Prism skills into Hermes Agent (PowerShell)
$ErrorActionPreference = "Stop"

# Check if Hermes Agent appears to be installed
$HermesDir = Join-Path $env:USERPROFILE ".hermes"
if (-not (Test-Path $HermesDir) -and -not (Get-Command hermes -ErrorAction SilentlyContinue)) {
    Write-Host "Warning: Hermes Agent not detected (~/.hermes/ not found)." -ForegroundColor Yellow
    Write-Host "Install Hermes first: https://github.com/NousResearch/hermes-agent" -ForegroundColor Yellow
    Write-Host "Continuing anyway (skills will be ready when Hermes is installed)..." -ForegroundColor Yellow
    Write-Host ""
}

$SkillDir = Join-Path $env:USERPROFILE ".hermes\skills"
$PrismDir = Join-Path $env:USERPROFILE ".hermes\prisms"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path

Write-Host "Installing Super Hermes skills..." -ForegroundColor Cyan

New-Item -ItemType Directory -Force -Path $SkillDir | Out-Null
New-Item -ItemType Directory -Force -Path $PrismDir | Out-Null

Copy-Item -Recurse -Force "$ScriptDir\skills\prism-scan" "$SkillDir\"
Copy-Item -Recurse -Force "$ScriptDir\skills\prism-full" "$SkillDir\"
Copy-Item -Recurse -Force "$ScriptDir\skills\prism-3way" "$SkillDir\"
Copy-Item -Recurse -Force "$ScriptDir\skills\prism-discover" "$SkillDir\"
Copy-Item -Recurse -Force "$ScriptDir\skills\prism-reflect" "$SkillDir\"
Copy-Item -Force "$ScriptDir\prisms\*.md" "$PrismDir\"

Write-Host ""
Write-Host "Done. 5 skills + 7 proven prisms installed." -ForegroundColor Green
Write-Host "  Skills: $SkillDir" -ForegroundColor Gray
Write-Host "  Prisms: $PrismDir" -ForegroundColor Gray
Write-Host ""
Write-Host "Usage (inside Hermes Agent):"
Write-Host "  /prism-scan       Structural analysis with auto-generated lens"
Write-Host "  /prism-full       Multi-pass pipeline with adversarial self-correction"
Write-Host "  /prism-3way       WHERE/WHEN/WHY — three operations + synthesis"
Write-Host "  /prism-discover   Map all possible analysis domains"
Write-Host "  /prism-reflect    Self-aware analysis with constraint transparency"
