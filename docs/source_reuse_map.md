# Source Reuse Map

## Purpose

This document records which prior project ideas were repurposed into Green-Hydrogen and how they are allowed to influence the repo.

This is not a code-copy record.

This is a design-pattern reuse map. The purpose is to preserve useful architecture logic without copying proprietary work, making unsupported claims, or importing unrelated claims from other projects.

## Reuse Rules

Green-Hydrogen may reuse:

- original design patterns,
- original documentation structure,
- original validation logic,
- original safety-gating concepts,
- original evidence-bundle patterns,
- original failure-mode discipline,
- original measurement-first framing,
- and original repo organization methods.

Green-Hydrogen must not reuse:

- proprietary third-party designs,
- copyrighted diagrams,
- copied vendor manuals,
- unverified performance claims,
- defense-sensitive implementation details,
- unsafe build instructions,
- antigravity claims,
- free-energy claims,
- miracle-efficiency claims,
- or any material that would imply certification or validation that does not exist.

## Summary Table

| Source / Donor Concept | Reused In Green-Hydrogen | Allowed Role | Forbidden Role |
|---|---|---|---|
| IX-Liquid | Water verification and source discipline | Water quality, water traceability, pre-run records | Claiming water treatment performance without measurement |
| IX-Marine-H2-Retrofit | Hydrogen process spine and safety framing | Hydrogen handling awareness, energy traceability, retrofit caution | Marine deployment claim or field-ready claim |
| STAG-style solar thermal logic | Solar thermal assist branch | Measured heat input and thermal accounting | Free heat, uncounted efficiency gain, or net-positive claim |
| Gankyil vortex phase concept | Gas-liquid phase management | Passive separation comparison and demisting behavior | Claiming output increase without A/B evidence |
| IX-Breath | Byproduct, reserve, and resource-gating logic | O2-side caution, bounded state transitions, deny logic | Life-support claim or oxygen reserve claim |
| IX-BlackFox | Governed runtime and evidence-control pattern | Policy gates, receipts, acceptance validation, reviewable decisions | Autonomous unsafe operation |
| IX-Style | Runtime assurance and FDIR-like discipline | Sensor trust, fault response, anomaly handling | Aerospace certification claim |
| OpenCryoCore | Thermal sensing and condenser awareness | Temperature tracking, thermal drift caution, condensation awareness | Cryogenic system claim |
| Superheavy-Survival-Audit | Evidence discipline and negative-control logic | Audit packs, route constraints, kill criteria, information gain | Nuclear claim transfer or unrelated physics claim |
| IX-Legacy | Energy truth protocol and tri-core routing concepts | Energy accounting, conservative routing, thermal guardian ideas | Overclaiming hidden energy recovery |
| IX-MPMT | Null tests, lock-in validation, artifact rejection | Negative controls, EMI artifact caution, sensor-skin thinking | Claiming exotic effects without isolation |
| IX-Shimizu | Water/oil separation and marine intake discipline | Turbidity, flow, calibration, contamination caution | Marine flood/water treatment claim |
| IX-Sustainment-OS | Maintenance blockers and approval logic | Maintenance gates, evidence events, blocked states | Operational deployment claim |
| IX-ZeroCell | MPPT, supercap, fuse/protection, low-power monitoring | Power continuity, electrical protection, data logging | Claiming novel power generation |
| IX-Thaed / IX-Vibe | Vibration, damping, FRF/SRS discipline | Mechanical stability and sensor mounting caution | Structural validation claim |
| IX-AntiGrav | Plasma/vortex/tri-spin interlock salvage only | Branch isolation and interlock caution | Antigravity, propulsion, or exotic-force claims |

## Donor Concept: IX-Liquid

### Useful Reuse

IX-Liquid contributes the idea that the input fluid must be treated as evidence.

For Green-Hydrogen, this means every run should record:

- source of water,
- date collected or prepared,
- water volume,
- temperature,
- pH,
- conductivity or TDS,
- turbidity or clarity,
- electrolyte addition, if any,
- filtration or pre-treatment, if any,
- and contamination concerns.

