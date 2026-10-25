# Manuscript review checklist

Use this as a diagnostic, not a promise of acceptance. Report only issues supported by the available manuscript and artifacts.

## Read for the central argument

- Can the mobile-computing problem and its technical failure mechanism be stated concretely?
- Is the gap supported by verified prior work or author evidence?
- Does the proposed mechanism address that gap, and do the contributions reflect distinct advances?
- Are the title, abstract and conclusion no stronger than the analysis and evaluated scope?

## Read for mathematical and system consistency

- Are entities, information, time indices, resources, units and variable domains defined?
- Does the optimization/controller use information available at decision time?
- Do feasibility, theorem assumptions, update rules and implementation describe compatible systems?
- Are theorem strengths, surrogate objectives and complexity claims stated accurately?
- Are privacy and fairness claims tied to explicit definitions rather than slogans?

## Read for evidence

- Does each main claim have an actual experiment or proof with a source locator?
- Do time, energy, memory and traffic metrics support the claimed benefit directly?
- Are baselines, tuning, budgets and stopping conditions comparable and disclosed?
- Do ablations test the mechanism and include relevant overhead?
- Are simulations, traces, emulation and testbed experiments labelled accurately?
- Are variability, failures, scale and relevant operating boundaries visible?

## Read for reproducibility and submission consistency

- Can the model/task, split, partition, hyperparameters, hardware and measurement procedure be recovered?
- Do figure values agree with tables, abstract and response letter?
- Are figure/section/equation/citation labels resolved in the final version?
- Are code/data availability and repository status stated truthfully?
- Have current TMC instructions been consulted for exact submission-stage requirements?

For each finding, provide `priority | verified location | problem | consequence | concrete repair`. Separate missing information from demonstrated errors. If only an excerpt was provided, bound the review to the excerpt. Do not claim that inaccessible appendices, code or proofs were checked.
