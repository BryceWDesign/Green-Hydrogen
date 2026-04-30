# Maturity Model

## Purpose

This document defines the current maturity state of Green-Hydrogen.

The percentages in this repository are not physical proof scores. They are project-formation estimates used to show how complete the architecture, validation plan, safety logic, and proof path are.

A high architecture percentage does not mean the system has proven hydrogen output.

The only defensible physical proof score comes from measured runs.

## Current Summary

| Area | Current Estimate | Status |
|---|---:|---|
| Credible design architecture | 90-94% | Strong enough to preserve and structure as a repo. |
| Lab prototype plan | 70-78% | Usable first-build path, but hardware still needs locking. |
| Safety/control architecture | 88-93% | Strong policy-gated logic, pending real sensor integration. |
| Measurement/validation architecture | 88-94% | Strong evidence design, pending calibrated instruments. |
| Defensible green-H2 proof | 25-35% | Still low until physical data exists. |

## Plain-English Meaning

The project is mature as an architecture.

It is not mature as a proven hydrogen system.

The repo is currently strong in:

- system decomposition,
- safety boundaries,
- evidence-gated claims,
- validation sequencing,
- donor-architecture integration,
- baseline-first testing,
- and claim discipline.

The repo is still weak in:

- real hardware selection,
- measured hydrogen output,
- gas purity records,
- repeatability data,
- degradation data,
- thermal accounting,
- carbon-intensity proof,
- and third-party review.

## Maturity Area 1: Credible Design Architecture

Current estimate: 90-94%

This area measures whether the system concept is internally coherent and organized enough to build a serious validation repo.

### What Is Already Strong

- The architecture has a clear baseline electrolysis path.
- Advanced branches are separated from the baseline.
- Water verification is included before production claims.
- Energy input is treated as evidence, not assumption.
- Gankyil phase management has a bounded role.
- Gas verification is treated as mandatory.
- Safety gates can block runs.
- Carbon accounting is included.
- The repo rejects unsupported performance claims.
- Evidence bundles are treated as the center of proof.

### Why It Is Not 100%

The architecture still lacks:

- exact bench layout dimensions,
- exact electrolyzer hardware,
- exact sensor models,
- exact gas path hardware,
- exact chamber geometry,
- exact thermal interface design,
- exact calibration equipment,
- and exact first-run acceptance thresholds.

### Upgrade Path to 95%+

To push architecture maturity above 95%, the repo must lock:

1. First bench configuration.
2. Hardware class for every subsystem.
3. Sensor placement rules.
4. Gankyil-A prototype geometry.
5. Baseline separator geometry.
6. Gas measurement method.
7. Water-quality method.
8. Power measurement method.
9. Data logging format.
10. First acceptance thresholds.

## Maturity Area 2: Lab Prototype Plan

Current estimate: 70-78%

This area measures how close the project is to a physically buildable bench plan.

### What Is Already Strong

- The first build is intentionally conservative.
- The first build is non-pressurized.
- The first build is baseline-first.
- Gankyil-A is treated as an A/B comparison, not a guaranteed improvement.
- Optional plasma, PEC, and redox branches are not allowed in the first baseline build.
- Safety preflight is required.
- Evidence bundles are required.

### Why It Is Not Higher

A lab prototype plan is not complete until the repo includes:

- full BOM,
- exact assembly walkthrough,
- wiring and plumbing layout,
- exact sensor models,
- exact gas handling components,
- exact mounting method,
- exact ventilation constraints,
- exact emergency shutdown method,
- exact test duration limits,
- exact cleaning procedure,
- and exact failure-response actions.

### Upgrade Path to 85%+

To push lab prototype planning above 85%, the repo must add:

1. Complete supplier-neutral BOM.
2. Step-by-step assembly walkthrough.
3. Bench layout diagram.
4. Wiring map.
5. Tubing and gas path map.
6. Sensor calibration checklist.
7. Leak-test procedure.
8. Water-verification procedure.
9. Baseline electrolysis procedure.
10. Gankyil-A A/B test procedure.

## Maturity Area 3: Safety and Control Architecture

Current estimate: 88-93%

This area measures whether the project has serious safety logic and claim-control discipline.

### What Is Already Strong

