# Hazard Register

## Purpose

This hazard register identifies known and foreseeable hazards for the Green-Hydrogen `GH-BENCH-A0` validation rig.

The purpose is to keep risk visible before physical testing.

This document is not a certification, safety approval, or substitute for qualified review.

## Scope

This hazard register covers:

- baseline electrolysis reference testing,
- non-pressurized gas handling,
- Gankyil-A phase-management testing,
- gas verification,
- water/electrolyte handling,
- electrical input,
- optional solar and thermal assist planning,
- evidence capture,
- and claim-control hazards.

This register does not approve:

- pressure storage,
- compression,
- flame testing,
- high-voltage plasma,
- unreviewed catalysts,
- unattended operation,
- field deployment,
- or commercial hydrogen production.

## Hazard Severity Scale

| Severity | Meaning |
|---:|---|
| 1 | Minor nuisance or documentation issue. |
| 2 | Minor equipment issue or weak evidence problem. |
| 3 | Moderate safety concern, failed run, or damaged component. |
| 4 | Serious hazard requiring immediate stop and review. |
| 5 | Severe hazard with potential for fire, explosion, injury, or major damage. |

## Hazard Likelihood Scale

| Likelihood | Meaning |
|---:|---|
| 1 | Unlikely under normal controlled use. |
| 2 | Possible if procedure is weak. |
| 3 | Plausible during early prototype testing. |
| 4 | Likely if uncontrolled or improvised. |
| 5 | Expected if safety rules are ignored. |

## Risk Score

```
risk_score = severity * likelihood
```

Suggested interpretation:

Risk Score	Interpretation
1-4	Low, monitor.
5-9	Moderate, control required.
10-15	High, strong control required.
16-25	Critical, block until redesigned or reviewed.
Register Summary
ID	Hazard	Severity	Likelihood	Risk	Required Control
H-001	Hydrogen accumulation	5	3	15	Ventilation, no storage, leak check, area awareness.
H-002	Ignition source near gas path	5	2	10	No ignition sources, no flame tests, workspace control.
H-003	Pressure buildup	5	2	10	Non-pressurized path, unblocked vent, no storage.
H-004	Wet hydrogen sensor	3	3	9	Liquid trap, demister, sensor position control.
H-005	False hydrogen claim from bubbles	2	4	8	Hydrogen-specific detection required.
H-006	Electrical short near water	4	3	12	Dry-side power, current limit, fuse, drip control.
H-007	Missing emergency disconnect	5	2	10	Required preflight field.
H-008	Unventilated operation	5	2	10	Ventilation required, run blocked if unknown.
H-009	Unknown water chemistry	3	3	9	Water verification record required.
H-010	Unknown electrolyte or additive	4	2	8	Use documented chemistry only.
H-011	Oxygen crossover or abnormal separation	4	2	8	O2-side observation, stop on concern.
H-012	Sensor saturation or drift	3	3	9	Calibration record, limitation note, reject weak data.
H-013	Gas leak	5	3	15	Leak check, short tubing, visible fittings.
H-014	Tubing disconnect	4	3	12	Secure fittings, strain relief, stop condition.
H-015	Blocked vent path	5	2	10	Vent path checklist, no storage.
H-016	Thermal runaway or overheating	4	2	8	Baseline no thermal assist, monitor temperature.
H-017	Plasma branch ignition/EMI risk	5	2	10	Blocked by default.
H-018	Misleading solar-green claim	2	4	8	Energy source record and carbon accounting.
H-019	Missing power data	2	3	6	Inline power meter, power record required.
H-020	Missing evidence bundle	2	3	6	Run folder and required evidence files.
H-021	Operator distraction	4	2	8	No unattended run, stop if distracted.
H-022	Poor bench layout	3	3	9	Six-zone layout and photo record.
H-023	Gankyil-A restriction	4	2	8	Non-pressurized outlet, restriction stop condition.
H-024	Liquid carryover into downstream path	3	3	9	Trap, demist, post-run inspection.
H-025	Inflated claim after weak result	2	4	8	Acceptance states and forbidden claim rules.
H-026	Failed run deleted or rewritten	2	3	6	Preserve rejected/inconclusive evidence.
H-027	Battery source misclassified as renewable	2	3	6	Battery charge-source record.
H-028	Component compatibility unknown	4	2	8	Documentation review before physical run.
H-029	Fire extinguisher/PPE absence	4	2	8	PPE and response equipment required.
H-030	Post-run residual gas ambiguity	4	2	8	Shutdown and venting checklist.
H-001: Hydrogen Accumulation
Hazard

