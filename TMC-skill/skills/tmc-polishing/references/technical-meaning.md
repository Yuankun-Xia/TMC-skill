# Preserve technical meaning while polishing

## High-consequence distinctions

| Source expression | Editing decision |
|---|---|
| "converges faster" with only accuracy/round curves | Keep a round-based convergence statement; do not write wall-clock speedup |
| "energy efficient" with FLOPs alone | Describe lower computation cost or flag missing energy evidence |
| "privacy preserving" because data stay local | State data locality; retain stronger privacy claims only with a defined mechanism and support |
| "optimal" after alternating nonconvex updates | Use the guarantee actually proved: feasible, stationary, locally optimal, or heuristic |
| "heterogeneous" | Clarify data, device, model, network, availability, or temporal heterogeneity |
| "fair" | Preserve the stated metric; do not interchange participation equity with equal client accuracy |
| "real-world" on public datasets and one server | Distinguish real data from real-device deployment |
| "improves by x%" | Verify denominator and relative change versus percentage points |

If the source is technically wrong, do not silently change it into an unsupported new claim. Explain the problem and use a supported weaker formulation if possible.

## Illustrative edits, not empirical results

- Weak: "Our approach can effectively deal with the problem of device diversity."
  More specific, when supported by the surrounding method: "The scheduler assigns smaller submodels to clients with less available memory."
- Ambiguous: "This reduces the delay, which improves the performance."
  Clarify the antecedent and metric: "Grouping clients by training time reduces idle waiting before aggregation."
- Overclaimed: "FL guarantees user privacy because data are not uploaded."
  Bounded: "FL keeps raw training data on clients; model updates may still disclose sensitive information."
- Chinese: "收敛速度显著提升" with no statistical test and only round curves.
  Write "reaches the target accuracy in fewer communication rounds" if the curves support that statement. Avoid statistical significance or elapsed-time claims.

Do not copy an illustrative mechanism into a manuscript that does not implement it.

## Paragraph and section control

Give each paragraph a clear job: bottleneck, gap, mechanism, observation, interpretation, or limitation. Place the subject before long qualifications. Separate a dense design description into operations that follow the execution timeline.

In Results, identify condition and comparison before interpreting the mechanism. Use tentative causal language for an explanation that has not been isolated by an ablation or analysis. A separate Discussion section is optional; interpretation can follow a result when the structure is clear.

Avoid arbitrary universal rules such as exactly three contributions, no sentences over 30 words, a fixed tense for all results, or a prescribed figure count. Sentence length and tense should serve clarity and the author's reporting context.

## LaTeX and quantitative checks

Keep mathematical operators, subscripts, random variables, and vector/scalar distinctions intact. Do not translate a variable name or citation key. Check agreement between prose inequalities and the equation. Preserve whether a bound holds in expectation or with high probability.

Keep `s`, `ms`, `J`, `W`, `MB`, `MiB`, `Mbps`, rounds, epochs and samples distinct. Do not convert between bytes and bits or power and energy without the necessary information. Retain baseline direction for lower-is-better metrics. Do not increase decimal precision beyond the evidence.

When shortening, remove repetition before deleting conditions, exceptions, or comparator details. Do not turn "under bounded staleness" into an unrestricted convergence guarantee.
