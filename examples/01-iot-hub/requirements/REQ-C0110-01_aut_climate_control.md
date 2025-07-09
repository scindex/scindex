---
id: REQ-C0110-01
date: 2025-06-05
summary: Automated Climate Control
status: Accepted
baseline: ProjX-FBld-1.0-HHB-20260701
---

# REQ-C0110-01: Automated Climate Control

## User Story

As a homeowner, I want the climate control system to be regulated automatically, in order to remain comfortable without manual intervention.

## Background

This user story defines the core logic for the automated climate control feature. It translates the raw temperature data gathered in `REQ-I0420-01` into actionable commands for the HVAC system, forming the primary value proposition of a smart thermostat.

## Requirements

1. The system shall support an 'Auto' mode that automatically controls the HVAC system.
2. The system shall allow a user to configure a desired temperature setpoint.
3. The system shall use a configurable temperature tolerance (dead band) to prevent rapid on/off cycling.
4. The system shall activate the cooling unit when the ambient temperature (see `REQ-I0420-01` for temperature sensing requirements) exceeds the setpoint plus the tolerance value.
5. The system shall activate the heating unit when the ambient temperature falls below the setpoint minus the tolerance value.
6. The system shall take no action when the ambient temperature is within the tolerance band of the setpoint.

## Acceptance Criteria

### AC1: Activate Cooling When Too Hot
* **GIVEN** the thermostat is set to 'Auto' mode with a setpoint of 72°F and a tolerance of 2°F
* **WHEN** the hub receives a temperature reading of 75°F from the thermostat sensor
* **THEN** the system's state shall change to 'Cooling'
* **AND** an 'on' command shall be sent to the HVAC cooling unit interface.

### AC2: Activate Heating When Too Cold
* **GIVEN** the thermostat is set to 'Auto' mode with a setpoint of 72°F and a tolerance of 2°F
* **WHEN** the hub receives a temperature reading of 69°F from the thermostat sensor
* **THEN** the system's state shall change to 'Heating'
* **AND** an 'on' command shall be sent to the HVAC heating unit interface.

### AC3: Remain Idle Within Tolerance Band
* **GIVEN** the thermostat is set to 'Auto' mode with a setpoint of 72°F and a tolerance of 2°F
* **WHEN** the hub receives a temperature reading of 73°F from the thermostat sensor
* **THEN** the system's state shall remain 'Idle'
* **AND** no command shall be sent to the HVAC interface.

