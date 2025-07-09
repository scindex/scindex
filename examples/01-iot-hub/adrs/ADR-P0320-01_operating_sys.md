---
id: ADR-P0320-01
date: 2025-06-04
summary: Choice of Operating System
status: Accepted
baseline: ProjX-FBld-1.0-HHB-20260701
---

# ADR-P0320-01: Choice of Operating System

## Context
The IoT Hub must guarantee that sensor data is processed within tight time constraints to ensure responsive control of home devices. A general-purpose OS may introduce non-deterministic scheduling delays (jitter).

## Decision
We will use a Real-Time Operating System (RTOS), specifically FreeRTOS, as the foundational OS for the hub's embedded processor.

## Consequences
* **Positive**: Provides predictable, deterministic task scheduling, ensuring real-time deadlines are met. Lower resource footprint (RAM/CPU) than a full Linux distribution.
* **Negative**: More limited ecosystem of libraries and drivers compared to Linux. Steeper learning curve for developers unfamiliar with real-time concepts.