Hydrogen may accumulate if the gas path leaks, vents poorly, or traps gas in an enclosed volume.

Causes
poor ventilation,
blocked vent path,
hidden gas route,
leaking fittings,
sealed collection volume,
tubing disconnection,
or operator misunderstanding.
Consequences
flammable mixture,
ignition hazard,
explosion risk,
equipment damage,
injury.
Controls
no pressure storage,
no sealed accumulation,
ventilation required,
short visible gas path,
leak check required,
vent path defined,
no ignition sources,
area hydrogen awareness where practical,
immediate stop on uncertainty.
Evidence Required
```
ventilation_present
vent_path_defined
leak_check_passed
no_pressure_storage
no_sealed_accumulation
operator_notes
```
Stop Condition

Stop immediately if accumulation is suspected or the gas path becomes unclear.

H-002: Ignition Source Near Gas Path
Hazard

Hydrogen gas may ignite if it contacts a flame, spark, hot surface, or electrical ignition source.

Causes
flame test,
open flame nearby,
arcing switch,
exposed wiring,
hot surface,
smoking materials,
static discharge,
inappropriate motors or electronics near vent path.
Consequences
fire,
explosion,
burns,
equipment damage.
Controls
no flame test,
no ignition sources,
dry-side electronics,
no exposed mains wiring,
vent path away from ignition sources,
safety signage,
workspace review.
Evidence Required
```
no_ignition_sources
vent_path_away_from_ignition_sources
flame_test_absent
workspace_checked
```
Stop Condition

Stop if any ignition source appears or the vent path changes.

H-003: Pressure Buildup
Hazard

Pressure may build if gas is routed into a sealed or restricted path.

Causes
blocked outlet,
flow meter restriction,
sealed collection container,
plugged tubing,
check valve misuse,
liquid blocking a tube,
Gankyil-A restriction,
operator capping outlet.
Consequences
rupture,
fitting ejection,
leaks,
sudden gas release,
unsafe hydrogen accumulation.
Controls
non-pressurized path only,
no storage,
no sealed jars,
no compression,
unblocked outlet,
restriction check,
liquid trap inspection,
stop if pressure is suspected.
Evidence Required
```
no_pressure_storage
outlet_unblocked
vent_path_defined
flow_device_pressure_risk_reviewed
gas_path_documented
```
Stop Condition

Stop if the outlet may be blocked or pressure buildup is suspected.

H-004: Wet Hydrogen Sensor
Hazard

Liquid carryover or condensate may wet the hydrogen sensor and corrupt readings or damage the device.

Causes
gas path carries droplets,
separator ineffective,
Gankyil-A outlet sends liquid downstream,
trap omitted,
tubing angle causes liquid slug,
high humidity,
condensation.
Consequences
false readings,
sensor damage,
rejected run,
misleading hydrogen claim.
Controls
liquid trap or demist stage,
sensor wetness protection,
sensor placement record,
post-run sensor inspection,
stop on wetness,
reject wet sensor data.
Evidence Required
```
liquid_protection_present
sensor_wetness_protection_confirmed
sensor_wetness_observed
post_run_sensor_inspection
```
Stop Condition

Stop if liquid reaches the sensor or verification point.

H-005: False Hydrogen Claim From Bubbles
Hazard

Visible gas bubbles may be mistaken for verified hydrogen.

Causes
visual-only observation,
no hydrogen sensor,
unknown gas composition,
operator optimism,
missing acceptance logic.
Consequences
false claim,
bad documentation,
misleading repo,
credibility loss.
Controls
hydrogen-specific detection required,
gas record required,
visual bubbles only allowed as observation,
acceptance gate rejects missing gas evidence.
Evidence Required
```
hydrogen_sensor_model
hydrogen_sensor_state
gas_path_description
acceptance_status
```
Stop Condition

Not a physical stop condition, but claim must be blocked if hydrogen-specific detection is missing.

H-006: Electrical Short Near Water
Hazard

Water or electrolyte may contact electrical connections.

