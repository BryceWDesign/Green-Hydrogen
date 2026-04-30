# First-Build Target

## Purpose

This document defines the first physical build target for Green-Hydrogen.

The first build is not intended to maximize hydrogen output.

The first build is intended to create a conservative, reviewable, non-pressurized bench validation rig that can test whether the measurement architecture works.

The first build should answer:

1. Can the system produce detectable hydrogen under controlled baseline conditions?
2. Can the system measure the hydrogen credibly?
3. Can the system record water, energy, gas, safety, and carbon evidence?
4. Can the safety gate reject bad run intents?
5. Can the Gankyil-A phase-management path be compared against a simpler baseline path?
6. Can the repo preserve accepted, rejected, and inconclusive evidence without overclaiming?

## First-Build Name

Recommended first build name:

```
GH-BENCH-A0
```
Meaning:

GH = Green-Hydrogen
BENCH = bench-scale validation only
A0 = first non-field, non-pressurized architecture prototype
First-Build Claim Boundary

GH-BENCH-A0 may only support bounded bench claims.

Allowed claim after successful evidence:

```
GH-BENCH-A0 produced detectable hydrogen in a non-pressurized bench configuration under measured electrical input, with recorded water, safety, gas, and evidence data.
```
Forbidden claims:
```
GH-BENCH-A0 produces green hydrogen efficiently.
GH-BENCH-A0 is commercially ready.
GH-BENCH-A0 is safe for unsupervised operation.
GH-BENCH-A0 proves the advanced branches work.
GH-BENCH-A0 proves solar-assisted net-positive hydrogen.
GH-BENCH-A0 proves Gankyil-A increases hydrogen production.
```
Build Philosophy

The first build must be:

boring,
small,
visible,
non-pressurized,
ventilated,
manually supervised,
easy to shut down,
easy to inspect,
easy to disassemble,
easy to repeat,
and easy to reject if data is weak.

The first build must not be:

sealed,
pressurized,
hidden,
automated beyond basic logging,
optimized for output,
plasma-assisted,
high-temperature,
high-voltage,
unattended,
or configured for storage.
First-Build Scope

GH-BENCH-A0 includes:

Water verification station.
Low-output baseline electrolysis cell or equivalent conservative hydrogen-generation reference.
Non-pressurized gas-liquid separation path.
Optional removable Gankyil-A phase-management chamber for A/B comparison.
Hydrogen detection method.
Oxygen-side observation method.
Flow, volume, or qualitative gas-output measurement method.
Electrical input measurement.
Optional thermal input measurement, disabled by default.
Ventilation and leak-check discipline.
Emergency shutdown path.
Evidence-bundle record.

GH-BENCH-A0 excludes:

Pressure storage.
Compression.
Flame tests.
Indoor unventilated operation.
High-current optimization.
Plasma/catalyst activation.
PEC branch integration.
Redox-mediated chemistry.
Autonomous operation.
Any claim of commercial readiness.
First-Build Subsystems
Subsystem 1: Water Verification Station

Purpose:

Verify and document the water before any production claim.

Required records:

water source,
preparation date,
volume,
temperature,
pH,
conductivity or TDS,
visible clarity,
electrolyte addition if used,
and contamination notes.

Preferred hardware class:

clean sample container,
pH meter or pH strips,
conductivity or TDS meter,
thermometer,
measuring container,
label tape or sample labels,
notebook or digital run form.

Acceptance requirement:

A run cannot proceed to a valid claim if the water record is missing.

Subsystem 2: Baseline Electrolysis Reference

Purpose:

Provide a conservative known-reference hydrogen-generation path.

Required records:

cell type,
electrode/material note if known,
electrolyte if any,
voltage,
current,
duration,
observed gas behavior,
and post-run condition.

Restrictions:

no pressure storage,
no sealed accumulation,
no open flame,
no high-current push for output,
no advanced branch connected,
no performance claim without gas and energy evidence.

Acceptance requirement:

The baseline path must be run successfully before Gankyil-A or any assist branch is tested.

Subsystem 3: Baseline Gas-Liquid Separation Path

Purpose:

Provide the A-side comparison for the Gankyil-A path.

The baseline path should be a simple, visible, non-pressurized path that allows gas to separate from liquid without intentional vortex geometry.

Required observations:

liquid carryover,
visible bubble behavior,
sensor wetting,
condensate behavior,
stability of gas path,
clogging or restriction,
and cleaning burden.

Acceptance requirement:

The baseline path must be documented well enough to compare against Gankyil-A.

Subsystem 4: Gankyil-A Phase-Management Chamber

