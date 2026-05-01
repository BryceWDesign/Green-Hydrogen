# Safety Policy

## Purpose

This document defines the safety policy for Green-Hydrogen.

Green-Hydrogen is a measurement-first bench-validation scaffold for studying bounded hydrogen-production evidence.

It is not a certified hydrogen system.

This safety policy exists to prevent the repo from encouraging unsafe physical work, unsupported claims, pressure storage, ignition testing, or advanced branch activation without review.

## Core Safety Position

Hydrogen work can be hazardous.

The first Green-Hydrogen proof path must remain:

- bench-scale,
- low-output,
- non-pressurized,
- ventilated,
- supervised,
- current-limited,
- documented,
- and easy to shut down.

Any physical implementation must follow:

- applicable laws,
- local codes,
- component documentation,
- lab safety rules,
- hydrogen safety guidance,
- electrical safety practice,
- chemical handling guidance,
- and qualified review where required.

This repo does not override real-world safety requirements.

## Safety Claim Boundary

This repo may say:

```
Green-Hydrogen includes a conservative safety-gated validation architecture for a non-pressurized bench-scale proof path.
```
This repo must not say:
```
Green-Hydrogen is safe.
Green-Hydrogen is certified.
Green-Hydrogen is ready for unsupervised operation.
Green-Hydrogen is ready for field deployment.
Green-Hydrogen is ready for commercial hydrogen production.
Green-Hydrogen can be built safely without qualified review.
```

Safety is not assumed.

Safety must be earned by design review, hardware limits, procedures, testing, and evidence.

Safety Philosophy

The project follows ten safety principles:

Block before guessing.
Prefer false rejection over unsafe acceptance.
No pressure storage in the first build.
No flame tests.
No unventilated operation.
No advanced branch by default.
No missing-sensor acceptance.
No hidden gas paths.
No unsupported green-hydrogen claims.
Preserve failed and blocked runs.
Mandatory First-Build Constraints

The first build, GH-BENCH-A0, must obey these constraints:

Constraint	Requirement
Pressure	Non-pressurized only.
Storage	No intentional hydrogen storage.
Venting	Safe non-pressurized vent path required.
Supervision	Operator present at all times.
Power	Low-voltage, current-limited input only.
Ignition	No ignition sources, no flame test.
Sensors	Hydrogen-specific detection required for hydrogen claim.
Evidence	Water, power, gas, safety, and operator records required.
Branches	Baseline first; advanced branches blocked by default.
Shutdown	Emergency disconnect required and reachable.
Absolute Prohibitions

The following are not allowed in GH-BENCH-A0:

hydrogen storage tanks,
compression hardware,
pressure vessels,
sealed gas accumulation,
flame tests,
spark tests,
improvised ignition verification,
high-voltage plasma hardware,
microwave sources,
unreviewed catalysts,
mystery electrolytes,
unattended operation,
indoor unventilated operation,
open electrical wiring near water,
hidden gas routing,
blocked outlets,
and any attempt to maximize output before measurement safety is proven.
Hydrogen Hazard Boundary

Hydrogen is:

flammable,
capable of forming explosive mixtures with air,
difficult to detect without proper sensors,
prone to leakage through small paths,
sensitive to ignition sources,
and unsafe to accumulate casually.

Therefore, Green-Hydrogen requires:

ventilation,
non-pressurized operation,
no storage,
leak checking,
no ignition sources,
hydrogen-specific detection,
area awareness where practical,
and immediate shutdown on uncertainty.
Oxygen and Crossover Boundary

Electrolysis may also produce oxygen.

Oxygen-side behavior matters because abnormal separation, crossover, or trapped gas can create dangerous conditions or corrupt evidence.

The system must record:

oxygen-side observation if available,
oxygen sensor data if available,
crossover concern,
abnormal bubbling,
separation uncertainty,
and gas path integrity.

If crossover is suspected, stop the run and mark it rejected or inconclusive.

Electrical Hazard Boundary

The first rig must use low-voltage, current-limited power only.

Required controls:

current-limited DC supply,
inline fuse or overcurrent protection,
emergency disconnect,
cable strain relief,
cable labels,
dry-side power placement,
drip loops where appropriate,
water/electrical zone separation,
and post-run power-down confirmation.

Reject the setup if:

water can drip into connectors,
power shutdown requires reaching across the wet zone,
exposed mains wiring is present,
cables are unlabeled,
current limit is unknown,
fuse/protection is missing,
or electrical behavior is unstable.
Chemical and Water Boundary

Water and electrolyte records are safety and evidence records.

The first build should avoid improvised chemistry.

Use only:

documented water source,
documented electrolyte if required by selected hardware,
documented quantities,
compatible containers,
and appropriate PPE.

Do not use:

unknown additives,
undocumented catalysts,
corrosive mixtures without proper review,
contaminated water,
mystery electrolytes,
or chemicals selected only to increase apparent output.