Causes
poor zone separation,
no drip loops,
cables crossing wet zone,
unstable container,
tubing leak,
connector below wet parts,
operator spill.
Consequences
short circuit,
shock risk,
equipment damage,
fire risk,
data loss.
Controls
dry-side power zone,
current-limited supply,
inline fuse/protection,
emergency disconnect,
cable strain relief,
drip control,
wet/electrical separation preflight.
Evidence Required
```
water_electric_separation_confirmed
current_limit_recorded
fuse_or_protection_present
emergency_disconnect_present
```
Stop Condition

Stop if liquid contacts electrical hardware or the layout becomes wet/unclear.

H-007: Missing Emergency Disconnect
Hazard

Operator cannot rapidly stop power during abnormal behavior.

Causes
disconnect omitted,
disconnect blocked,
disconnect behind wet zone,
unclear switch,
cable routing problem.
Consequences
delayed shutdown,
increased hazard,
equipment damage,
operator risk.
Controls
emergency disconnect required,
marked and reachable,
preflight check,
reject layout if wet-zone crossing is needed.
Evidence Required
```
emergency_disconnect_present
emergency_disconnect_reachable
wet_zone_crossing_required_for_shutdown = false
```
Stop Condition

Do not start if emergency disconnect is missing or unreachable.

H-008: Unventilated Operation
Hazard

Hydrogen may accumulate if testing is performed in a poorly ventilated or enclosed space.

Causes
indoor closed room,
ventilation assumed but not checked,
blocked vent path,
small enclosed pocket,
shield or enclosure trapping gas.
Consequences
flammable mixture,
ignition risk,
unsafe exposure,
invalid test.
Controls
ventilation required,
no sealed enclosures,
vent path defined,
operator confirmation,
stop if ventilation changes.
Evidence Required
```
ventilation_present
ventilation_description
vent_path_defined
```
Stop Condition

Stop if ventilation is missing, unknown, or changes during run.

H-009: Unknown Water Chemistry
Hazard

Unknown water conditions may cause unpredictable electrolysis behavior or corrupt evidence.

Causes
undocumented water,
contaminated water,
inconsistent source,
unknown electrolyte,
poor labeling,
no pH/TDS record.
Consequences
false repeatability,
sensor drift,
electrode fouling,
unexpected byproducts,
weak evidence.
Controls
water record required,
source label,
temperature, pH, TDS/conductivity,
visible clarity note,
electrolyte record.
Evidence Required
```
water_source
water_temperature
water_ph
water_tds_or_conductivity
electrolyte_used
```
Stop Condition

Block accepted claim if water record is missing.

H-010: Unknown Electrolyte or Additive
Hazard

Improvised electrolyte or additives may increase chemical, corrosion, gas, or interpretation risk.

Causes
output chasing,
undocumented additive,
mystery catalyst,
contaminated container,
borrowed chemical without record.
Consequences
hazardous byproducts,
corrosion,
sensor cross-sensitivity,
false output change,
disposal issue.
Controls
use only documented chemistry required by selected module,
record source and quantity,
review safety data where applicable,
avoid improvised chemistry in A0.
Evidence Required
```
electrolyte_used
electrolyte_source_or_spec
quantity
compatibility_reviewed
operator_notes
```
Stop Condition

Do not run with unknown or improvised chemistry.

H-011: Oxygen Crossover or Abnormal Separation
Hazard

Gas crossover or abnormal separation may compromise safety and evidence quality.

Causes
damaged membrane,
wrong module setup,
pressure imbalance,
tubing error,
liquid blockage,
unknown cell condition.
Consequences
mixed gas hazard,
poor gas interpretation,
unsafe accumulation,
rejected run.
Controls
oxygen-side observation,
separation checklist,
non-pressurized operation,
stop on abnormal behavior,
post-run inspection.
Evidence Required
```
oxygen_observation_present
oxygen_side_behavior
crossover_concern
separation_integrity_check
```

Stop Condition

Stop if crossover is suspected.

H-012: Sensor Saturation or Drift
Hazard

Sensor readings may be wrong if the sensor saturates, drifts, warms up improperly, or is used beyond range.

Causes
no warmup,
uncalibrated sensor,
wet sensor,
high humidity,
cross-sensitivity,
old sensor,
range exceeded.
Consequences
false hydrogen evidence,
wrong output estimate,
rejected or misleading result.
Controls
sensor model record,
warmup record,
calibration/bump-test record,
limitation notes,
post-run inspection,
reject saturated readings.
Evidence Required

