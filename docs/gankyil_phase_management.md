# Gankyil Phase Management

## Purpose

This document defines the Green-Hydrogen Gankyil phase-management concept.

The Gankyil concept is used here as a passive gas-liquid handling architecture.

It is not treated as proof of increased hydrogen production.

It is not treated as proof of improved electrolysis efficiency.

It is not treated as an exotic energy mechanism.

Its only allowed role in this repo is to test whether geometry-guided flow can improve practical phase-management behavior in a non-pressurized bench setup.

## Core Claim Boundary

Allowed claim:

```
Gankyil-A is a passive phase-management test article for comparing gas-liquid handling behavior against a simpler baseline separator path.
```
Forbidden claims:
```
Gankyil-A increases hydrogen production.
Gankyil-A improves electrolysis efficiency.
Gankyil-A creates energy.
Gankyil-A proves vortex-enhanced hydrogen generation.
Gankyil-A proves green hydrogen.
Gankyil-A is validated for scale-up.
```
Why Phase Management Matters

Hydrogen bench tests can be corrupted by poor gas-liquid handling.

Common issues include:

droplets entering the gas verification path,
sensor wetting,
gas bubbles collecting inconsistently,
liquid slugs moving through tubing,
inconsistent vent behavior,
condensate confusing flow readings,
unstable detector readings,
backflow,
and unclear separation behavior.

If gas-liquid behavior is messy, the project may falsely interpret a sensor artifact as hydrogen evidence or may reject useful data because the gas path is unstable.

The Gankyil layer exists to make this part of the system more observable and repeatable.

Gankyil-A Definition

Gankyil-A is the first passive phase-management prototype.

It is:

removable,
inspectable,
non-pressurized,
passive,
gas-path-limited,
and designed for A/B comparison.

It is not:

a reactor,
a pressure chamber,
a hydrogen storage device,
a performance booster,
or an advanced branch.
System Position

Gankyil-A belongs downstream of baseline generation and upstream of gas verification.
```
baseline electrolysis reference
  -> upstream gas-liquid output
  -> baseline separator OR Gankyil-A
  -> liquid carryover protection
  -> hydrogen verification point
  -> safe non-pressurized vent path
```
The Gankyil chamber must not be placed where it can trap pressure or hide a gas accumulation hazard.

Conceptual Flow Regions

Gankyil-A has three conceptual regions.

Region 1: Inlet Conditioning Region

Purpose:

receive wet gas or gas-liquid mixture,
reduce direct droplet carryover,
introduce flow into the chamber in a controlled direction,
avoid sudden impingement into the outlet,
and make incoming behavior visible.

Important constraints:

inlet must be labeled,
inlet must not be hidden,
inlet must not create high backpressure,
inlet must not require high flow to function,
and inlet must be easy to leak-check.
Region 2: Guided Separation Region

Purpose:

encourage liquid to separate from gas,
slow chaotic droplet carryover,
create an inspectable flow path,
allow visual comparison against baseline separator,
and prevent direct liquid shot into the gas sensor.

Important constraints:

guide features must be removable or cleanable,
guide features must not block the outlet,
guide features must not shed particles,
guide features must not create sealed pockets,
and guide features must not be treated as proof by visual swirl.
Region 3: Demist / Outlet Region

Purpose:

allow gas to leave toward verification,
reduce liquid carryover to downstream sensors,
preserve non-pressurized venting,
and keep the gas path stable.

Important constraints:

outlet must be labeled,
outlet must remain unblocked,
outlet must not force gas through a restrictive path,
outlet must not connect to storage,
and outlet must be inspected before each run.

Conceptual Layout
```
+------------------------------------------------------+
|                                                      |
|   Inlet Conditioning                                 |
|       |                                              |
|       v                                              |
|   +---------------------------+                      |
|   | Guided Separation Region  |                      |
|   | - visible flow path       |                      |
|   | - removable guide insert  |                      |
|   | - liquid separation zone  |                      |
|   +---------------------------+                      |
|       |                                              |
|       v                                              |
|   Lower Liquid Collection / Observation Region       |
|                                                      |
|   Upper Gas Exit / Demist Region                     |
|       |                                              |
|       v                                              |
|   To hydrogen verification path                      |
|                                                      |
+------------------------------------------------------+
```
Geometry Discipline

The first Gankyil geometry should be simple enough to inspect.

Do not optimize geometry before proving that the baseline comparison can be repeated.

The first geometry should prioritize:

visibility,
non-pressurized operation,
cleanability,
short gas path,
stable mounting,
repeatable orientation,
sensor protection,
leak-check simplicity,
easy bypass,
and conservative evidence.
Supplier-Neutral Geometry Requirements

The exact dimensions are not locked in this repo because the first physical design must match selected tubing, selected electrolysis reference hardware, selected chamber material, and selected gas verification method.

