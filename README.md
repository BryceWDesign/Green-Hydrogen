# Green-Hydrogen

Measurement-first validation scaffold for a solar-assisted green-hydrogen bench proof path.

## Current Status

Green-Hydrogen is a structured architecture and validation repository.

It is not a proven hydrogen-production system.

It is not a certified green-hydrogen system.

It is not commercial equipment.

It is not a pressure system.

It is not a claim of net-positive hydrogen production.

The repository preserves the current project architecture and organizes it into a reviewable proof-of-concept path with:

- water verification,
- baseline electrolysis reference planning,
- non-pressurized gas handling,
- Gankyil-A phase-management comparison,
- hydrogen-specific gas verification,
- safety preflight,
- hazard controls,
- evidence receipts,
- acceptance logic,
- carbon/source accounting,
- and conservative claim boundaries.

## Core Principle

No claim is accepted without evidence.

A hydrogen claim requires hydrogen-specific detection.

A green-hydrogen claim requires hydrogen evidence, water evidence, measured energy input, renewable-source traceability, carbon accounting, safety records, and bounded acceptance.

Visible bubbles are not hydrogen proof.

Solar hardware nearby is not renewable traceability.

A visually interesting vortex is not production improvement.

Unknown data stays unknown.

## Current Maturity Estimate

These values are project-formation estimates, not physical proof scores.

| Area | Current Estimate | Meaning |
|---|---:|---|
| Credible design architecture | 90-94% | The architecture is mostly formed and internally coherent. |
| Lab prototype plan | 70-78% | The first-build path is usable but exact hardware still needs locking. |
| Safety/control architecture | 88-93% | Strong policy-gated safety logic, pending exact real-world limits. |
| Measurement/validation architecture | 88-94% | Strong evidence design, pending calibrated instruments and physical runs. |
| Defensible green-H2 proof | 25-35% | Still low until measured gas, water, energy, carbon, and repeatability data exist. |

The blunt boundary:

The architecture is strong enough to preserve, review, and build toward.

The physical proof is still early because the repo does not yet contain measured hydrogen output, gas purity, energy input traces, carbon intensity, degradation data, or repeatability data.

## What This Repo Is

Green-Hydrogen is a bench-validation scaffold for testing a solar-assisted hydrogen-production concept under conservative conditions.

It is designed to help answer:

1. Did the system produce detectable hydrogen?
2. Was the detection hydrogen-specific?
3. Was the water source documented?
4. Was electrical input measured?
5. Was any solar or thermal input actually recorded?
6. Was the gas path non-pressurized?
7. Was the gas path leak-checked?
8. Was the run safely bounded?
9. Was the evidence complete enough to review?
10. What claim, if any, is allowed?

## What This Repo Is Not

This repo is not:

- a finished hydrogen generator,
- a commercial electrolyzer,
- a pressure-rated hydrogen system,
- a hydrogen storage design,
- a certified gas appliance,
- a safety certification,
- a field-deployment manual,
- a claim of high efficiency,
- a claim of net-positive energy,
- a claim of verified green hydrogen,
- a claim that Gankyil-A improves hydrogen output,
- or a claim that plasma, PEC, redox, or thermal assist branches work.

## First-Build Target

The first physical target is:

```
GH-BENCH-A0
```

GH-BENCH-A0 is intended to be:

- bench-scale,
- low-output,
- non-pressurized,
- supervised,
- ventilated,
- current-limited,
- baseline-first,
- instrumented,
- manually inspectable,
- evidence-driven,
- and easy to shut down.

It is not intended to maximize output.

It is intended to make the first proof path safer, clearer, and harder to overclaim.

## First Proof-of-Concept Goal

The first proof-of-concept goal is:

```
Demonstrate a supervised, non-pressurized baseline bench run with documented water input, measured electrical input, documented gas path, safety preflight, hydrogen-specific detection, evidence receipt, and bounded acceptance decision.
```

That proof does not automatically prove green hydrogen.