```
sensor_model
sensor_range
sensor_warmup_completed
sensor_calibration_state
sensor_limitations
sensor_saturation_observed
```

Stop Condition

Stop or mark inconclusive if sensor behavior becomes unstable or saturated.

H-013: Gas Leak
Hazard

Gas may escape before verification or accumulate in unintended areas.

Causes
loose fitting,
cracked tubing,
wrong fitting,
no leak check,
tubing pulled by movement,
chamber leak,
damaged trap.
Consequences
unsafe hydrogen release,
false low output,
inconsistent readings,
accumulation risk.
Controls
leak check required,
tubing strain relief,
visible fittings,
post-run inspection,
no hidden gas route.
Evidence Required
```
leak_check_method
leak_check_locations
leak_check_result
post_run_leak_observed
```
Stop Condition

Stop if leak is suspected or leak check fails.

H-014: Tubing Disconnect
Hazard

Tubing may disconnect during operation and release gas or liquid unexpectedly.

Causes
poor fitting,
tubing strain,
movement,
pressure pulse,
loose clamp,
operator bump,
Gankyil-A chamber movement.
Consequences
leak,
liquid spill,
sensor loss,
hydrogen release,
invalid evidence.
Controls
strain relief,
secure fittings,
stable mount,
tubing clips,
stop condition,
pre-run tug-free inspection.
Evidence Required
```
tubing_secured
strain_relief_present
mount_stable
post_run_tubing_condition
```
Stop Condition

Stop immediately if tubing disconnects or shifts.

H-015: Blocked Vent Path
Hazard

A blocked vent path may create pressure or accumulation.

Causes
cap left on,
kinked tube,
liquid slug,
flow meter restriction,
blocked outlet,
operator accidentally covers vent.
Consequences
pressure buildup,
leaks,
rupture,
unsafe accumulation,
invalid data.
Controls
vent path checklist,
outlet visible,
no caps during run,
no restrictive measurement,
stop on restriction concern.
Evidence Required
```
vent_path_defined
vent_path_unblocked
outlet_unblocked
restriction_concern
```
Stop Condition

Stop if vent path blockage is suspected.

H-016: Thermal Runaway or Overheating
Hazard

Heating may damage parts, change chemistry, corrupt sensors, or create unsafe conditions.

Causes
high current,
thermal assist,
poor cooling,
blocked gas path,
module misuse,
sun concentration,
insulation trapping heat.
Consequences
part deformation,
sensor drift,
leak,
chemical change,
fire risk.
Controls
baseline no thermal assist,
current limit,
temperature monitoring,
thermal stop checklist,
component limit review.
Evidence Required
```
water_temp_c
cell_surface_temp_c
ambient_temp_c
thermal_assist_used
temperature_anomaly
```
Stop Condition

Stop if unexpected heating, deformation, smoke, odor, or thermal uncertainty occurs.

H-017: Plasma Branch Ignition / EMI Risk
Hazard

Plasma or activation hardware may create ignition, high-voltage, EMI, reactive species, or measurement corruption hazards.

Causes
high-voltage supply,
plasma near hydrogen,
poor isolation,
unreviewed catalyst,
ozone/reactive species,
electromagnetic coupling into sensors.
Consequences
ignition,
sensor false readings,
equipment damage,
unsafe gas reaction,
invalid evidence.
Controls
plasma/catalyst branch blocked by default,
separate hazard review,
separate test article,
no baseline mixing,
no shared gas accumulation.
Evidence Required
```
branch_selected
advanced_branch_reviewed
plasma_catalyst_blocked
```
Stop Condition

Block any plasma/catalyst run without formal review.

H-018: Misleading Solar-Green Claim
Hazard

A run may be called green hydrogen without source traceability.

Causes
solar nearby but not connected,
battery charge source unknown,
grid power ignored,
thermal input uncounted,
carbon record missing.
Consequences
false green claim,
credibility loss,
invalid proof package.
Controls
energy source record,
renewable fraction estimate,
carbon accounting,
unknown marked as unknown,
acceptance blocks green claim when source is unclear.
Evidence Required
```
source_type
source_description
battery_charge_source
solar_used
renewable_fraction
carbon_record
```
Stop Condition

