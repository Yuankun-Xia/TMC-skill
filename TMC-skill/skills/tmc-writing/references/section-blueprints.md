# TMC section blueprints

These are adaptable writing moves, not mandated headings. Reorder Related Work or combine formulation with design when that makes the paper easier to judge.

## Choose a contribution architecture

| Contribution | Typical argument order | Decisive evidence |
|---|---|---|
| Mobile/edge system | Application and measured bottleneck; design goals; architecture; implementation; evaluation; limitations | End-to-end benefit, overhead breakdown, design ablations, representative workloads |
| Optimization and learning theory | System and timeline; objective and constraints; difficulty; solver or protocol; analysis; numerical evaluation | Valid assumptions, correct guarantee, feasible solutions, useful system trade-offs |
| Learning method for mobile workloads | Mobile data/system failure; mechanism; implementation; evaluation | Appropriate task metrics plus resource or operational implications of the method |
| Security or privacy | Assets and adversary; attack or risk; defense; analysis; evaluation | Attack effectiveness, benign utility, overhead, explicit security boundary |

The supplied corpus contains all of these patterns. FedPipe and SPFERE illustrate implementation-oriented narratives; Fed-RAA combines resource adaptation and convergence; PEFL illustrates threat-dependent evaluation. Use [corpus observations](tmc-corpus-observations.md) for local paper anchors.

## Title

Combine the actual capability or mechanism with the system/problem: `[Mechanism] for [task] under [constraint]`. Use an acronym only if it aids identification. Do not imply universality, optimality, privacy, or deployment that the results do not establish.

## Abstract

Move from `mobile bottleneck -> unresolved technical issue -> proposed mechanism -> analysis/implementation, if present -> decisive observed result -> bounded significance`.

- Make the distinction from prior work concrete: resource-aware submodel selection is more informative than "an efficient framework."
- Include quantitative results only when verified, preserving baseline, metric, denominator, and setting.
- A comparison needs a reference point; "reduces training time" should identify the comparison or budget if the evidence permits.
- Do not invent a percentage to make an abstract appear complete. Keep a results slot provisional when data are unavailable.
- Follow the user's supplied/current journal abstract constraints. Do not infer a universal word count from published papers.

## Introduction

Write backward from the contribution, then present a coherent forward argument:

1. Establish a concrete application and the mobile constraint that changes the problem.
2. Describe the relevant existing approach and its failure mechanism under that constraint.
3. Explain why that failure is technically difficult to address. A constraint list without coupling or conflict is insufficient.
4. State the design insight and connect each component to the problem it solves.
5. State contributions that can be checked later in the manuscript.

Use measured motivation when available: an idle-time trace, a resource profile, unstable participation, a topology change, or a reproducible privacy attack. Label untested motivation as a hypothesis rather than a result. Avoid generic 6G/AI growth paragraphs unless they explain the specific problem.

An empirical contribution can briefly state a verified result in the Introduction. Do not impose a ban on mentioning results, and do not turn the Introduction into a duplicate of the evaluation.

## Related Work

Group by mechanism or assumption that bears on the gap: synchronization and staleness, heterogeneity adaptation, compression/submodels, topology control, incentive design, or threat model as applicable. For each group, state what it does, its relevant boundary, and the precise distinction from this work.

Use a comparison table only if the features are consistently defined and verified for each paper. "Not reported" is different from "not supported." Venue prestige and citation count do not establish relevance. Do not exclude stronger conference baselines merely because the target is a journal.

## Method and system model

Read [model and analysis](model-and-analysis.md). Start from entities, information flow, and timing; introduce the mechanism in the order it runs. For each design component explain its input, operation, output, and reason. Formalization should describe the implemented or evaluated system, with deviations disclosed.

## Evaluation and Results

Read [evaluation](evaluation.md). Organize by questions, not by a tour of figures. A result paragraph should identify the tested claim, specify the comparison and condition, report the observation, then explain its interpretation with appropriate uncertainty. Report exceptions that constrain the central claim.

## Discussion and limitations

Use a separate section only when it helps. Explain which assumptions limit generalization, which costs remain, and which failure cases matter. An unimplemented extension is future work. Do not disguise a needed validation as a solved limitation.

## Conclusion

Close with the mechanism, the decisive verified outcome, and the system-level implication under the tested conditions. Introduce no new experiment, theorem, or guarantee. Avoid broad claims about every mobile environment when evidence covers a few datasets or devices.

## Chinese notes to English prose

First extract propositions and their evidence, then write the logical chain in English. Preserve distinctions such as `轮数/rounds`, `时间/wall-clock time`, `功率/power`, `能量/energy`, `异步/asynchronous`, and `半同步/semi-synchronous`. Clarify whether `提升 5%` means five percentage points or a five-percent relative change before finalizing a quantitative claim.