If chemical compatibility is unknown, do not run.

Thermal Boundary

Thermal input is disabled by default for baseline testing.

Thermal assist may be introduced only after:

baseline evidence exists,
thermal input can be measured,
temperature limits are known,
selected components allow the temperature range,
sensor drift can be considered,
and safety review is complete.

Stop if:

unexpected heating occurs,
tubing softens,
plastic deforms,
condensation reaches sensors,
power draw changes unexpectedly,
smell, smoke, discoloration, or noise appears,
or operator uncertainty appears.
Gas Path Boundary

The gas path must remain:

short,
visible where practical,
non-pressurized,
leak-checked,
unblocked,
vented safely,
protected from liquid carryover,
and documented.

The gas path must not include:

pressure storage,
sealed jars,
flame ports,
hidden tubing,
unknown fittings,
blocked outlets,
or unreviewed flow restrictions.

If the operator cannot explain the gas path, the run is blocked.

Sensor Boundary

Sensors are evidence only when their limits are respected.

Hydrogen claims require hydrogen-specific detection.

Quantitative claims require:

known sensor model,
known range,
calibration or bump-test record where available,
sensor position,
wetness protection,
gas path record,
and limitation notes.

Reject or downgrade evidence if:

sensor model is unknown,
sensor is wet,
sensor is saturated,
sensor is unstable,
sensor is uncalibrated but treated as quantitative,
sensor position is undocumented,
or cross-sensitivity concerns are ignored.
Ventilation Boundary

Ventilation is mandatory for physical testing.

The repo does not define a universal ventilation design because workspace conditions vary.

The operator must confirm that the selected location is appropriate for hydrogen bench testing under applicable guidance.

A run is blocked if:

ventilation is missing,
ventilation is unknown,
vent path is obstructed,
gas can accumulate in a pocket,
vent path terminates near ignition sources,
or ventilation changes during the run.
Ignition Source Boundary

No ignition sources are allowed near the test area.

Examples of ignition concerns include:

open flame,
spark sources,
hot surfaces,
smoking materials,
arcing switches,
exposed wiring,
motors not appropriate for the environment,
static discharge risks,
and improvised test igniters.

No flame test is allowed.

A hydrogen flame or pop test is not acceptable evidence for this repo.

Advanced Branch Boundary

Advanced branches are blocked by default.

Advanced branches include:

plasma/catalyst activation,
PEC branch,
redox-mediated branch,
solar thermal assist,
high-temperature branch,
and any unreviewed catalyst or activation method.

The baseline branch must be stable first.

Advanced branches require:

separate run intent,
separate hazard review,
separate evidence bundle,
explicit approval,
no pressure storage,
no hidden energy input,
no baseline claim mixing,
and conservative stop conditions.
Plasma/Catalyst Branch Policy

Plasma/catalyst activation is considered high-risk for the first repo stage.

It may introduce:

ignition risk,
high voltage,
electromagnetic interference,
sensor corruption,
reactive species,
ozone or byproducts,
thermal instability,
catalyst contamination,
and false readings.

Therefore:
```
plasma_catalyst branch = blocked by default
```
It may not be enabled in GH-BENCH-A0 baseline testing.

PEC Branch Policy

The PEC branch is a separate research path.

It may not be mixed with baseline electrolysis evidence.

PEC work requires:

separate test article,
separate water and material record,
separate optical/solar input record,
separate degradation record,
separate gas verification,
and separate acceptance criteria.

No PEC result may be used to claim baseline performance.

Redox Branch Policy

The redox-mediated branch is a separate chemistry path.

It requires:

separate hazard review,
chemical compatibility review,
disposal plan,
storage review,
contamination control,
and separate evidence bundle.

No redox branch may be added casually to the baseline rig.

Solar Thermal Assist Policy

Solar thermal assist is optional and disabled by default.

It may only be tested after baseline stability.

A thermal-assisted run must record:

thermal source,
measured temperature,
exposure time,
contact method,
ambient conditions,
electrical input,
gas output,
and whether sensor behavior changed.

Thermal input must be counted.

Uncounted heat cannot support efficiency claims.

Safety Preflight Requirements

Before every physical run, complete safety preflight.