A green-hydrogen claim requires source traceability and carbon accounting.

## Architecture Overview

```
Water Verification
  -> Energy Input
  -> Baseline Electrolysis Reference
  -> Gas-Liquid Handling
  -> Gas Verification
  -> Safety Gate
  -> Evidence Bundle
  -> Carbon Accounting
  -> Acceptance Decision
  -> Claim Boundary
```

## Main Layers

## 1. Water Verification

The water record protects the project from vague input claims.

Required evidence includes:

- water source,
- water volume,
- water temperature,
- pH,
- TDS or conductivity,
- visible clarity,
- electrolyte use,
- and contamination notes.

Unknown water weakens interpretation.

## 2. Energy Input

The project records energy before making energy claims.

Minimum electrical evidence includes:

- source type,
- voltage,
- current,
- duration,
- estimated watt-hours,
- current limit,
- protection hardware,
- emergency disconnect,
- and measurement method.

## 3. Baseline Electrolysis Reference

The baseline branch is the conservative first path.

It should use a low-output documented electrolysis reference module or equivalent conservative setup.

The baseline path is tested before Gankyil-A, solar thermal assist, plasma/catalyst activation, PEC, redox, or hybrid branches.

## 4. Gas-Liquid Handling

The first baseline separator path provides the A-side comparison.

Gankyil-A provides the B-side comparison later.

No separator or Gankyil chamber may create pressure storage.

## 5. Gankyil-A Phase Management

Gankyil-A is a passive phase-management test article.

Allowed role:

- reduce liquid carryover,
- reduce sensor wetting,
- improve gas path stability,
- improve condensate visibility,
- improve repeatability of gas verification.

Forbidden role:

- claiming hydrogen output increase,
- claiming electrolysis efficiency improvement,
- claiming vortex energy,
- claiming green hydrogen.

## 6. Gas Verification

Hydrogen claims require hydrogen-specific evidence.

Visible bubbles alone are not enough.

A stronger gas record may include:

- hydrogen detector model,
- calibration or bump-test state,
- hydrogen response,
- flow or volume estimate,
- oxygen-side observation,
- gas path description,
- leak-check result,
- wetness protection,
- and sensor limitation notes.

## 7. Safety Gate

The safety gate blocks unsafe or incomplete runs before operation.

Required preflight fields include:

```
operator_present
ventilation_present
no_pressure_storage
no_sealed_accumulation
no_ignition_sources
emergency_disconnect_present
leak_check_passed
water_electric_separation_confirmed
sensors_connected
sensor_wetness_protection_confirmed
gas_path_documented
vent_path_defined
branch_selected
run_duration_bounded
prior_anomalies_resolved
evidence_forms_ready
```

If any required field fails, the run is blocked.

## 8. Evidence Receipts

Every run should produce a receipt showing:

- what was attempted,
- what branch was selected,
- what evidence exists,
- what evidence is missing,
- whether safety passed,
- whether hydrogen-specific evidence exists,
- whether a green claim is supported,
- what anomalies occurred,
- and what claim status is allowed.

## 9. Carbon Accounting

Hydrogen is not green by default.

A green-hydrogen claim requires:

- hydrogen-specific evidence,
- water evidence,
- power evidence,
- source traceability,
- renewable fraction,
- carbon assumptions,
- safety preflight,
- and bounded acceptance.

Unknown energy source blocks the green claim.

Unknown battery charge source blocks the green claim.

Unmeasured thermal input blocks efficiency claims.

## 10. Acceptance Logic

Acceptance states are intentionally conservative.

Allowed statuses:

```
accepted_bounded_result
accepted_bounded_phase_management_improvement
accepted_bounded_research_result
rejected
inconclusive
requires_rerun
blocked_by_safety_gate
blocked_by_missing_evidence
blocked_by_missing_baseline
blocked_by_advanced_branch_policy
```

Forbidden statuses:

```
proven
certified
commercial_ready
green_hydrogen_confirmed
efficiency_improved
net_positive
safe_for_deployment
```