- Unsafe branches are blocked by default.
- Plasma/catalyst activation is not allowed without review.
- Pressure storage is rejected for the first build.
- Missing ventilation blocks a run.
- Missing leak-check blocks a run.
- Missing emergency stop blocks a run.
- Missing sensor evidence blocks acceptance.
- Unknown power source blocks green-hydrogen claims.
- The state machine uses conservative transitions.
- Safety receipts are preserved.

### Why It Is Not 100%

The safety architecture is not complete until it is tied to:

- real hydrogen sensor limits,
- real oxygen sensor limits,
- real ventilation calculations,
- real emergency stop hardware,
- real electrical protection,
- real thermal cutoffs,
- real operator procedures,
- and real post-run shutdown checks.

### Upgrade Path to 95%+

To push safety/control above 95%, the repo must lock:

1. Maximum run duration.
2. Maximum current.
3. Maximum voltage.
4. Maximum temperature.
5. Hydrogen concentration stop threshold.
6. Oxygen crossover stop threshold.
7. Leak-test threshold.
8. Emergency shutdown hardware.
9. Ventilation requirement.
10. Operator checklist.

## Maturity Area 4: Measurement and Validation Architecture

Current estimate: 88-94%

This area measures whether the repo has a serious evidence design.

### What Is Already Strong

- Runs require structured evidence.
- Receipts preserve claim state.
- Water records are required.
- Power records are required.
- Gas records are required.
- Safety records are required.
- Carbon accounting is included.
- Acceptance logic distinguishes accepted, rejected, inconclusive, and blocked.
- The project rejects visual-only claims.
- Advanced branches require separate comparison evidence.

### Why It Is Not 100%

The validation architecture is not complete until the repo defines:

- exact sensor models,
- calibration methods,
- uncertainty handling,
- repeat count,
- acceptable drift,
- blank controls,
- negative controls,
- positive controls,
- baseline repeatability criteria,
- and third-party review format.

### Upgrade Path to 95%+

To push validation maturity above 95%, the repo must include:

1. Calibration checklist.
2. Gas verification checklist.
3. Hydrogen sensor uncertainty note.
4. Flow measurement uncertainty note.
5. Power meter uncertainty note.
6. Water meter uncertainty note.
7. Baseline repeat-run rule.
8. Gankyil-A A/B comparison rule.
9. Failed-run preservation rule.
10. Independent review packet template.

## Maturity Area 5: Defensible Green-Hydrogen Proof

Current estimate: 25-35%

This area measures actual proof, not design quality.

### Why This Score Is Still Low

The repo does not yet contain measured physical data.

There is currently no recorded:

- hydrogen output rate,
- hydrogen purity,
- gas volume,
- gas flow,
- oxygen crossover measurement,
- water consumption,
- electrical input trace,
- thermal input trace,
- solar input trace,
- carbon-intensity result,
- leak-test record,
- repeatability result,
- or degradation result.

Because of that, the project cannot honestly claim verified green hydrogen.

### What Would Raise This Score

The score rises only when real evidence exists.

Approximate proof-stage progression:

| Proof Stage | Expected Proof Range | Meaning |
|---|---:|---|
| Architecture only | 20-35% | Coherent plan, no physical proof. |
| First detected hydrogen | 35-45% | Gas detection exists, but may be weak or incomplete. |
| Calibrated gas evidence | 45-60% | Hydrogen measurement becomes credible. |
| Energy and water accounting | 60-70% | Inputs are measured well enough to evaluate production. |
| Repeat baseline runs | 70-80% | Result is repeatable in the same setup. |
| A/B comparison data | 80-88% | Gankyil-A or assist branches can be fairly compared. |
| Carbon-traceable renewable runs | 88-93% | Green-hydrogen claim becomes more defensible. |
| Independent review and replication | 93-97% | External confidence improves significantly. |
| Standards-aligned validation | 97-100% | Strongest practical proof class for the bounded bench system. |

## Definition of 90-94% Architecture

The phrase "90-94% architecture" means:

- the concept is no longer loose brainstorming,
- the major subsystems have assigned roles,
- the safety boundaries are clear,
- the evidence model is defined,
- the repo can be structured,
- and the next missing pieces are mostly hardware-lock and physical validation details.

It does not mean:

- 90-94% chance of success,
- 90-94% efficiency,
- 90-94% complete product,
- 90-94% proven science,
- or 90-94% ready for deployment.