### Why It Matters

Hydrogen output cannot be interpreted cleanly if the water source is unknown.

Unknown water can introduce:

- contamination,
- sensor drift,
- conductivity changes,
- catalyst poisoning,
- electrode fouling,
- unexpected gas byproducts,
- and false repeatability.

### Boundary

IX-Liquid does not prove Green-Hydrogen works.

It only contributes the discipline that water must be characterized before production claims are made.

## Donor Concept: IX-Marine-H2-Retrofit

### Useful Reuse

IX-Marine-H2-Retrofit contributes hydrogen-system caution:

- hydrogen must be treated as a safety-critical gas,
- energy source must be traceable,
- retrofit thinking requires strict boundaries,
- gas handling must avoid casual accumulation,
- and practical systems require inspection and shutdown paths.

### Reused Pattern

Green-Hydrogen reuses this as a process spine:

```
water record
  -> energy input
  -> hydrogen generation attempt
  -> gas separation
  -> gas verification
  -> safety record
  -> evidence bundle
  -> bounded claim decision
```
Boundary

Green-Hydrogen does not inherit any marine deployment claim.

The current repo is a bench-validation scaffold only.

Donor Concept: STAG-Style Solar Thermal Logic
Useful Reuse

STAG-style thinking contributes the idea that thermal input can be useful only if it is measured.

Solar heat cannot be treated as free improvement unless it is counted.

For Green-Hydrogen, thermal input records should include:

thermal source,
collection method,
temperature,
exposure time,
contact method,
insulation state,
thermal losses if known,
and whether the thermal input affected sensor readings.
Boundary

Solar thermal assist must not be claimed to improve efficiency unless total energy accounting includes both electrical and thermal contributions.

Donor Concept: Gankyil Vortex Phase Management
Useful Reuse

The Gankyil concept is reused as a bounded phase-management idea.

Allowed role:

gas-liquid separation,
bubble path organization,
demisting,
condensate behavior control,
sensor wetting reduction,
and A/B comparison against a simple baseline separator.

Forbidden role:

claiming higher hydrogen yield without measurement,
claiming exotic energy behavior,
claiming vortex-driven production,
or claiming performance from visual swirl alone.
Required Test

Gankyil-A must be tested as an A/B comparison:
```
Baseline separator path
versus
Gankyil-A phase-management path
```
Comparison fields:

liquid carryover,
gas path stability,
hydrogen sensor stability,
visible bubble behavior,
condensate behavior,
clogging,
cleaning burden,
and repeatability.
Donor Concept: IX-Breath
Useful Reuse

IX-Breath contributes resource-gated safety logic.

The useful lesson is that production systems fail through coupled limits, not one resource alone.

For Green-Hydrogen, this becomes:

oxygen-side byproduct awareness,
bounded regeneration/production logic,
protected safety/control bus thinking,
deny-by-default transitions,
and no-credit-without-proof validation.
Example Translation

IX-Breath concept:
```
Do not assume oxygen margin just because oxygen exists.
```
Green-Hydrogen translation:
```
Do not assume safe hydrogen production just because bubbles exist.
```
Boundary

Green-Hydrogen does not make life-support claims.

IX-Breath is used only for safety logic, byproduct caution, and state discipline.

Donor Concept: IX-BlackFox
Useful Reuse

IX-BlackFox contributes governed engineering workflow:

policy gates,
workspace boundaries,
allowlisted tests,
parsed evidence,
receipts,
bundles,
acceptance validation,
and human review.

For Green-Hydrogen, this becomes:
```
run intent
  -> safety preflight
  -> allowed / denied
  -> evidence capture
  -> acceptance validation
  -> claim boundary
```
Why It Matters

Hydrogen work is dangerous if the system accepts vague intent.

The control plane must deny unsafe or under-specified runs.

Boundary

Green-Hydrogen does not need autonomous patching or repo-repair intelligence.