Not a physical stop condition, but green claim must be blocked if source traceability is incomplete.

H-019: Missing Power Data
Hazard

Without voltage/current/duration, output cannot be interpreted.

Causes
no power meter,
manual log skipped,
meter failure,
supply display trusted without record,
time not recorded.
Consequences
no efficiency claim,
weak hydrogen evidence,
rejected run,
poor repeatability.
Controls
inline power meter,
manual backup form,
timestamp,
acceptance blocks missing power evidence.
Evidence Required
```
voltage_v
current_a
duration_s
energy_wh
instrument_used
```
Stop Condition

Block accepted result if power evidence is missing.

H-020: Missing Evidence Bundle
Hazard

A run may happen but produce no reviewable record.

Causes
run folder missing,
forms not ready,
logging failure,
photos not saved,
manual notes lost.
Consequences
unusable run,
unsupported claim,
repeatability loss.
Controls
create run ID before run,
evidence folder required,
paper backup,
acceptance requires evidence files.
Evidence Required
```
run_id
evidence_folder_created
required_files_present
operator_notes
```
Stop Condition

Block or reject run if evidence cannot be stored.

H-021: Operator Distraction
Hazard

Operator distraction can delay shutdown or miss unsafe behavior.

Causes
multitasking,
phone use,
filming too closely,
unclear roles,
fatigue,
rushing.
Consequences
missed leak,
missed sensor wetting,
delayed shutdown,
unsafe continuation.
Controls
operator present,
no unattended run,
stop if distracted,
clear checklist,
separate observer if filming.
Evidence Required
```
operator_present
operator_role
stop_conditions_reviewed
operator_notes
```
Stop Condition

Stop if operator attention cannot be maintained.

H-022: Poor Bench Layout
Hazard

A confusing layout increases spill, wiring, gas, and evidence errors.

Causes
cluttered bench,
no zones,
crossed tubing and cables,
hidden sensor,
emergency disconnect blocked.
Consequences
unsafe operation,
bad photos,
bad repeatability,
wrong claims.
Controls
six-zone layout,
labels,
setup photos,
wet/dry separation,
emergency access.
Evidence Required
```
zone_layout_photo
wet_zone_defined
dry_zone_defined
emergency_disconnect_reachable
```
Stop Condition

Do not run if the operator cannot explain the setup.

H-023: Gankyil-A Restriction
Hazard

The Gankyil-A chamber may restrict gas flow or trap liquid.

Causes
blocked outlet,
guide insert shifted,
small passages,
liquid pooling,
wrong orientation,
tubing kink.
Consequences
pressure buildup,
sensor corruption,
leak,
invalid comparison,
unsafe run.
Controls
removable insert,
non-pressurized outlet,
orientation record,
restriction stop condition,
post-run inspection.
Evidence Required
```
gankyil_orientation_recorded
outlet_unblocked
guide_insert_stable
restriction_concern
```
Stop Condition

Stop if restriction or pressure buildup is suspected.

H-024: Liquid Carryover Into Downstream Path
Hazard

Liquid may move into gas verification hardware and corrupt measurements.

Causes
separator failure,
high bubbling,
poor chamber angle,
tubing low point,
no trap,
Gankyil-A outlet behavior.
Consequences
wet sensor,
false reading,
rejected run,
cleanup issue.
Controls
liquid trap,
demist stage,
tubing slope control,
visual inspection,
post-run record.
Evidence Required
```
liquid_carryover_observed
liquid_trap_present
sensor_wetness_observed
gas_path_stability
```
Stop Condition

Stop if liquid reaches verification hardware.

H-025: Inflated Claim After Weak Result
Hazard

A weak or incomplete result may be described as stronger than it is.

Causes
excitement,
incomplete evidence review,
visual-only interpretation,
missing carbon accounting,
confusing detected hydrogen with green hydrogen.
Consequences
credibility loss,
unsafe replication,
misleading documentation.
Controls
claim boundary,
acceptance status,
forbidden claim list,
evidence completeness checks.
Evidence Required
```
acceptance_status
claim_boundary
missing_evidence
reviewer_notes
```
Stop Condition

Not physical; block claim until evidence supports it.

H-026: Failed Run Deleted or Rewritten
Hazard

Failed evidence may be lost, hiding risks and weakening learning.

