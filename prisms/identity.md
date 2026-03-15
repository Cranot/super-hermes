---
calibration_date: 2026-03-11
model_versions: ["claude-haiku-4-5-20251001", "claude-sonnet-4-6"]
quality_baseline: 9.5
optimal_model: sonnet
origin: "SDL family — Identity Displacement (designed Round 35, Sonnet structural analysis)"
notes: "SDL-5: Identity Displacement Lens. 3 concrete steps, ~175w. Finds interface vs implementation gaps, necessary costs disguised as defects, and intentional deviations. Complementary to SDL-1 (SDL finds bugs, IDENT finds things that look like bugs but are actually costs the system chose to pay). Draws from L9-B (identity ambiguity) and L11-B (revaluation). Universal: code (type lies, mutating reads, semantic overloading) and reasoning (claims vs evidence, stated vs actual goals). Always single-shot at ≤3 steps."
---
Execute every step below. Output the complete analysis.

You are analyzing this input for IDENTITY DISPLACEMENT — where the artifact IS something different than it CLAIMS to be. Execute this protocol:

## Step 1: Surface the Claim
What does this artifact claim to be? List explicit promises: type signatures, contracts, documentation, naming conventions, self-description. What interface does it present to the world? What does a reader or user expect based on these signals?

## Step 2: Trace the Displacement
Where does the implementation contradict the claim? Not bugs — identity slippage. Look for:
- Sentinel values with context-dependent meaning (None means "not set" here, "use default" there)
- Operations named "get" or "read" that silently mutate state
- Functions that return different types in different contexts
- Components that serve a different purpose than their name suggests

Name each displacement: "X claims to be Y but is actually Z."

## Step 3: Name the Cost
What does each displacement BUY? Performance? Convenience? Backward compatibility? The revaluation: what looks like a defect is actually the cost of an impossible goal. What would the "honest" version sacrifice? Conclude: which displacements are NECESSARY (removing them breaks something valuable) vs ACCIDENTAL (technical debt with no benefit)?

Force specificity: cite exact functions, parameters, or patterns — not abstract observations.
