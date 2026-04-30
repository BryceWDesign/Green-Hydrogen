Layer 1: Water Verification

The water verification layer exists because hydrogen production claims are weak if the water source is unknown or uncontrolled.

The system must record:

water source,
water volume,
water temperature,
conductivity or TDS,
pH,
visible clarity,
turbidity if available,
pre-treatment if any,
electrolyte if any,
and any contamination concern.

The first build should prefer a conservative, documented water source and avoid exotic additives.

Water records are not optional. If water cannot be characterized, the run should be marked incomplete.

Layer 2: Energy Input

The energy input layer records the real inputs that make hydrogen production possible.

Minimum electrical records:

supply type,
voltage,
current,
power,
duration,
estimated watt-hours,
measurement device used,
measurement interval,
and operator notes.

Renewable traceability records:

whether the source is grid, battery, solar, or mixed,
whether solar input is direct or stored,
whether battery charging source is known,
and whether the run can honestly be called renewable-powered.

Optional thermal input records:

thermal source,
measured temperature,
thermal contact method,
thermal exposure duration,
insulation state,
and whether thermal input was stable or drifting.

A run must not be described as green hydrogen merely because hydrogen was produced. It must have energy-source traceability.

Layer 3: Baseline Electrolysis

The baseline electrolysis layer is the conservative reference path.

The first physical proof path should use baseline electrolysis before attempting any advanced assist branch.

Baseline goals:

Establish a safe known-reference run.
Confirm that hydrogen measurement works.
Confirm that the evidence bundle works.
Confirm that the safety gate catches missing requirements.
Provide a comparison point for Gankyil-A and optional assist branches.

Baseline restrictions:

no pressure storage,
no sealed gas accumulation,
no open ignition sources,
no indoor unventilated operation,
no plasma branch,
no catalyst novelty claim,
no net-positive claim,
no efficiency claim without complete measurements.
Layer 4: Phase Management

The phase-management layer handles gas-liquid behavior after generation.

This is where the Gankyil-A concept belongs.

The purpose of this layer is not to claim magical efficiency. The purpose is to test whether geometry-guided flow can improve practical separation behavior compared with a simpler baseline path.

Phase-management targets:

reduce liquid carryover,
reduce sensor wetting,
reduce bubble trapping,
stabilize gas path behavior,
improve repeatability of gas measurement,
and make separation behavior easier to inspect.

The first Gankyil-A test should be an A/B comparison:

A path: simple baseline separator or gas path.
B path: Gankyil-A phase-management chamber.

The comparison should observe:

liquid carryover,
gas path stability,
sensor stability,
visible bubble behavior,
condensate behavior,
maintenance burden,
and any safety or clogging issue.

The result is accepted only if the measurement is clear and repeatable. A visually interesting swirl is not proof of better hydrogen production.

Layer 5: Gas Verification

The gas verification layer prevents false claims.

Minimum gas evidence should include:

hydrogen detection,
hydrogen sensor model or method,
calibration record or bump-test record,
flow or volume measurement method,
oxygen-side observation,
oxygen crossover concern if applicable,
leak-check result,
gas path description,
and whether the measurement is direct, inferred, or qualitative.

Preferred evidence includes:

hydrogen concentration,
hydrogen output rate,
oxygen concentration,
gas temperature,
gas humidity condition,
total gas volume,
duration-normalized production rate,
uncertainty estimate,
and repeat run comparison.

No gas claim is valid if the measurement path is wet, uncalibrated, saturated, or physically ambiguous.

Layer 6: Safety and Shutdown

The safety layer is a hard gate.

It must be able to deny a run before the system starts.

Minimum safety checks:

ventilation present,
ignition sources excluded,
no pressure storage,
no sealed accumulation,
leak check complete,
emergency stop present,
operator present,
water/electrical separation confirmed,
sensors connected,
branch selection reviewed,
and run duration bounded.

Automatic denial conditions:

unknown gas path,
failed leak check,
missing ventilation,
missing emergency stop,
missing sensor record,
unknown branch state,
plasma branch requested without review,
pressure vessel use,
indoor unventilated operation,
or any prior unresolved anomaly.

The control system must prefer false rejection over unsafe acceptance.

Layer 7: Evidence and Receipts

The evidence layer makes the repo auditable.

Every run should produce a receipt containing:

run ID,
date,
operator,
configuration,
branch,
water record,
input energy record,
sensor record,
safety preflight result,
gas measurement record,
carbon accounting estimate,
acceptance result,
anomalies,
and claim status.

Claim status should be one of:

accepted_bounded_result
rejected
inconclusive
requires_rerun
blocked_by_safety_gate
blocked_by_missing_evidence

Evidence should be boring, structured, and repeatable.

Layer 8: Carbon Accounting