Causes
embarrassment,
desire for clean repo,
manual overwrite,
no rejected-run folder,
no receipt discipline.
Consequences
repeated mistakes,
inflated maturity,
bad review confidence.
Controls
preserve failed runs,
rejected-run examples,
receipts,
immutable run IDs where practical.
Evidence Required
```
run_id
acceptance_status
rejection_reason
receipt
```
Stop Condition

Not physical; do not continue maturity claims without failure preservation.

H-027: Battery Source Misclassified as Renewable
Hazard

Battery-powered run may be called solar or green when the battery charge source is unknown.

Causes
battery used without charge record,
mixed source,
assumption,
missing energy source form.
Consequences
false green claim,
bad carbon accounting,
weak evidence.
Controls
battery charge-source record,
renewable fraction field,
unknown state allowed,
carbon accounting blocks unsupported claim.
Evidence Required
```
battery_used
battery_charge_source
source_type
renewable_fraction
```
Stop Condition

Not physical; block green claim if battery source is unknown.

H-028: Component Compatibility Unknown
Hazard

Unknown compatibility may cause leaks, degradation, contamination, or failure.

Causes
random tubing,
unknown plastics,
unknown fittings,
unknown electrolyte compatibility,
improvised chamber.
Consequences
leak,
sensor contamination,
mechanical failure,
chemical interaction,
invalid run.
Controls
supplier documentation,
compatibility review,
no unknown gas-path parts,
mark questionable parts.
Evidence Required
```
component_list
compatibility_reviewed
unknown_component_present
operator_notes
```
Stop Condition

Do not run with unknown critical gas-path compatibility.

H-029: Fire Extinguisher / PPE Absence
Hazard

Operator lacks basic protective and response equipment.

Causes
rushed setup,
incomplete BOM,
assumption that small test is harmless,
PPE unavailable.
Consequences
increased injury risk,
poor response to incident,
invalid safety posture.
Controls
PPE checklist,
eye protection required,
gloves if electrolyte used,
spill kit,
appropriate emergency equipment per local guidance.
Evidence Required
```
eye_protection_confirmed
gloves_confirmed
spill_kit_available
emergency_equipment_available
```
Stop Condition

Do not run without required PPE and response equipment.

H-030: Post-Run Residual Gas Ambiguity
Hazard

Residual gas may remain in tubing or chamber after shutdown.

Causes
gas path sealed too early,
no post-run venting,
unclear shutdown,
trapped pocket,
operator disassembly too soon.
Consequences
unexpected release,
ignition risk,
bad post-run readings,
unsafe storage.
Controls
normal shutdown checklist,
maintain ventilation,
do not seal gas path prematurely,
post-run sensor record,
final inspection.
Evidence Required
```
power_off_confirmed
venting_completed
gas_path_not_sealed_prematurely
post_run_inspection_complete
```
Stop Condition

Do not disassemble or store until post-run safety state is clear.

Top Risk Items

The highest priority hazards for GH-BENCH-A0 are:

Hydrogen accumulation.
Gas leak.
Electrical short near water.
Pressure buildup.
Ignition source near gas path.
Missing emergency disconnect.
Unventilated operation.
Tubing disconnect.
Wet hydrogen sensor.
Poor gas-path evidence.
Required Controls Before First Physical Run

Before any first physical baseline run:

 Ventilation method confirmed.
 No pressure storage confirmed.
 No sealed accumulation confirmed.
 No ignition sources confirmed.
 Emergency disconnect installed.
 Leak-check method selected.
 Hydrogen detector selected.
 Sensor wetness protection planned.
 Water/electrical separation confirmed.
 Current limit set.
 Fuse/protection installed.
 Gas path documented.
 Evidence folder ready.
 Stop checklist visible.
 Operator present.
Hazard Register Maintenance

Update this hazard register when:

new hardware is selected,
exact sensor models are chosen,
Gankyil-A geometry changes,
solar thermal assist is introduced,
battery path is introduced,
PEC branch is introduced,
redox branch is introduced,
plasma/catalyst branch is proposed,
a run is rejected,
an anomaly occurs,
or external review identifies a new hazard.
Final Rule

A hazard is not handled because it is written down.

A hazard is handled only when the build, procedure, evidence, and operator behavior make the risk harder to trigger and easier to detect.

If a hazard cannot be controlled at bench scale, the run must be blocked.
