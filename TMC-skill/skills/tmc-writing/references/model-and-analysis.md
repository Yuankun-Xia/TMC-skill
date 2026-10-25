# System model, formulation, and analysis

## Model what the decision maker can observe

Specify the entities and roles: server, edge node, client, vehicle, UAV, satellite, peer, or adversary. State which entity chooses each variable and which information it has at decision time. A scheduler that uses future channel states or unobserved client data needs an oracle label or a realizable estimator.

Define the time unit: slot, epoch, communication round, aggregation event, orbital interval, or deadline window. Specify ordering, delays, stale version indices, dropped messages, and when resources become available. Use a timeline figure for asynchronous or overlapping operations when useful.

For FL, distinguish data heterogeneity from device/system heterogeneity and temporal drift. State the global objective weighting and how sampling or client selection alters it. Do not silently replace data-size weights with uniform client weights.

## Account for relevant resources

| Resource | Questions that affect correctness |
|---|---|
| Communication | Payload in bits or bytes? Upload and download? Metadata, peer traffic, retransmissions, compression coding and synchronization? Shared bandwidth and link availability? |
| Computation | Operations, elapsed training time, inference interference, preprocessing, solver/control overhead? CPU/GPU parallelism or sequential work? |
| Memory | Model parameters, gradients, optimizer states, activations, buffers, server aggregation? Peak or allocated memory, per client or system-wide? |
| Energy | Integrated measured power, modelled energy, idle time, radio cost, battery condition? Define included components and units. |
| Topology/mobility | Link direction, connectivity over time, mixing weights, contact durations, vehicle residence time, task/deadline feasibility? |
| Fairness | Selection frequency, data coverage, workload, per-client utility, worst-client performance? Name and define the chosen metric. |

Do not require every row for every paper. Include what supports the specific claim. For concurrent compute and upload, a maximum or pipeline schedule may be appropriate; summing all tasks as sequential time requires justification.

For LoRA/PEFT, specify rank, modules, frozen parameters, precision, batch/sequence sizes, and rank/memory feasibility. Explain aggregation across heterogeneous ranks and the cost of projections, padding, conversion, or server reconstruction. These are reporting checks, not assumptions about any unpublished design.

## Formulate the actual problem

Define variables, domains, objective, constraints, and information assumptions before presenting a solver. State units and normalization for multi-objective weights. Distinguish a per-round proxy from total time/energy to a learning target.

If a convergence bound motivates a surrogate, show which terms depend on the decisions. Explain which constants are unknown or estimated. Optimizing a bound does not automatically minimize the measured learning loss.

Use precise difficulty claims:

- Nonconvexity alone does not prove NP-hardness.
- A relaxation needs a feasible recovery rule and a stated relation to the original problem.
- Alternating optimization needs a well-defined subproblem, update order, termination condition, and feasible output.
- Lyapunov/online control needs queue updates, constraints, available observations, and the scope of its stability/regret statement.
- An MDP/RL controller needs observable state, action feasibility, reward, transition assumptions, training/deployment costs, and constraints at execution time.

## State guarantees at their proved strength

Make a theorem readable as `assumptions -> quantity bounded -> parameter regime -> rate or guarantee`. Match convex/nonconvex, deterministic/stochastic, expected/high-probability, finite-time/asymptotic, local/global distinctions to the actual proof.

Check indexing and conditioning of stochastic expectations; independence assumptions for client sampling, noise, and topology; bounded delay and gradient assumptions; stochasticity/connectivity of mixing matrices; and constants that may grow with heterogeneity. Do not silently add stronger assumptions to repair a proof.

For privacy/security, define the adversary, information visibility, corruption/collusion scope, and mechanism. DP needs a neighboring relation, clipping/sensitivity, noise calibration and composition/accounting under the stated sampling. Encryption and keeping data local are different claims. Do not infer formal protection from an empirical attack failing.

## Complexity and implementation

State complexity in meaningful dimensions: clients, edges, parameters/rank, iterations, or problem size. Include the update frequency and the coordinator cost when they matter. Distinguish asymptotic complexity, measured controller runtime, and end-to-end latency. Describe numerical tolerances and the behavior on infeasible inputs if they affect reproducibility.

If a derivation is incomplete, identify the exact unsupported step and its consequences; do not manufacture a proof. Offer a conditional statement, a weaker claim, or an experiment that tests the boundary.