The carbon accounting layer exists because hydrogen is not automatically green.

A run can produce hydrogen and still fail the green-hydrogen claim.

Carbon accounting should record:

electrical source,
estimated energy consumed,
renewable fraction,
grid fraction if any,
battery source if known,
thermal input source,
embodied-equipment note if available,
and estimated carbon intensity.

For early bench runs, the carbon accounting result may be approximate.

Approximate does not mean fictional. If the source is unknown, mark it unknown.

Layer 9: Optional Research Branches

Optional branches must never replace the baseline path.

They are comparison paths only.

Solar Thermal Assist

Purpose:

test whether controlled heat input improves operating behavior or efficiency.

Risks:

uncontrolled temperature,
membrane degradation,
electrolyte changes,
sensor drift,
false efficiency gain if thermal input is not counted.

Gate:

allowed only after baseline is stable and thermal input can be measured.
Plasma/Catalyst Activation

Purpose:

explore whether controlled activation improves reaction behavior.

Risks:

ignition hazard,
electromagnetic interference,
ozone or reactive species,
catalyst contamination,
false signal coupling,
unsafe gas interaction,
measurement corruption.

Gate:

blocked by default.
requires formal review.
requires separate safety envelope.
requires no shared gas accumulation path.
requires explicit non-claim status.
PEC Branch

Purpose:

compare photoelectrochemical behavior as a separate research path.

Risks:

fragile materials,
low output,
degradation,
measurement ambiguity,
overclaiming solar-to-hydrogen performance.

Gate:

separate test article.
separate evidence bundle.
no blending with baseline claims.
Redox-Mediated Branch

Purpose:

explore decoupled production, buffering, or safer intermediate chemistry.

Risks:

chemical handling complexity,
storage ambiguity,
contamination,
disposal requirements,
false equivalence to direct green hydrogen.

Gate:

separate chemistry review.
separate hazard register.
separate acceptance criteria.
Data Flow

```
run_intent.json
      |
      v
safety_preflight.py
      |
      +--> denied -> receipt: blocked_by_safety_gate
      |
      v
state_machine.py
      |
      v
operator run + sensor logs
      |
      v
metrics.py + carbon_accounting.py
      |
      v
evidence_bundle.py
      |
      v
acceptance.py
      |
      v
run_bundles/<run_id>/
```

Control Philosophy

The system should operate under conservative controls:

Deny unsafe branches by default.
Require explicit evidence before accepting a claim.
Preserve raw observations even when results fail.
Treat missing data as missing data, not as success.
Make uncertainty visible.
Never convert a concept into proof without measurement.
Keep every acceptance decision reviewable.
First Physical Configuration

The first physical configuration should be:

bench-scale,
non-pressurized,
low-output,
instrumented,
ventilated,
supervised,
baseline-first,
manually inspectable,
and easy to shut down.

The first configuration should not be:

sealed,
pressurized,
autonomous,
high voltage,
high temperature,
plasma-assisted,
hidden inside opaque housings,
or operated without calibrated measurement.
Main Interfaces
Input Interfaces
water sample record,
electrical input record,
optional thermal input record,
run intent file,
operator preflight checklist,
sensor calibration record.
Output Interfaces
run receipt,
evidence bundle,
acceptance result,
carbon estimate,
anomaly log,
updated maturity note.
Acceptance Philosophy

A run should not be accepted because it looks interesting.

A run should be accepted only when the evidence supports a bounded claim.

Example accepted claim:

"The baseline bench configuration produced detectable hydrogen under measured electrical input for a short-duration non-pressurized run. The result is bounded to this configuration and requires repeat testing."

Example rejected claim:

"This system produces green hydrogen efficiently."

The second claim requires far more evidence than the first.

Architecture Success Criteria

The architecture is successful when it can:

Block unsafe run intents.
Preserve run evidence.
Separate baseline tests from advanced branches.
Prevent unsupported claims.
Compare Gankyil-A against a baseline path.
Track water, energy, gas, safety, and carbon records.
Produce reviewable acceptance decisions.
Identify what evidence is missing.
Support repeatable lab work.
Make failure useful.
Architecture Failure Criteria

The architecture fails if it:

Accepts a run with missing safety data.
Accepts a run with missing gas evidence.
Treats unknown power source as green.
Allows plasma/catalyst branch by default.
Hides failed runs.
Overwrites raw observations.
Confuses visual gas bubbles with verified hydrogen.
Claims efficiency without complete energy accounting.
Claims carbon benefit without source traceability.
Encourages physical build steps beyond the documented safety envelope.
Locked Architecture Rule

The repo must always distinguish between:

design architecture,
lab prototype plan,
measured bench result,
validated performance,
and field-ready hardware.

At the current stage, Green-Hydrogen is a design architecture and lab-validation scaffold.

It is not validated performance.