Minimum required fields:
```
run_id
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

Automatic Blocking Conditions

A run must be blocked if:

ventilation is missing,
emergency disconnect is missing,
pressure storage is present,
sealed gas accumulation is possible,
ignition source is present,
leak check fails,
gas path is unknown,
hydrogen sensor is missing for hydrogen claim,
water record is missing,
power record is missing,
branch is unknown,
advanced branch is requested without review,
prior anomaly is unresolved,
operator is absent,
run duration is unbounded,
or evidence cannot be stored.
Stop Conditions

Stop immediately if:

hydrogen accumulation is suspected,
hydrogen area alarm activates,
ventilation changes,
leak is suspected,
tubing disconnects,
gas path becomes blocked,
liquid reaches sensor,
sensor saturates or behaves unexpectedly,
unexpected heat occurs,
power behavior changes unexpectedly,
sparking, smoke, odor, discoloration, or noise appears,
electrolyte spills,
operator loses line of sight,
evidence logging fails,
or any operator safety concern appears.

The operator does not need permission to stop.

Post-Run Safety Requirements

After every run:

Power down.
Confirm power is off.
Maintain ventilation as needed.
Do not seal gas path prematurely.
Record final sensor state.
Inspect tubing and fittings.
Inspect liquid trap.
Inspect sensor wetness.
Inspect electrical connections.
Record anomalies.
Mark questionable parts.
Preserve evidence.

A run is not complete until post-run inspection is complete.

Failed Run Policy

Failed runs must be preserved.

A failed run can reveal:

unsafe layout,
bad evidence design,
wet sensor risk,
gas path ambiguity,
power measurement failure,
water record gaps,
carbon accounting gaps,
and unrealistic assumptions.

Do not delete failed runs.

Do not rewrite failed runs as success.

Evidence Integrity Policy

Evidence must be honest.

Required behavior:

mark unknown values as unknown,
preserve missing fields,
record sensor limitations,
preserve blocked runs,
preserve rejected runs,
preserve inconclusive runs,
record operator uncertainty,
and keep claim status conservative.

Forbidden behavior:

filling missing evidence from memory,
treating unknown as zero,
treating visual bubbles as hydrogen proof,
treating uncalibrated data as quantitative,
deleting failed data,
changing run IDs after the fact,
or promoting a result beyond its evidence level.
Claim Safety Policy

Claims must match evidence.

Allowed claim states:
```
blocked_by_safety_gate
blocked_by_missing_evidence
rejected
inconclusive
requires_rerun
accepted_bounded_result
accepted_bounded_phase_management_improvement
```
Forbidden claim jumps:
```
visual bubbles -> hydrogen proven
hydrogen detected -> green hydrogen proven
solar nearby -> renewable-powered proven
uncalibrated sensor -> concentration proven
single run -> repeatability proven
Gankyil visual swirl -> improved production proven
thermal input ignored -> efficiency improved
```
Personal Protective Equipment

Minimum PPE for physical bench testing:

eye protection,
gloves compatible with selected water/electrolyte,
appropriate clothing or lab coat/apron,
and spill-response materials.

PPE does not make an unsafe setup safe.

PPE is the last layer, not the first layer.

Workspace Requirements

A physical test workspace should have:

ventilation,
stable bench,
no ignition sources,
emergency access,
dry-side electronics area,
spill control,
clear labels,
lighting,
operator line of sight,
and enough space to stop without knocking parts over.

Do not run in a cramped or improvised space.

Maintenance Blockers

A run is blocked if any of these are unresolved:

damaged tubing,
cracked chamber,
leaking fitting,
wet sensor,
expired or unknown sensor state,
missing power protection,
missing emergency disconnect,
contaminated water path,
unknown electrolyte,
unstable mount,
prior anomaly not reviewed,
or evidence folder missing.
Review Required Before Physical Build

Before physical testing, review:

Selected electrolysis module documentation.
Hydrogen detector documentation.
Gas path compatibility.
Ventilation approach.
Electrical protection.
Emergency disconnect.
Water/electrolyte chemistry.
Leak-check method.
Sensor calibration state.
Evidence forms.
Stop conditions.
Local rules and safety requirements.
Safety Acceptance Criteria

The safety plan is acceptable when:

unsafe runs are blocked,
missing evidence is visible,
pressure storage is excluded,
ignition testing is excluded,
gas path is non-pressurized,
ventilation is required,
emergency shutdown is required,
advanced branches are blocked by default,
failed runs are preserved,
and claims are bounded to evidence.
Safety Failure Criteria

The safety plan fails if it allows:

pressure storage,
sealed accumulation,
flame tests,
unventilated operation,
unattended operation,
undocumented gas paths,
missing sensors,
missing shutdown,
missing evidence,
advanced branch activation without review,
or inflated claims.
Safety Maturity Status

Current safety/control maturity estimate:
```
88-93%
```
Meaning:

The safety architecture is strong as a control design, but it still needs exact hardware limits, exact sensor thresholds, exact ventilation review, and exact emergency shutdown hardware before physical proof work.

What Raises Safety Maturity

Safety maturity improves when the repo locks:

exact hydrogen detector,
exact area monitor,
exact ventilation method,
exact emergency disconnect,
exact current limit,
exact fuse/protection rating,
exact sensor calibration process,
exact leak-check process,
exact stop thresholds,
and exact post-run inspection forms.
Final Safety Rule

The safest run is the one the system is willing to block.

Green-Hydrogen should never reward bravery over evidence.

If the setup is unclear, unsafe, unmeasured, or hard to explain, do not run it.