## Repository Structure

```
Green-Hydrogen/
  NOTICE
  README.md
  pyproject.toml
  .gitignore

  docs/
    project_snapshot.md
    system_architecture.md
    maturity_model.md
    source_reuse_map.md
    first_build_target.md
    bom_bench_validation_rig.md
    bom_sensors_gas_safety.md
    bom_power_solar_thermal_logging.md
    assembly_walkthrough_baseline_rig.md
    assembly_walkthrough_gankyil_a.md
    assembly_walkthrough_gas_verification_rack.md
    safety_policy.md
    hazard_register.md
    validation_plan.md
    test_matrix.md
    gankyil_phase_management.md
    advanced_branches.md
    evidence_control_plane.md

  src/
    green_hydrogen/
      __init__.py
      metrics.py
      gankyil.py
      policy.py
      preflight.py
      state_machine.py
      receipt.py
      evidence_bundle.py
      acceptance.py
      carbon_accounting.py

  schemas/
    run_intent.schema.json
    safety_preflight.schema.json
    evidence_bundle.schema.json

  examples/
    baseline_pem_1g_hr_run_intent.json
    gankyil_ab_test_run_intent.json
    plasma_assist_blocked_review_required.json
    rejected_missing_evidence_bundle.json

  scripts/
    smoke_test.py

  tests/
    test_policy_preflight.py
    test_acceptance.py
    test_metrics_carbon_gankyil.py

  run_bundles/
    .gitkeep
```

## Documentation Map

| Document | Purpose |
|---|---|
| `docs/project_snapshot.md` | Current state, scope, maturity, and claim boundary. |
| `docs/system_architecture.md` | Full layered system architecture. |
| `docs/maturity_model.md` | Explains percentage estimates and proof limits. |
| `docs/source_reuse_map.md` | Records donor design-pattern reuse without claim transfer. |
| `docs/first_build_target.md` | Defines GH-BENCH-A0. |
| `docs/bom_bench_validation_rig.md` | Supplier-neutral bench rig BOM. |
| `docs/bom_sensors_gas_safety.md` | Sensor, gas verification, and safety BOM. |
| `docs/bom_power_solar_thermal_logging.md` | Power, solar, thermal, and logging BOM. |
| `docs/assembly_walkthrough_baseline_rig.md` | First baseline assembly walkthrough. |
| `docs/assembly_walkthrough_gankyil_a.md` | Gankyil-A assembly and A/B test walkthrough. |
| `docs/assembly_walkthrough_gas_verification_rack.md` | Gas verification rack walkthrough. |
| `docs/safety_policy.md` | Safety boundaries and blocking rules. |
| `docs/hazard_register.md` | Hazard register for GH-BENCH-A0. |
| `docs/validation_plan.md` | Validation levels and proof sequence. |
| `docs/test_matrix.md` | Structured test matrix. |
| `docs/gankyil_phase_management.md` | Gankyil concept, constraints, and claim limits. |
| `docs/advanced_branches.md` | Solar, thermal, plasma, PEC, redox, and hybrid branch boundaries. |
| `docs/evidence_control_plane.md` | Run intent, evidence, receipt, and acceptance flow. |

## Software Modules

| Module | Purpose |
|---|---|
| `metrics.py` | Scores water, power, gas, carbon, repeatability, and Gankyil evidence quality. |
| `gankyil.py` | Checks Gankyil-A installation and A/B phase-management comparison records. |
| `policy.py` | Blocks unknown or under-reviewed branches. |
| `preflight.py` | Blocks unsafe or incomplete safety preflight records. |
| `state_machine.py` | Tracks conservative validation states. |
| `receipt.py` | Generates compact run receipts. |
| `evidence_bundle.py` | Checks required run-bundle evidence. |
| `acceptance.py` | Converts evidence into bounded acceptance decisions. |
| `carbon_accounting.py` | Evaluates source traceability and caller-supplied carbon assumptions. |

## Running Tests

