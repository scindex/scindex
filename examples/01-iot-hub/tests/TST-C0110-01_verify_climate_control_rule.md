---
id: TST-C0110-01
verifies: ["REQ-C0110-01"]
---

# TST-C0110-01: Test Plan for Automated Climate Control

## Objective
This test plan outlines the specific test cases required to verify all functionality of the automated climate control logic as defined in requirement `REQ-C0110-01`.

## Test Cases

### TC-1: Verify Cooling Activation
* **Description**: Verifies the system correctly activates cooling when the ambient temperature exceeds the upper tolerance boundary. This covers `AC1`.
* **Preconditions**:
    1. The system is in `Idle` state.
    2. The operating mode is set to `Auto`.
    3. The temperature setpoint is configured to `72°F`.
    4. The temperature tolerance is configured to `2°F`.
* **Steps**:
    1. Simulate a temperature reading of `75°F` from the thermostat sensor (`REQ-I0420-01`).
* **Expected Results**:
    1. The system's internal state transitions to `Cooling`.
    2. An 'on' command is sent to the HVAC cooling unit interface within 500ms of processing the reading.

### TC-2: Verify Heating Activation
* **Description**: Verifies the system correctly activates heating when the ambient temperature falls below the lower tolerance boundary. This covers `AC2`.
* **Preconditions**:
    1. The system is in `Idle` state.
    2. The operating mode is set to `Auto`.
    3. The temperature setpoint is configured to `72°F`.
    4. The temperature tolerance is configured to `2°F`.
* **Steps**:
    1. Simulate a temperature reading of `69°F` from the thermostat sensor (`REQ-I0420-01`).
* **Expected Results**:
    1. The system's internal state transitions to `Heating`.
    2. An 'on' command is sent to the HVAC heating unit interface within 500ms of processing the reading.

### TC-3: Verify Idle State Within Tolerance Band
* **Description**: Verifies the system remains idle when the temperature is within the acceptable tolerance "dead band". This covers `AC3`.
* **Preconditions**:
    1. The system is in `Idle` state.
    2. The operating mode is set to `Auto`.
    3. The temperature setpoint is configured to `72°F`.
    4. The temperature tolerance is configured to `2°F`.
* **Steps**:
    1. Simulate a temperature reading of `73°F` from the thermostat sensor (`REQ-I0420-01`).
* **Expected Results**:
    1. The system's internal state remains `Idle`.
    2. No command is sent to any HVAC interface.

### TC-4: Verify Upper Boundary Condition
* **Description**: Verifies the system remains idle when the temperature is exactly at the upper tolerance boundary, confirming "exceeds" logic.
* **Preconditions**:
    1. The system is in `Idle` state.
    2. The operating mode is set to `Auto`.
    3. The temperature setpoint is configured to `72°F`.
    4. The temperature tolerance is configured to `2°F`.
* **Steps**:
    1. Simulate a temperature reading of `74°F` (exactly `setpoint + tolerance`).
* **Expected Results**:
    1. The system's internal state remains `Idle`.
    2. No command is sent to any HVAC interface.