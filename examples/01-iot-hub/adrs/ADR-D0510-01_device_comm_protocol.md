---
id: ADR-D0510-01
date: 2025-06-02
summary: "Device Communication Protocol"
status: Accepted
baseline: ProjX-FBld-1.0-HHB-20260701
---

# ADR-D0510-01: Device Communication Protocol

## Context
The hub needs to communicate with a variety of low-power smart devices (sensors, lights) over potentially unreliable home Wi-Fi networks. The protocol must be lightweight and handle intermittent connectivity gracefully.

## Decision
We will use **MQTT** as the standard messaging protocol for all device-to-hub communication. A central MQTT broker will run on the hub itself.

## Consequences
* **Positive**: The publish/subscribe model decouples devices from the hub. MQTT's low overhead is ideal for constrained devices. Its Quality of Service (QoS) levels provide reliable message delivery.
* **Negative**: Introduces a single point of failure (the MQTT broker). Requires all devices to have an MQTT client library.