Install test tooling as appropriate for your Python environment, then run:

```
python -m pytest
```

Run the dry smoke test:

```
python scripts/smoke_test.py
```

The smoke test writes a dry result to:

```
run_bundles/GH-A0-SMOKE-001-smoke_result.json
```

The smoke test is not physical evidence.

It only confirms the repo’s software path can create a bounded dry acceptance result.

## Example Run Intents

The repo includes dry examples:

| Example | Purpose |
|---|---|
| `examples/baseline_pem_1g_hr_run_intent.json` | Dry baseline intent. Filename is a planning label, not verified output. |
| `examples/gankyil_ab_test_run_intent.json` | Dry Gankyil-A A/B comparison intent. |
| `examples/plasma_assist_blocked_review_required.json` | Shows plasma/catalyst branch blocked by default. |
| `examples/rejected_missing_evidence_bundle.json` | Shows missing evidence should fail closed. |

## Important Note on the Baseline Example Filename

The file:
```
examples/baseline_pem_1g_hr_run_intent.json
```

uses `1g_hr` as a nominal planning label only.

It is not a verified production rate.

No output rate is proven until physical gas measurement exists.

## Validation Levels

| Level | Name | Meaning |
|---:|---|---|
| 0 | Repo-only validation | Repo structure and logic exist. |
| 1 | Dry evidence validation | Bad runs can be blocked in software. |
| 2 | Physical assembly validation | Bench layout and safety setup are documented. |
| 3 | Baseline hydrogen detection | Hydrogen-specific detection is recorded. |
| 4 | Calibrated baseline measurement | Sensor confidence improves. |
| 5 | Repeat baseline runs | Repeatability begins. |
| 6 | Gankyil-A A/B comparison | Phase-management behavior is compared. |
| 7 | Solar electrical traceability | Energy source path is documented. |
| 8 | Solar thermal assist validation | Thermal input is measured and counted. |
| 9 | Carbon-traceable green-H2 evidence | Bounded green-H2 claim becomes possible. |
| 10 | External review package | Evidence is packaged for outside review. |

## First Proof Package

The minimum first proof package should include:

```
T-000 repo smoke test
T-001 valid baseline dry run
T-002 missing evidence blocked
T-003 plasma branch blocked
T-005 six-zone layout
T-006 non-pressurized gas path
T-007 emergency disconnect
T-008 water verification
T-009 power measurement
T-010 gas verification rack readiness
T-011 baseline hydrogen detection run
T-024 carbon accounting check
T-026 failed-run preservation
```

## Minimum Physical Baseline Evidence

A minimum physical baseline run requires:

```
run_intent.json
safety_preflight.json
water_record.json
power_record.json
gas_record.json
carbon_record.json
receipt.json
acceptance.json
notes.md
setup_photos/
```

The run can be accepted only if it includes:

- passed safety preflight,
- no pressure storage,
- no sealed accumulation,
- ventilation confirmed,
- leak check passed,
- emergency disconnect present,
- water record present,
- power record present,
- gas path documented,
- hydrogen-specific detection present,
- sensor not corrupted by wetness,
- operator notes present,
- and bounded acceptance.

## Minimum Gankyil-A Evidence

A Gankyil-A phase-management claim requires:

```
baseline_run_reference.json
gankyil_run_reference.json
comparison_conditions.json
phase_management_metrics.json
acceptance.json
notes.md
setup_photos/
```

Allowed bounded claim:
```
Under GH-BENCH-A0 test conditions, Gankyil-A improved one or more practical phase-management metrics compared with the baseline separator path.
```

Forbidden claim:

```
Gankyil-A improved hydrogen production.
```

## Minimum Green-Hydrogen Claim Evidence

A bounded green-hydrogen claim requires:

- hydrogen-specific detection,
- water record,
- power record,
- energy source record,
- renewable fraction known or bounded,
- carbon accounting assumptions,
- safety preflight,
- leak check,
- non-pressurized gas path,
- acceptance decision,
- and claim boundary.