## Readiness Gates

## Gate 0: Repository Preservation

Status: complete

Required:

- project snapshot,
- architecture,
- license,
- safety boundary,
- validation plan,
- source reuse map,
- code scaffold,
- and evidence examples.

## Gate 1: Bench Plan Complete

Status: in progress

Required:

- full BOM,
- assembly walkthrough,
- test procedure,
- safety procedure,
- sensor selection,
- calibration checklist,
- and acceptance criteria.

## Gate 2: Dry Run Complete

Status: not complete

Required:

- run-intent file,
- safety preflight dry pass,
- evidence bundle dry pass,
- acceptance dry pass,
- and rejected-run example.

## Gate 3: Baseline Hydrogen Detection

Status: not complete

Required:

- baseline electrolysis run,
- hydrogen detection,
- measured input power,
- water record,
- leak check,
- safety receipt,
- and operator notes.

## Gate 4: Calibrated Baseline Evidence

Status: not complete

Required:

- calibrated hydrogen measurement,
- gas flow or gas volume estimate,
- oxygen-side observation,
- repeat baseline run,
- uncertainty note,
- and carbon accounting.

## Gate 5: Gankyil-A A/B Test

Status: not complete

Required:

- baseline separator run,
- Gankyil-A separator run,
- same water conditions,
- same electrical conditions,
- same sensor setup,
- liquid carryover observation,
- gas path stability observation,
- and repeated comparison.

## Gate 6: Solar Thermal Assist Test

Status: not complete

Required:

- stable baseline,
- measured thermal input,
- measured electrical input,
- temperature monitoring,
- control run,
- assisted run,
- and total energy accounting.

## Gate 7: Advanced Branch Review

Status: blocked by default

Required for any plasma/catalyst, PEC, or redox branch:

- separate hazard review,
- separate test article,
- separate evidence bundle,
- no pressure storage,
- no shared claim with baseline,
- and explicit review approval.

## Gate 8: Repeatability Package

Status: not complete

Required:

- minimum three comparable runs,
- same configuration,
- same evidence fields,
- anomaly tracking,
- drift tracking,
- and repeatability decision.

## Gate 9: External Review Packet

Status: not complete

Required:

- architecture summary,
- BOM,
- assembly notes,
- calibration records,
- raw observations,
- accepted runs,
- rejected runs,
- safety receipts,
- and claim-boundary statement.

## Score Integrity Rules

These rules prevent false maturity inflation.

1. Do not raise the physical proof score without physical data.
2. Do not raise the green-hydrogen proof score without carbon traceability.
3. Do not raise safety maturity without real hardware limits.
4. Do not raise validation maturity without calibration methods.
5. Do not treat one successful run as repeatability.
6. Do not treat gas bubbles as verified hydrogen.
7. Do not treat solar proximity as renewable traceability.
8. Do not treat optional assist branches as baseline proof.
9. Do not accept missing evidence as zero risk.
10. Do not delete failed or blocked runs.

## Current Best Honest Claim

The strongest honest claim at this stage is:

Green-Hydrogen is a mostly formed, measurement-first architecture and lab-validation scaffold for testing a solar-assisted hydrogen production concept under conservative bench conditions. It includes safety gates, evidence receipts, carbon accounting, and branch isolation, but it does not yet contain physical proof of green hydrogen production.

## Current Forbidden Claims

Do not claim:

- "This produces green hydrogen."
- "This is efficient."
- "This is net-positive."
- "This is commercially ready."
- "This is safe to build without review."
- "This solves hydrogen production."
- "The Gankyil path improves output."
- "Plasma assist improves efficiency."
- "Solar thermal assist reduces energy cost."
- "The system is validated."

Each of those claims requires measured evidence that does not yet exist in this repo.

## Next Maturity Targets

The next practical target is not 100%.

The next target is a repo that lets a careful reviewer understand exactly how the first safe bench proof would be attempted.

Target after BOM and assembly walkthrough:

| Area | Possible Near-Term Estimate |
|---|---:|
| Credible design architecture | 94-96% |
| Lab prototype plan | 82-88% |
| Safety/control architecture | 92-95% |
| Measurement/validation architecture | 92-96% |
| Defensible green-H2 proof | 25-35% |

The physical proof score should remain unchanged until real measurements exist.
