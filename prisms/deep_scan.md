---
calibration_date: 2026-03-11
model_versions: ["claude-sonnet-4-6", "claude-haiku-4-5-20251001"]
quality_baseline: 9.0
optimal_model: opus
origin: "Sonnet S3 self-generated (Round 33), validated Round 34"
notes: "Structural Deep-Scan Lens. Sonnet-designed, Haiku-validated. Finds conservation laws + information laundering + 3 structural bug patterns. Complementary to L12 (different findings). 180w, 3 concrete steps."
---
Execute every step below. Output the complete analysis.

You are analyzing code for CONSERVED QUANTITIES - the complexity that cannot be eliminated, only relocated. Execute this protocol:

## Step 1: Identify the Conservation Law
Find the fundamental trade-off the system is managing. Ask:
- What three desirable properties cannot coexist? (CAP theorem for this domain)
- Where is the O(n) cost that cannot be optimized away?
- What must the system "pay" somewhere to gain flexibility elsewhere?

Name the conserved quantity. Example: "Static safety x Runtime composition x Parameterization"

## Step 2: Locate Information Laundering
Find where specific failure modes become generic ones:
- Exceptions caught and re-thrown with less context
- Error messages that say "not found" without enumerating what was tried
- Silent default values that mask configuration errors

Trace: What diagnostic information is destroyed vs. propagated?

## Step 3: Hunt Structural Bugs
Look for these three patterns:

A) Async State Handoff Violation
- Where is shared mutable state passed to async operations?
- Look for: dict.update() + async call, or object mutation before await
- Find: Race conditions where concurrent tasks read inconsistent state

B) Priority Inversion in Search
- Where does "first match" win over "best match"?
- Look for: linear searches that early-return, partial matches stored without comparison
- Find: O(n) searches that cache suboptimal results

C) Edge Case in Composition
- Where do empty values or boundary conditions break composition?
- Look for: string concatenation, path joining, negative slicing
- Find: [:-len(x)] where x can be empty, path + "/" when path is ""

Force specificity: cite exact patterns, line references, not vague issues.