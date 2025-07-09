# Example Scenario: IoT Home Automation Hub

This example demonstrates how Scindex is used to document an IoT Hub that manages smart devices in a home. The system runs on an embedded device, communicates with sensors and actuators using the MQTT protocol, and is governed by a set of project standards.

## Record Summary & Traceability

This table shows how requirements, decisions, and tests are interconnected using Scindex codes.

| ID                | Type        | Description                                       | Related To                                    |
| ----------------- | ----------- | ------------------------------------------------- | --------------------------------------------- |
| [REQ-I0420-01](./requirements/REQ-I0420-01.md) | Requirement | The hub must ingest temperature data from sensors.  | Implemented by `ADR-D0510-01`                  |
| [REQ-C0110-01](./requirements/REQ-C0110-01.md) | Requirement | The system must use a rules engine for climate control. | Verified by `TST-C0110-01`                    |
| [ADR-P0320-01](./adrs/ADR-P0320-01.md)       | ADR         | Decision to use a Real-Time Operating System (RTOS).  | -                                             |
| [ADR-D0510-01](./adrs/ADR-D0510-01.md)       | ADR         | Decision to use MQTT for all device communication.    | Implements `REQ-I0420-01`                      |
| [TEST-C0110-01](./tests/TST-C0110-01.md)      | Test Case   | Verifies the climate control rule works correctly.  | Tests `REQ-C0110-01`                           |
| [GEN-0210-01](./standards/G0210-01.md)     | Standard    | Defines the C++ code formatting standard.           | Applies to all firmware development            |