Purpose:

Test whether a geometry-guided phase-management path improves practical gas-liquid handling compared with the baseline path.

Allowed claims:

reduced liquid carryover if measured or clearly observed,
improved gas path stability if measured or clearly observed,
reduced sensor wetting if measured or clearly observed,
improved repeatability if repeat runs support it.

Forbidden claims:

improved hydrogen output without production measurement,
improved efficiency without full energy accounting,
exotic vortex energy behavior,
or any claim based on visual swirl alone.

Acceptance requirement:

Gankyil-A must be removable and testable as a B-side comparison.

Subsystem 5: Gas Verification

Purpose:

Prevent false hydrogen claims.

Minimum evidence:

hydrogen detection method,
hydrogen sensor or detector record,
calibration or bump-test note if available,
gas path description,
leak-check result,
humidity or wetting concern,
and whether the result is direct, inferred, or qualitative.

Preferred evidence:

hydrogen concentration,
gas volume or flow estimate,
gas temperature,
gas humidity note,
oxygen-side reading,
uncertainty note,
and repeat-run comparison.

Acceptance requirement:

Visible bubbles alone are not hydrogen proof.

Subsystem 6: Electrical Input Measurement

Purpose:

Prevent unsupported energy claims.

Minimum evidence:

supply type,
voltage,
current,
duration,
estimated watt-hours,
instrument used,
and whether power was stable.

Preferred evidence:

logged voltage/current over time,
power meter export,
battery state if used,
solar input state if used,
and uncertainty note.

Acceptance requirement:

No efficiency claim can be made without electrical input data.

Subsystem 7: Renewable Traceability

Purpose:

Prevent unsupported green-hydrogen claims.

Minimum evidence:

source type: grid, battery, solar, or mixed,
whether battery charging source is known,
whether solar was direct or indirect,
estimated renewable fraction,
and carbon-accounting note.

Acceptance requirement:

Hydrogen is not green by default. The energy source must be traceable.

Subsystem 8: Safety Gate

Purpose:

Block unsafe or under-specified runs.

Required preflight checks:

ventilation present,
no pressure storage,
no sealed accumulation,
no ignition sources,
emergency stop present,
leak check planned,
water/electric separation checked,
sensors connected,
branch selection reviewed,
run duration bounded,
and operator present.

Automatic denial conditions:

missing ventilation,
missing emergency stop,
pressure storage requested,
plasma branch requested,
unknown gas path,
unreviewed advanced branch,
unresolved prior anomaly,
or missing sensor plan.

Acceptance requirement:

The system must prefer blocking a run over accepting an unsafe one.

First-Build Physical Layout

The first build should be organized into four visible zones:
```
+--------------------------------------------------------------+
| Zone 1: Water / Electrolyte Prep                             |
| - water sample                                               |
| - pH / TDS / temperature                                     |
| - labels and notes                                           |
+-----------------------------+--------------------------------+
                              |
                              v
+--------------------------------------------------------------+
| Zone 2: Baseline Generation                                  |
| - conservative electrolysis reference                         |
| - measured electrical input                                  |
| - no pressure storage                                        |
+-----------------------------+--------------------------------+
                              |
                              v
+--------------------------------------------------------------+
| Zone 3: Gas-Liquid Handling                                  |
| - baseline separator path                                    |
| - removable Gankyil-A path                                   |
| - visual inspection                                          |
| - condensate observation                                     |
+-----------------------------+--------------------------------+
                              |
                              v
+--------------------------------------------------------------+
| Zone 4: Verification / Evidence                              |
| - hydrogen detection                                         |
| - oxygen-side observation                                    |
| - leak check                                                 |
| - evidence bundle                                            |
| - acceptance result                                          |
+--------------------------------------------------------------+
```
Build Constraints
Constraint 1: Non-Pressurized Only

GH-BENCH-A0 must not use pressure storage.

Allowed:

open-to-safe-vent non-pressurized gas path,
low-volume observation path,
visible gas-liquid separation,
and safe venting according to local safety requirements.

Forbidden:

compressed hydrogen storage,
sealed accumulation,
pressure vessels,
pressure-rated claims,
intentional gas storage,
or pressure testing.
Constraint 2: Baseline First

The first valid run must be baseline-only.

Order:

Baseline electrolysis reference.
Baseline separator path.
Gas verification.
Evidence bundle.
Acceptance or rejection.
Repeat baseline.
Only then compare Gankyil-A.

No advanced branch should be tested before baseline evidence exists.

Constraint 3: Gankyil-A Is an A/B Test

Gankyil-A must be tested against a simpler baseline path.