Only the governance and evidence concepts are reused.

Donor Concept: IX-Style
Useful Reuse

IX-Style contributes runtime assurance logic:

sensor trust scoring,
fault detection,
isolation,
recovery,
anomaly labeling,
and evidence-bundle discipline.

For Green-Hydrogen, this supports:

rejecting wet sensor data,
rejecting saturated sensor data,
rejecting missing calibration,
preserving anomalies,
and separating measurement failure from production failure.
Boundary

No aerospace certification claim is transferred.

This is only a software and validation discipline pattern.

Donor Concept: OpenCryoCore
Useful Reuse

OpenCryoCore contributes thermal-awareness patterns:

temperature drift matters,
condensation matters,
thermal memory can corrupt interpretation,
cooling/heating paths need records,
and sensors can be fooled by thermal transients.

For Green-Hydrogen, this matters because gas verification can be affected by:

humidity,
condensation,
temperature-dependent sensor behavior,
electrolyte temperature,
tubing temperature,
and chamber wall temperature.
Boundary

Green-Hydrogen does not become a cryogenic project.

Only thermal-sensing caution and condenser awareness are reused.

Donor Concept: Superheavy-Survival-Audit
Useful Reuse

Superheavy-Survival-Audit contributes extreme evidence discipline.

Useful patterns:

provenance tracking,
negative controls,
kill criteria,
route constraints,
information gain,
ambiguity scoring,
and audit packs.

For Green-Hydrogen, this becomes:

preserve failed runs,
reject missing evidence,
record why a claim failed,
require comparison runs,
and mark uncertainty clearly.
Boundary

No nuclear-science claim transfers into Green-Hydrogen.

The reuse is methodological only.

Donor Concept: IX-Legacy
Useful Reuse

IX-Legacy contributes energy-truth discipline.

Useful patterns:

measured input before output claims,
routing energy through defined states,
thermal guardian thinking,
low-loss caution,
and no hidden-credit accounting.

For Green-Hydrogen, this becomes:

no efficiency claim without complete input accounting,
no green claim without source traceability,
no thermal benefit unless thermal input is counted,
and no output claim without gas verification.
Boundary

No over-unity, free-energy, or hidden-energy claim is allowed.

Donor Concept: IX-MPMT
Useful Reuse

IX-MPMT contributes measurement artifact discipline.

Useful patterns:

null tests,
coded-phase thinking,
lock-in validation attitude,
EMI caution,
thermal artifact rejection,
and sensor-skin awareness.

For Green-Hydrogen, this supports:

plasma branch isolation,
sensor interference checks,
blank controls,
wet/dry sensor comparison,
and rejection of unstable readings.
Boundary

No exotic-effect claim transfers into Green-Hydrogen.

The reuse is limited to artifact control.

Donor Concept: IX-Shimizu
Useful Reuse

IX-Shimizu contributes water-handling caution:

intake discipline,
turbidity awareness,
flow awareness,
sensor calibration,
contamination paths,
and separation behavior.

For Green-Hydrogen, this supports:

water verification,
electrolyte clarity records,
tubing inspection,
gas-liquid separation observation,
and post-run contamination checks.
Boundary

Green-Hydrogen does not claim flood, marine, or oil-water treatment capability.

Donor Concept: IX-Sustainment-OS
Useful Reuse

IX-Sustainment-OS contributes maintenance and approval logic.

For Green-Hydrogen, this becomes:

do not run if maintenance is unresolved,
do not run if sensors are expired,
do not run if calibration is missing,
do not run if tubing is degraded,
do not run if prior anomaly is unresolved,
and record maintenance blockers as evidence.
Boundary

This is not operational deployment management.

It is bench validation discipline.

Donor Concept: IX-ZeroCell
Useful Reuse

IX-ZeroCell contributes small-power-system discipline:

MPPT awareness,
battery traceability,
supercapacitor buffering caution,
fuse/protection thinking,
low-power monitoring,
and brownout behavior.