If any of those are missing, the green claim is blocked.

## Advanced Branches

Advanced branches are preserved as future research paths.

They are not part of the first baseline proof.

| Branch | Status |
|---|---|
| `solar_electrical` | Optional later after source metering exists. |
| `solar_thermal_assist` | Optional later after baseline stability and thermal measurement. |
| `plasma_catalyst` | Blocked by default. Requires formal review. |
| `pec` | Future-only. Requires separate test article. |
| `redox` | Future-only. Requires chemistry and disposal review. |
| `hybrid_future` | Future-only. Requires single-branch evidence first. |

## Safety Boundary

The first build must not include:

- pressure storage,
- compression,
- sealed gas accumulation,
- flame testing,
- spark testing,
- high-voltage plasma hardware,
- unreviewed catalysts,
- mystery electrolytes,
- unattended operation,
- unventilated indoor operation,
- hidden gas routing,
- blocked vent paths,
- or output chasing before measurement is stable.

## Stop Conditions

Stop a physical run immediately if:

- hydrogen accumulation is suspected,
- ventilation changes,
- leak is suspected,
- tubing disconnects,
- gas path becomes blocked,
- liquid reaches sensor,
- sensor saturates or behaves unexpectedly,
- unexpected heat occurs,
- power behavior changes unexpectedly,
- sparking, smoke, odor, discoloration, or noise appears,
- electrolyte spills,
- operator loses line of sight,
- evidence logging fails,
- or any operator safety concern appears.

A stopped run is useful evidence.

Do not delete it.

## Claim Ladder

Allowed escalation path:

```
visual gas observation
  -> hydrogen-specific detection
  -> bounded hydrogen measurement
  -> output estimate
  -> repeatable output estimate
  -> renewable-source traceability
  -> carbon-accounted bounded green-H2 claim
  -> external review package
```

Forbidden escalation:
```
visual bubbles
  -> hydrogen proven
  -> green hydrogen proven
  -> efficient system
  -> commercial readiness
```

## Current Best Honest Claim

The strongest honest claim at the current repo stage is:
```
Green-Hydrogen is a mostly formed, measurement-first architecture and lab-validation scaffold for testing a solar-assisted hydrogen production concept under conservative bench conditions. It includes safety gates, evidence receipts, carbon accounting, Gankyil-A phase-management comparison, and branch isolation, but it does not yet contain physical proof of green hydrogen production.
```

## Current Forbidden Claims

Do not claim:
```
Green-Hydrogen has produced verified hydrogen.
Green-Hydrogen has produced verified green hydrogen.
Green-Hydrogen is efficient.
Green-Hydrogen is net-positive.
Green-Hydrogen is commercially ready.
Green-Hydrogen is safe for unsupervised operation.
Gankyil-A improves hydrogen output.
Solar thermal assist improves efficiency.
Plasma/catalyst activation improves performance.
```

## Roadmap to Physical Validation

To move the repo closer to physical proof, the next missing pieces are:

1. Select exact low-output electrolysis reference hardware.
2. Select exact hydrogen detector or sensor.
3. Select exact oxygen-side observation method.
4. Select exact power meter.
5. Select exact water-quality tools.
6. Select exact leak-check method.
7. Select exact ventilation approach.
8. Lock Gankyil-A chamber material and geometry.
9. Create physical run sheets.
10. Run dry evidence validation.
11. Assemble GH-BENCH-A0.
12. Perform baseline hydrogen-specific detection.
13. Preserve accepted, rejected, and inconclusive runs.
14. Repeat baseline runs.
15. Only then attempt Gankyil-A A/B comparison.
16. Only after that consider solar electrical or thermal branches.

## Licensing

This repository is licensed under Apache-2.0.

See the `LICENSE` file already present in the GitHub repository.

## Final Rule

Green-Hydrogen should never try to look more proven than it is.

The value of this repo is not hype.

The value is that every claim must survive safety gates, measurements, missing-data checks, receipts, acceptance logic, and conservative review.
