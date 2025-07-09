---
id: REQ-I0420-01
date: 2025-06-09
summary: Temperature Sensor Ingestion
status: Accepted
baseline: ProjX-FBld-1.0-HHB-20260701
---

# REQ-I0420-01: Temperature Sensor Ingestion

## User Story

As a **system administrator**, I want **the hub to reliably ingest data from all connected thermostats**, in order to **provide accurate input for the automated climate control logic**.

## Background

This requirement defines the foundational data-gathering capability of the IoT Hub. Accurate and timely ingestion of environmental data is critical for all higher-level automation features, particularly the climate control logic specified in `REQ-C0110-01`. It establishes the primary communication protocol and polling frequency for thermostat devices.

## Requirements

1. The system **shall** communicate with thermostat sensors using the Zigbee protocol.
2. The system **shall** ingest both temperature and humidity values from each sensor.
3. The system **shall** poll each registered sensor for new data at a regular interval of 30 seconds.
4. The system **shall** maintain a list of registered thermostat sensors to actively poll.
5. The system **shall** log a warning if a registered sensor fails to respond after three consecutive polling attempts.

## Acceptance Criteria

### AC1: Successful Data Ingestion
* **GIVEN** a Zigbee thermostat sensor is registered with the hub and is online
* **WHEN** a 30-second polling interval elapses
* **THEN** the system shall receive a new temperature and humidity reading from the sensor
* **AND** the received data shall be stored as the current value for that sensor.

### AC2: Sensor Becomes Unresponsive
* **GIVEN** a registered sensor has responded successfully to previous polls
* **WHEN** the sensor fails to respond to three consecutive polling attempts
* **THEN** the system shall mark the sensor's status as 'unresponsive'
* **AND** a warning message shall be written to the system log.

