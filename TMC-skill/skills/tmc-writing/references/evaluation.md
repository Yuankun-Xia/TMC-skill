# TMC evaluation planning and reporting

## Translate claims into questions

Use `claim -> test -> metric and budget -> baseline -> observed evidence -> limitation`.

| Claim | Useful evidence, when relevant |
|---|---|
| Faster learning | Wall-clock time to a common target; accuracy versus elapsed time; setup and control costs |
| Communication efficiency | Transferred bytes/bits to a common target; upload/download and protocol accounting |
| Energy efficiency | Measured or explicitly modelled energy; accuracy/utility versus energy; battery/idle assumptions |
| Memory feasibility | Peak client memory and failures on representative devices; parameter/activation/optimizer accounting |
| Asynchrony robustness | Staleness, straggler ratios, varying client speeds and participation; wall-clock progress and fairness |
| Decentralized scalability | Size and topology sweeps, failures/contact changes, convergence and traffic or energy costs |
| Mobility support | Contact duration, trajectories, missed uploads or deadlines; trace/simulator provenance |
| Privacy/security | Defined attack settings and adversary budget; attack metric, benign utility, and cost |
| Generality | Tasks, distributions, resources, or devices that test the claimed scope |

These are evidence choices, not a compulsory list of experiments. Prioritize what would change the conclusion. Read the corpus observations for examples of real-device versus simulated evidence.

## Keep comparisons fair

Compare at a declared common accuracy, time, energy, communication, or training-work budget. Explain trade-offs instead of combining incompatible budgets into one winner claim.

Report baseline version, configuration, tuning effort, model, data split, selected clients, hardware/simulator, stopping criterion, and repeated-run procedure as relevant. Use the same task and splits when a direct comparison requires them. Different payloads, local epochs, ranks, batch sizes, or precision can be legitimate design choices, but disclose them and account for their costs.

Include a simple baseline and strong mechanisms closest to the proposed design. An oracle or exhaustive search is useful for small problems when clearly labelled. Never call an implementation "official" without checking its source.

For non-IID FL, define the partition generator and seed, heterogeneity parameter, client sample sizes, label/feature/quantity skew, train/test split, and any drift. An alpha value alone is not a complete partition description. Do not invent a standard value to fill a missing setup.

## Isolate why the method works

Ablations should remove or replace a mechanism while holding the comparison budget meaningful. State how constraints remain feasible. Do not claim causal attribution when two conditions change the model size, training budget, and mechanism simultaneously.

Use sensitivity studies to expose a meaningful boundary: load, bandwidth, client count, resource imbalance, rank, contact duration, failure rate, privacy budget, or label/noise conditions. Select variables related to the paper's mechanism. Do not copy every sweep from another paper.

Report controller/solver overhead and a time or energy breakdown when adaptive decisions might consume the claimed savings. For fairness, report the operational definition and distribution/worst-client outcome where an average hides exclusion.

## Separate evidence levels

- **Simulation:** specify the abstraction and model assumptions; multiple processes/threads on one server are not a multi-device deployment.
- **Trace-driven evaluation/emulation:** identify what was measured versus replayed or modelled.
- **Real-device testbed:** give actual devices, runtime, network and measurement procedure; enumerate which experiments used the testbed.

Small testbed results and large simulations can complement each other. Do not describe the entire evaluation as on-device merely because one part used hardware. A realistic satellite constellation or SUMO road model remains a simulation.

## Quantities and uncertainty

For a reduction from baseline B to method M, use `(B - M) / B` for a relative reduction when B is positive. For a speedup use `B / M`. A change from 80% to 84% is 4 percentage points, or a 5% relative increase. State which quantity is reported.

Use variability across independent runs when available. Identify the number of runs and whether intervals show standard deviation, standard error, bootstrap intervals, or another construction. Do not treat epochs or correlated observations as independent repeated trials. A single run permits a curve but not invented error bars.

State timeouts, failures, censored time-to-target values, and excluded runs. A method that never reaches the target does not have a finite measured completion time. Do not interpolate beyond observed data or smooth curves without disclosure.

## Write Results as evidence

A compact pattern is: `At [condition/budget], [method] achieved [verified metric] versus [baseline]. [Diagnostic] is consistent with [mechanism]; however, [observed boundary] limits [claim].`

Avoid broad statements such as "outperforms all methods in all scenarios" when the tables contain exceptions. Use "statistically significant" only when an appropriate test and result support it. Retain numerical precision justified by the measurement.

Return an experiment plan as a plan with priorities and dependencies. Run experiments only when requested or implied by the task and resources are available. Never convert proposed tests into completed evidence in manuscript prose or reviewer replies.
