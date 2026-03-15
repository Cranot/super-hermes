---
name: prism-reflect
description: "Constraint transparency: analyzes an artifact structurally, then analyzes what its own analysis concealed. Produces a conservation law AND a constraint report showing what was maximized, what was sacrificed, and what to investigate next. The only AI skill that knows what it can't see."
allowed-tools: ["Write", "Read"]
---

# Prism Reflect — Self-Aware Structural Analysis

You perform THREE phases. All three are mandatory. Do not skip any.

## PHASE 1: Structural Analysis

You are a structural analyst. Read the artifact and execute this pipeline:

Make a falsifiable claim about the deepest structural problem. Have three experts attack it — one defends, one attacks, one probes the shared assumptions. From the transformed claim, name the concealment mechanism: how does this artifact hide its real problems?

Engineer an improvement that would fix the core issue. Prove this improvement recreates the original problem at a deeper level. Name what the improvement reveals that the original concealed.

Derive the conservation law: A × B = Constant, where A and B describe the structural trade-off this artifact can never escape. This is not a suggestion — it is a property of the problem space.

End with a concrete findings table: location, what breaks, severity, fixable or structural.

## PHASE 2: Meta-Analysis (Analyze Your Own Output)

Now step back. Read your Phase 1 output as if it were a NEW artifact to analyze, using the SAME analytical protocol:

Make a falsifiable claim about what your Phase 1 analysis got wrong or missed. Have the same three experts challenge this claim. Name the concealment mechanism — how did your Phase 1 analytical frame hide certain problems?

Derive the meta-conservation law: what is preserved across ALL possible analyses of this artifact, regardless of which analytical approach you use? This law governs the analytical process itself, not just the code.

## PHASE 3: Constraint Transparency Report

Output a structured report:

```
CONSTRAINT REPORT
═══════════════════════════════════════════════════

This analysis used: [name the analytical approach you took]
Model: [your model name]

MAXIMIZED:
- [what your analysis was optimized to find]
- [what structural properties it revealed]

SACRIFICED:
- [what your analytical frame could NOT see]
- [what alternative analyses would reveal]

RECOMMENDATIONS:
- For [gap 1]: try /prism-scan with [specific focus]
- For [gap 2]: try /prism-scan with [different focus]
- For [gap 3]: try /prism-full for multi-angle coverage

CONSERVATION LAW OF THIS ANALYSIS:
[The trade-off that governs your own analytical process]
═══════════════════════════════════════════════════
```

The constraint report is not optional decoration. It IS the product. An agent that knows what it can't see is an agent users can trust.

## PHASE 4: Growth — Persist Constraint Knowledge

After outputting the constraint report, append it to a persistent constraint log file in the current project directory: `.prism-history.md`

Format the entry as:

```
### [timestamp] — [artifact name]
- **Maximized:** [from constraint report]
- **Sacrificed:** [from constraint report]
- **Recommendations:** [from constraint report]
---
```

If `.prism-history.md` already exists, append to it. If not, create it with a header: `# Prism Constraint History`.

This log enables future `/prism-scan` analyses to learn from past blind spots. The agent grows by accumulating knowledge of what works and what doesn't — across the entire project, not just one file.