For Green-Hydrogen, this supports:

power logging,
protection hardware,
low-voltage sensor bus,
data logger continuity,
and source-traceable renewable runs.
Boundary

IX-ZeroCell does not prove Green-Hydrogen can generate net-positive energy.

It only contributes power-management discipline.

Donor Concept: IX-Thaed / IX-Vibe
Useful Reuse

IX-Thaed and IX-Vibe contribute mechanical test discipline:

vibration can affect sensors,
mounting can corrupt measurements,
tubing movement can affect gas readings,
mechanical resonance can cause repeatability problems,
and sensor placement must be stable.

For Green-Hydrogen, this supports:

stable bench mounting,
strain relief,
vibration isolation,
consistent sensor placement,
and repeatable Gankyil-A comparison.
Boundary

Green-Hydrogen does not claim structural-health-monitoring validation.

Only mechanical stability discipline is reused.

Donor Concept: IX-AntiGrav
Useful Reuse

IX-AntiGrav is not reused for antigravity claims.

The only salvageable ideas are:

branch isolation,
interlock caution,
plasma hazard separation,
vortex-geometry skepticism,
and strict rejection of exotic claims without evidence.
Explicit Rejection

Green-Hydrogen rejects:

antigravity claims,
propellantless propulsion claims,
exotic-force claims,
free-energy claims,
and vortex-as-proof reasoning.
Allowed Translation

IX-AntiGrav may only influence this repo in the following way:
```
If a concept sounds exotic, isolate it, gate it, test it separately, and refuse to claim it until measured.
```

Integration Map
```
IX-Liquid
  -> water verification records

IX-Marine-H2-Retrofit
  -> hydrogen process caution

STAG-style solar thermal logic
  -> measured thermal assist branch

Gankyil vortex phase concept
  -> passive phase-management A/B test

IX-Breath
  -> byproduct and safety-state discipline

IX-BlackFox
  -> policy gates, receipts, evidence bundles

IX-Style
  -> sensor trust and anomaly handling

OpenCryoCore
  -> thermal drift and condensation caution

Superheavy-Survival-Audit
  -> negative controls, kill criteria, audit packs

IX-Legacy
  -> energy truth protocol

IX-MPMT
  -> artifact rejection and null tests

IX-Shimizu
  -> water handling and calibration discipline

IX-Sustainment-OS
  -> maintenance blockers and approval gates

IX-ZeroCell
  -> power protection and monitoring bus

IX-Thaed / IX-Vibe
  -> mechanical stability and sensor mounting

IX-AntiGrav
  -> exotic-claim rejection and branch isolation only
  ```
Reuse Priority

The most valuable donor patterns are ranked as follows:

IX-BlackFox governance and evidence receipts.
IX-Breath conservative state transitions.
IX-Liquid water verification.
Gankyil-A phase-management A/B test.
IX-Marine-H2 hydrogen caution.
STAG measured thermal assist.
Superheavy-Survival-Audit negative controls.
IX-MPMT artifact rejection.
IX-ZeroCell power traceability.
IX-Sustainment-OS maintenance blockers.
What This Map Protects Against

This map protects the repo from five failure modes:

Claim inflation.
Unsafe branch mixing.
Hidden borrowed assumptions.
Unsupported novelty claims.
Loss of provenance from the prior design work.
Claim Transfer Rule

No claim transfers automatically from any donor project into Green-Hydrogen.

Every Green-Hydrogen claim must be independently earned by Green-Hydrogen evidence.

Current Allowed Claim

The repo may claim:

Green-Hydrogen reuses original validation, safety, evidence, water-verification, energy-accounting, and phase-management patterns from prior project work to structure a bounded green-hydrogen bench-validation scaffold.

Current Forbidden Claim

The repo must not claim:

Prior projects prove that Green-Hydrogen can produce efficient, safe, scalable, or verified green hydrogen.

They do not.

Final Rule

Reuse architecture.

Do not reuse certainty.