The comparison must keep these conditions as similar as practical:

water source,
water volume,
electrolyte condition,
cell configuration,
electrical input,
run duration,
sensor position,
gas path length,
ambient conditions,
and operator procedure.
Constraint 4: Solar Thermal Assist Disabled by Default

Solar thermal assist is not part of the first baseline run.

It may be added only after:

baseline run is stable,
thermal input can be measured,
temperature can be monitored,
and the acceptance logic can count both electrical and thermal energy.
Constraint 5: Plasma/Catalyst Branch Blocked by Default

Plasma/catalyst activation is not allowed in GH-BENCH-A0 baseline testing.

It requires a separate reviewed branch because it may introduce:

ignition risk,
electromagnetic interference,
reactive species,
ozone or byproducts,
sensor corruption,
thermal changes,
catalyst contamination,
and false signals.
Constraint 6: No Flame Test

No flame test is allowed as evidence.

Hydrogen verification should use appropriate detection and measurement methods, not ignition.

Constraint 7: No Unsupervised Operation

GH-BENCH-A0 is not autonomous.

A trained operator or reviewer must be present for physical testing.

Constraint 8: Failed Runs Are Preserved

A failed run is still useful.

The repo must preserve:

blocked runs,
rejected runs,
inconclusive runs,
sensor failures,
leaks,
wet sensor events,
unstable readings,
and operator concerns.

Failure is evidence.

First-Build Proof-of-Concept Goal

The first proof-of-concept goal is:
```
Demonstrate a safe, non-pressurized, baseline hydrogen detection run with measured water input, measured electrical input, documented gas path, safety preflight, evidence receipt, and acceptance decision.
```
First-Build Minimum Success Criteria

A minimum successful baseline run must include:

Completed run intent.
Completed safety preflight.
Water record.
Electrical input record.
Gas path description.
Hydrogen detection record.
Leak-check note.
Ventilation note.
Operator note.
Evidence bundle.
Acceptance result.
First-Build Stronger Success Criteria

A stronger successful baseline package includes:

Three repeat baseline runs.
Comparable water conditions.
Comparable electrical conditions.
Calibrated hydrogen detection.
Flow or volume estimate.
Oxygen-side observation.
Power log.
Carbon-accounting estimate.
Uncertainty note.
Repeatability decision.
First-Build Gankyil-A Success Criteria

Gankyil-A should be considered promising only if it shows measurable or clearly documented improvement in at least one practical phase-management metric.

Possible metrics:

less liquid carryover,
less sensor wetting,
more stable gas path,
easier condensate handling,
lower cleaning burden,
fewer blocked readings,
better repeatability of measurement,
or easier visual inspection.

Gankyil-A should not be considered successful merely because the flow looks interesting.

First-Build Rejection Criteria

A run should be rejected if:

safety preflight fails,
ventilation is missing,
leak check fails,
gas path is unknown,
sensor is wet or saturated,
hydrogen detector is not functioning,
water record is missing,
electrical input is missing,
branch configuration is unclear,
operator cannot explain the setup,
or evidence bundle is incomplete.
First-Build Stop Conditions

A run should stop if:

hydrogen accumulation is suspected,
ventilation changes,
liquid reaches the sensor,
electrical behavior becomes unstable,
unexpected heat occurs,
tubing disconnects,
odor, noise, spark, smoke, or visible damage appears,
operator loses line of sight,
data logging fails,
or any safety concern appears.
First-Build Evidence Folder

A complete run should produce a folder like:
```
run_bundles/GH-A0-YYYYMMDD-001/
  run_intent.json
  safety_preflight.json
  water_record.json
  power_record.json
  gas_record.json
  carbon_record.json
  receipt.json
  acceptance.json
  notes.md
```
First-Build Review Questions

After the first build, review:

Did the rig stay non-pressurized?
Was the gas path visible and understandable?
Was the water record complete?
Was electrical input measured?
Was hydrogen detection credible?
Was there any oxygen crossover concern?
Was there any leak or wet-sensor event?
Did the safety gate behave correctly?
Did the evidence bundle preserve the result?
Was the claim bounded correctly?
Was the run repeatable?
What blocked confidence?
First-Build Completion Definition

GH-BENCH-A0 is complete when the repo contains:

full BOM,
assembly walkthrough,
safety checklist,
baseline procedure,
Gankyil-A comparison procedure,
evidence schemas,
example run intent,
example rejected run,
smoke test,
and final README.

GH-BENCH-A0 is not complete merely because documents exist.

It becomes meaningful only when the documents make the first physical validation safer, clearer, and harder to overclaim.

