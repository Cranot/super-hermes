#!/bin/bash
# Super Hermes — Install Prism skills into Hermes Agent
set -e

# Check if Hermes Agent appears to be installed
if [ ! -d "${HOME}/.hermes" ] && ! command -v hermes &> /dev/null; then
    echo "Warning: Hermes Agent not detected (~/.hermes/ not found)."
    echo "Install Hermes first: https://github.com/NousResearch/hermes-agent"
    echo "Continuing anyway (skills will be ready when Hermes is installed)..."
    echo ""
fi

SKILL_DIR="${HOME}/.hermes/skills"
PRISM_DIR="${HOME}/.hermes/prisms"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "Installing Super Hermes skills..."

mkdir -p "$SKILL_DIR" "$PRISM_DIR"
cp -r "$SCRIPT_DIR/skills/prism-scan" "$SKILL_DIR/"
cp -r "$SCRIPT_DIR/skills/prism-full" "$SKILL_DIR/"
cp -r "$SCRIPT_DIR/skills/prism-3way" "$SKILL_DIR/"
cp -r "$SCRIPT_DIR/skills/prism-discover" "$SKILL_DIR/"
cp -r "$SCRIPT_DIR/skills/prism-reflect" "$SKILL_DIR/"
cp -r "$SCRIPT_DIR/prisms/"*.md "$PRISM_DIR/" 2>/dev/null || true

echo ""
echo "Done. 5 skills + 7 proven prisms installed."
echo ""
echo "  Skills installed to: $SKILL_DIR"
echo "  Prisms installed to: $PRISM_DIR"
echo ""
echo "Usage (inside Hermes Agent):"
echo "  /prism-scan       Single-pass analysis with auto-generated lens"
echo "  /prism-full       Multi-pass pipeline with adversarial self-correction"
echo "  /prism-3way       WHERE/WHEN/WHY — three orthogonal operations + synthesis"
echo "  /prism-discover   Map all possible analysis domains"
echo "  /prism-reflect    Self-aware analysis with constraint transparency report"
echo ""
echo "Proven prisms (use as system prompts with any tool):"
echo "  error_resilience.md  Corruption cascades + silent exits (10.0/10)"
echo "  l12.md               Conservation laws + meta-laws + bugs (9.8/10)"
echo "  optimize.md          Critical path + safe/unsafe fixes (9.5/10)"
echo "  identity.md          Claims vs reality (9.5/10)"
echo "  deep_scan.md         Information destruction + laundering (9.0/10)"
echo "  claim.md             Assumption inversion (9.0/10)"
echo "  simulation.md        Temporal prediction (9.0/10)"