The first geometry should follow supplier-neutral constraints:

Feature	Requirement
Chamber body	Transparent or inspectable.
Operation	Non-pressurized only.
Inlet	Clearly labeled and leak-checked.
Outlet	Clearly labeled and unblocked.
Internal geometry	Removable or cleanable.
Liquid region	Visible or inspectable.
Mounting	Repeatable orientation.
Bypass	Baseline path can be restored easily.
Sensor protection	Liquid carryover reduced before hydrogen detector.
Venting	No storage, no compression, no sealed accumulation.
First Geometry Recommendation

The first Gankyil-A geometry should use:

one visible chamber body,
one clearly marked inlet,
one clearly marked outlet,
one lower liquid-observation area,
one removable internal guide feature if used,
one stable vertical or near-vertical mount,
one bypassable downstream path,
and one downstream liquid protection stage before the hydrogen sensor.

The first version should avoid:

tiny passages,
complex internal channels,
sealed layers,
hidden cavities,
fixed non-cleanable inserts,
fragile parts,
unclear inlet/outlet routing,
and any geometry that creates restriction.
Orientation Rule

Default first orientation:

```
orientation = vertical
```
orientation = vertical
```
orientation
orientation_angle_degrees
inlet_position
outlet_position
liquid_collection_position
guide_insert_present
guide_insert_description
```
If the orientation changes between runs, the comparison must record that change.

Do not compare two runs as equivalent if the chamber orientation changed without documentation.

Inlet Constraints

The inlet should:

be labeled,
enter the chamber in a repeatable position,
avoid pointing directly at the outlet,
avoid splashing liquid toward the sensor,
be short and visible,
and be easy to inspect for leaks.

The inlet should not:

be hidden behind the chamber,
rely on pressure,
include unknown adapters,
collect liquid in an undocumented low point,
or kink the tubing.
Outlet Constraints

The outlet should:

be labeled,
remain unblocked,
lead toward liquid protection and sensor verification,
avoid trapping condensate,
avoid sharp bends,
and remain easy to disconnect after shutdown.

The outlet should not:

connect to storage,
connect to a sealed container,
connect to a flame-test port,
connect to a restrictive device without review,
or be capped during operation.
Internal Guide Constraints

If internal guide features are used, they should be:

removable,
cleanable,
chemically compatible,
mechanically stable,
non-shedding,
and visible or inspectable.

They should not:

block the outlet,
require pressure,
shed particles,
hide liquid,
create sealed pockets,
create hard-to-clean residue traps,
or make the chamber impossible to inspect.
Liquid Collection Constraints

The liquid region should:

be visible,
be easy to inspect after shutdown,
not connect to electronics,
not require pressure to drain,
and not hide the amount of liquid collected.

If a drain exists, it must:

not create sealed accumulation,
not be manipulated during active operation unless the run is stopped and safe,
and be documented in the run record.
Sensor Protection Constraints

Gankyil-A is useful only if it improves or preserves gas verification quality.

The downstream sensor path should include:
```
Gankyil-A outlet
  -> liquid protection / demist buffer
  -> hydrogen verification point
  -> safe non-pressurized vent path
```
A Gankyil test should be rejected or marked inconclusive if liquid reaches the hydrogen sensor.

Non-Pressurization Constraints

Gankyil-A must not increase system pressure.

Required confirmations before each Gankyil run:
```
no_pressure_storage = true
no_sealed_accumulation = true
outlet_unblocked = true
vent_path_defined = true
gas_path_visible = true
restriction_concern = false
```
If restriction is suspected, stop the run.

A/B Comparison Requirement

Gankyil-A cannot claim improvement without a baseline comparison.

Required comparison:
```
A-side = baseline separator path
B-side = Gankyil-A phase-management path
```
Conditions should remain as close as practical:

same water source,
same water volume,
same electrolyte state,
same electrolysis reference module,
same voltage/current range,
same run duration,
same sensor position,
same vent path class,
same operator procedure,
and same evidence forms.

Any difference must be recorded.

Comparison Metrics

Gankyil-A should be compared on practical phase-management metrics.

Metric	What To Observe
Liquid carryover	Did less liquid reach downstream path?
Sensor wetting	Did the hydrogen sensor remain dry?
Gas path stability	Were readings more stable?
Condensate behavior	Was liquid easier to observe or isolate?
Bubble behavior	Was gas-liquid motion more consistent?
Restriction concern	Did the chamber cause backpressure or blockage?
Leak behavior	Did added fittings increase leak risk?
Cleaning burden	Was cleanup easier or harder?
Setup complexity	Did it add too much complexity?
Repeatability	Did results repeat under comparable conditions?
Evidence Record

A Gankyil run should record:
```
run_id
comparison_id
separator_type
gankyil_variant_id
baseline_run_reference
orientation
inlet_position
outlet_position
guide_insert_present
guide_insert_description
liquid_protection_present
leak_check_result
vent_path_defined
water_source
voltage_v
current_a
duration_s
hydrogen_sensor_model
sensor_wetness_observed
liquid_carryover_observed
gas_path_stability
restriction_concern
operator_notes
acceptance_status
```
Gankyil Variant Naming

Use this naming pattern:

GANKYIL-A0 = first documented concept
GANKYIL-A1 = first revised geometry
GANKYIL-A2 = second revised geometry
GANKYIL-A3 = third revised geometry
```
Do not overwrite prior variants.

Each variant should preserve:
```
Geometry Change Rules

A geometry change is allowed when it targets a specific observed issue.

Good reasons to revise geometry:

outlet wetting occurred,
liquid collection was not visible,
chamber restricted flow,
guide insert shifted,
cleaning was poor,
bubble behavior was too chaotic,
sensor readings were unstable,
or comparison was hard to repeat.

Bad reasons to revise geometry:

it looked less impressive than expected,
visual swirl was not dramatic,
output claim was desired,
or the test failed and the evidence was inconvenient.
Gankyil Acceptance Criteria

Gankyil-A may receive accepted_bounded_phase_management_improvement only if:

baseline A-side record exists,
Gankyil B-side record exists,
conditions are comparable,
leak check passed,
gas path remained non-pressurized,
sensor was not corrupted by wetness,
outlet was not restricted,
evidence shows improvement in at least one practical metric,
and claim wording is limited to phase management.
Gankyil Rejection Criteria

Reject or mark inconclusive if:

no baseline comparison exists,
Gankyil path restricts flow,
outlet is blocked,
chamber leaks,
sensor is wetted,
guide insert shifts,
gas path becomes unclear,
conditions are not comparable,
result relies only on visual swirl,
or evidence files are missing.
What Counts As Improvement

Possible improvement:
```
Less liquid carryover reached the downstream gas verification path compared with the baseline separator path.
```
Possible improvement:
```
The hydrogen sensor remained dry during the Gankyil-A run while the baseline path produced sensor-wetting risk under comparable conditions.
```
Possible improvement:
```
Gas-path observations were more stable and easier to document with Gankyil-A than with the baseline path.
```
What Does Not Count As Improvement

Not improvement by itself:
```
The swirl looked stronger.
```
Not improvement by itself:
```
The chamber looked more advanced.
```
Not improvement by itself:
```
The operator expected it to help.
```
Not improvement by itself:
```
Hydrogen output seemed higher but was not measured.
```
Integration With Gas Verification Rack

Gankyil-A should be treated as upstream conditioning, not final verification.

A correct chain is:
```
Gankyil-A
  -> liquid protection
  -> hydrogen detector / sensor
  -> safe non-pressurized vent
```
An incorrect chain is:
```
Gankyil-A
  -> sealed storage
  -> pressure accumulation
  -> flame test
```
The incorrect chain is forbidden.

Integration With Carbon Accounting

Gankyil-A does not affect carbon accounting unless a later test proves that it changes measured energy/output behavior.

At the current stage, Gankyil-A may only influence:

gas path stability,
sensor wetness,
liquid carryover,
measurement repeatability,
and setup quality.

It does not automatically improve the green-hydrogen claim.

Integration With Advanced Branches

Gankyil-A must not be used to justify advanced branches.

Do not combine first Gankyil tests with:

plasma/catalyst activation,
PEC branch,
redox branch,
high-temperature branch,
or unreviewed catalyst testing.

Gankyil-A comparison should remain baseline-only until it is characterized.

Failure Preservation

A failed Gankyil run should be preserved.

Useful failed outcomes include:

chamber leaked,
liquid reached sensor,
guide insert shifted,
restriction occurred,
no improvement observed,
comparison conditions were invalid,
or evidence was incomplete.

These failures guide the next geometry revision.

Current Maturity Position

Gankyil phase management is currently:
```
architecture concept = strong
physical geometry = not locked
measured improvement = not proven
```
Current honest claim:
```
Gankyil-A is a promising phase-management comparison concept that deserves controlled A/B testing, but it has not proven performance improvement yet.
```
What Would Raise Confidence

Confidence increases if the repo gains:

Exact Gankyil-A geometry drawing.
Exact chamber material selection.
Exact inlet/outlet dimensions matched to selected tubing.
Exact mounting orientation.
Repeatable baseline separator path.
Three A/B comparison runs.
Sensor wetness comparison.
Liquid carryover comparison.
Gas path stability comparison.
Post-run cleaning and maintenance records.
Final Rule

Gankyil-A earns credibility only by making the gas verification path cleaner, safer, or more repeatable.

It does not earn credibility by looking exotic.

It does not earn credibility by visual swirl.

It earns credibility only through controlled comparison against the baseline path.


