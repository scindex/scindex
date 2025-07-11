# Software Component Index (Scindex)

 version: _0.2.1_
 date: _11/07/2025_

 ---

## Division: M - METHODOLOGY & CONVENTIONS
*This division covers overarching standards, processes, and methodologies related to how the project is managed and how the software is developed.*

### Section: M01 - Project Management & Methodology
_Covers the processes for planning, executing, and managing project work._

- **M0110**: Work Planning & Execution
  - *Description*: Defines the methodology for breaking down project work and the cadence of execution, from high-level phases or epics to individual tasks.
  - *Examples*: Work Breakdown Structure (WBS), Agile Epics & Stories, Project Phases & Gates, Kanban Policies

- **M0120**: Release Planning & Coordination
  - *Description*: The process for planning, scheduling, and coordinating software releases, including versioning strategy.
  - *Examples*: Release Train Schedule, Semantic Versioning Policy, Go/No-Go Checklists

- **M0130**: Decision Making & Governance
  - *Description*: The formal process for making and recording architectural or significant technical decisions.
  - *Examples*: Architecture Decision Record (ADR) Process, Technical Steering Committee Charter

- **M0140**: Team Roles & Responsibilities
  - *Description*: Defines the key roles within the project team and their primary responsibilities.
  - *Examples*: RACI Matrix, Product Owner vs Project Manager, Architect Role

- **M0150**: Vendor & Stakeholder Communication Process
  - *Description*: Contact information and communications proceess for external vendors or stakeholders.

- **M0160**: Budget & Financial Process
  - *Description*: Administrative processes related to project budget, invoicing, or purchasing.

- **M0170**: Legal & Compliance Adherence
  - *Description*: Documentation records and notes related to legal reviews, compliance requirements, or data privacy impact assessments.

- **M0199**: Provisional Project Management & Methodology Item
  - *Description*: A temporary holding category for Project Management & Methodology items that do not fit other defined items. Use sparingly and submit a 'Suggestion' issue to have the component formally added to the Scindex.

### Section: M02 - Development Standards & Conventions
_Covers coding standards and conventions to ensure consistency and quality._

- **M0210**: Code Formatting & Style
  - *Description*: Rules for code formatting, including line length, indentation, and style guidelines enforced by linters.
  - *Examples*: Prettier/ESLint Config, Black Formatter Rules, EditorConfig

- **M0220**: Identifier & Naming Conventions
  - *Description*: Guidelines for naming variables, functions, classes, database tables, and other identifiers.
  - *Examples*: Variable Naming (camelCase, snake_case), API Endpoint Naming, Git Branch Naming

- **M0230**: Scindex Usage & Suffix Rules
  - *Description*: Specific rules governing how Scindex codes and suffixes are applied within the project.
  - *Examples*: ADR Suffix Rules, Requirement Suffix Format

- **M0299**: Provisional Development Standards & Conventions Item
  - *Description*: A temporary holding category for Development Standards & Conventions items that do not fit other defined items. Use sparingly and submit a 'Suggestion' issue to have the component formally added to the Scindex.

### Section: M03 - Quality & Testing Strategy
_Defines the overall approach to ensuring software quality._

- **M0310**: Code Review Process
  - *Description*: The standards and process for conducting pull request reviews, including required approvals and review etiquette.
  - *Examples*: Pull Request Templates, Mandatory Reviewer Checklists

- **M0320**: Testing Level Definitions
  - *Description*: The strategy and scope for different levels of testing, such as unit, integration, and end-to-end (E2E) tests.
  - *Examples*: Unit Test Coverage Thresholds, Integration Test Strategy, E2E Test Scenarios

- **M0399**: Provisional Quality & Testing Strategy Item
  - *Description*: A temporary holding category for Quality & Testing Strategy items that do not fit other defined items. Use sparingly and submit a 'Suggestion' issue to have the component formally added to the Scindex.

### Section: M04 - Documentation Standards
_Covers requirements for how project and system documentation is created and maintained._

- **M0410**: Documentation Structure & Style
  - *Description*: Defines the required structure, file organization, and content for project documents, along with the official writing style, tone, and terminology to ensure consistency.

- **M0499**: Provisional Documentation Standards Item
  - *Description*: A temporary holding category for Documentation Standards items that do not fit other defined items. Use sparingly and submit a 'Suggestion' issue to have the component formally added to the Scindex.

### Section: M99 - Provisional METHODOLOGY & CONVENTIONS Section
_A temporary holding section for METHODOLOGY & CONVENTIONS components that do not fit into any other defined section. Use sparingly and submit a 'Suggestion' issue to have a formal section added._

- **M9999**: Uncategorized METHODOLOGY & CONVENTIONS Component
  - *Description*: A provisional item for a component in the METHODOLOGY & CONVENTIONS division that lacks a formal section or item category. Please open a 'Suggestion' issue to have this component and its category formally added.

## Division: D - DATA MANAGEMENT
*This division is dedicated to how data is stored, retrieved, structured, and managed.*

### Section: D01 - Databases
_Covers systems for storing, retrieving, and managing structured and unstructured data, including relational, NoSQL, time-series, and graph databases._

- **D0110**: Relational Databases
  - *Description*: Databases using a structured, table-based format with rows and columns, enforcing ACID properties. Ideal for transactional data and complex queries.
  - *Examples*: PostgreSQL, MySQL

- **D0120**: NoSQL Databases
  - *Description*: Databases providing flexible data models (key-value, document, columnar, etc.). They excel at handling large-scale, unstructured data and horizontal scaling.
  - *Examples*: MongoDB, DynamoDB

- **D0130**: Time-Series Databases
  - *Description*: Databases optimized for storing and querying time-stamped data points, such as metrics, sensor readings, and financial data. High-performance for time-based analysis.
  - *Examples*: InfluxDB

- **D0140**: Graph Databases
  - *Description*: Databases that use graph structures with nodes, edges, and properties to represent and store data. Ideal for managing highly connected data and complex relationships.
  - *Examples*: Neo4j

- **D0199**: Provisional Databases Item
  - *Description*: A temporary holding category for Databases items that do not fit other defined items. Use sparingly and submit a 'Suggestion' issue to have the component formally added to the Scindex.

### Section: D02 - Caching
_Focuses on temporary data storage to reduce latency. Includes in-memory caches for rapid access, CDNs for distributed content, and client-side caching to improve user experience._

- **D0210**: In-Memory Caches
  - *Description*: Data stores that keep frequently accessed data in RAM for extremely fast retrieval, reducing latency and load on primary databases or services.
  - *Examples*: Redis, Memcached

- **D0220**: Content Delivery Networks (CDN)
  - *Description*: Geographically distributed networks of proxy servers that cache content close to users, accelerating the delivery of web assets and reducing latency.
  - *Examples*: Cloudflare, Akamai, Fastly

- **D0230**: Client-Side Caching
  - *Description*: Storing data directly on the user's device (e.g., in a web browser) to speed up repeat visits, reduce network requests, and enable offline functionality.
  - *Examples*: Browser Cache, Service Worker Cache

- **D0299**: Provisional Caching Item
  - *Description*: A temporary holding category for Caching items that do not fit other defined items. Use sparingly and submit a 'Suggestion' issue to have the component formally added to the Scindex.

### Section: D03 - Storage Systems & Abstractions
_Deals with underlying storage tech and access patterns. Covers object/block storage, file systems, and ORMs that bridge application code and relational databases._

- **D0310**: Object Storage
  - *Description*: A system for storing large amounts of unstructured data as objects in a flat address space. Highly scalable and durable, accessed via APIs.
  - *Examples*: S3, Google Cloud Storage

- **D0320**: Block Storage & File Systems
  - *Description*: Systems that manage data as blocks within sectors and tracks, abstracted by a file system (e.g., ext4, NTFS) for hierarchical organization and access.
  - *Examples*: ext4, NTFS, APFS, Amazon EBS

- **D0330**: Object-Relational Mappers (ORM)
  - *Description*: Libraries that provide an abstraction layer to convert data between object-oriented programming languages and relational databases, simplifying data access.
  - *Examples*: SQLAlchemy, Hibernate, Entity Framework

- **D0399**: Provisional Storage Systems & Abstractions Item
  - *Description*: A temporary holding category for Storage Systems & Abstractions items that do not fit other defined items. Use sparingly and submit a 'Suggestion' issue to have the component formally added to the Scindex.

### Section: D04 - Data Structure & Integrity
_Defines data structure, serialization, and validation. Covers schemas, migrations, data formats, and integrity checks like hashing and error correction to ensure data quality._

- **D0410**: Database Schemas & Migrations
  - *Description*: The formal definition of a database's structure (schema) and the version-controlled scripts (migrations) used to manage its evolution over time.
  - *Examples*: Alembic, Flyway, Liquibase

- **D0420**: Data Serialization Formats
  - *Description*: Standardized formats for converting data structures into a format that can be stored or transmitted and reconstructed later. Essential for APIs and configuration.
  - *Examples*: JSON, XML, Protocol Buffers

- **D0430**: Data Validation Schemas & Rules Engines
  - *Description*: Systems for defining and enforcing rules and constraints on data, ensuring it conforms to a predefined structure and meets business requirements.
  - *Examples*: JSON Schema, Schematron

- **D0440**: Checksums & Hashing
  - *Description*: Techniques used to verify data integrity. A checksum or hash is computed from data and can be re-checked later to detect accidental alterations or corruption.
  - *Examples*: CRC32, SHA-256

- **D0450**: Error Detection & Correction Codes
  - *Description*: Algorithms that add redundant data to messages, allowing the receiver to detect and, in some cases, correct errors that occurred during transmission or storage.
  - *Examples*: Reed-Solomon, Hamming codes

- **D0499**: Provisional Data Structure & Integrity Item
  - *Description*: A temporary holding category for Data Structure & Integrity items that do not fit other defined items. Use sparingly and submit a 'Suggestion' issue to have the component formally added to the Scindex.

### Section: D05 - Data Transport & Protocols
_Encompasses methods for moving data between systems. Covers real-time messaging, high-performance serialization formats, and publish/subscribe communication models._

- **D0510**: Real-Time Messaging Protocols
  - *Description*: Protocols designed for low-latency, high-throughput communication, often used in IoT, industrial automation, and financial systems for timely data exchange.
  - *Examples*: DDS, AMQP, MQTT

- **D0520**: Data Marshalling & IPC Formats
  - *Description*: Formats and protocols for serializing and deserializing data structures for inter-process communication (IPC), enabling different processes to exchange complex data.
  - *Examples*: Apache Avro, Thrift, CORBA

- **D0530**: Bit-Encoding Formats
  - *Description*: Highly efficient, low-level data serialization formats that use bit-level encoding to achieve minimal message size and very fast (de)serialization speeds.
  - *Examples*: SBE, Google FlatBuffers

- **D0540**: Data Subscription & Publication Models
  - *Description*: Communication patterns where message producers (publishers) send messages to channels, and consumers (subscribers) receive them, decoupling senders and receivers.
  - *Examples*: Pub/Sub, Observer Pattern

- **D0599**: Provisional Data Transport & Protocols Item
  - *Description*: A temporary holding category for Data Transport & Protocols items that do not fit other defined items. Use sparingly and submit a 'Suggestion' issue to have the component formally added to the Scindex.

### Section: D06 - In-Memory & Volatile Data
_Covers data held temporarily in memory. This includes shared memory for IPC, in-process stores for application state, and hardware registers for low-level control._

- **D0610**: Shared Memory Segments
  - *Description*: A method of inter-process communication (IPC) where multiple processes can access the same region of memory, allowing for very fast data exchange.
  - *Examples*: POSIX shm, System V shm, Windows File Mapping

- **D0620**: In-Process Data Stores
  - *Description*: Data structures held within a single process's memory space, used for managing application state, session data, or temporary information without external dependencies.
  - *Examples*: Session State Objects, Game State Singletons, In-Memory Queues

- **D0630**: Volatile Configuration & Status Registers
  - *Description*: Low-level hardware registers used to control device operations, configure peripherals, or read status flags. Data is volatile and lost on power-off.
  - *Examples*: GPIO Control Registers, DMA Controller Registers, CPU Flags

- **D0699**: Provisional In-Memory & Volatile Data Item
  - *Description*: A temporary holding category for In-Memory & Volatile Data items that do not fit other defined items. Use sparingly and submit a 'Suggestion' issue to have the component formally added to the Scindex.

### Section: D99 - Provisional DATA MANAGEMENT Section
_A temporary holding section for DATA MANAGEMENT components that do not fit into any other defined section. Use sparingly and submit a 'Suggestion' issue to have a formal section added._

- **D9999**: Uncategorized DATA MANAGEMENT Component
  - *Description*: A provisional item for a component in the DATA MANAGEMENT division that lacks a formal section or item category. Please open a 'Suggestion' issue to have this component and its category formally added.

## Division: P - PLATFORM & INFRASTRUCTURE
*This division covers the foundational components on which the software operates.*

### Section: P01 - Compute
_Execution environments for code, from virtualized hardware to serverless functions. Covers VMs, containers, bare-metal processors, and specialized hardware accelerators._

- **P0110**: Virtual Machines
  - *Description*: Emulated computer systems that provide the functionality of a physical computer. They run on a hypervisor and allow multiple OS instances on a single machine.
  - *Examples*: VMware, VirtualBox, QEMU

- **P0120**: Containers
  - *Description*: Lightweight, standalone, executable packages of software that include everything needed to run it: code, runtime, system tools, system libraries, and settings.
  - *Examples*: Docker, containerd

- **P0130**: Serverless Functions
  - *Description*: Event-driven, stateless compute functions that run in the cloud without requiring server management. They scale automatically and are billed based on execution time.
  - *Examples*: AWS Lambda, Azure Functions

- **P0140**: Bare Metal / Embedded Processors
  - *Description*: Directly running on physical hardware without a host OS or hypervisor. Common in embedded systems and high-performance computing for maximum control and low overhead.
  - *Examples*: Raspberry Pi, Arduino, ARM Cortex-M

- **P0150**: Hardware Acceleration
  - *Description*: Specialized hardware (GPUs, FPGAs, ASICs) used to perform specific tasks more efficiently than a general-purpose CPU, often for graphics, AI, or scientific computing.
  - *Examples*: FPGA, GPU, ASIC

- **P0199**: Provisional Compute Item
  - *Description*: A temporary holding category for Compute items that do not fit other defined items. Use sparingly and submit a 'Suggestion' issue to have the component formally added to the Scindex.

### Section: P02 - Networking
_Communication infrastructure. Defines protocols, virtual networks, firewalls, service discovery for microservices, and high-performance interconnects for specialized systems._

- **P0210**: Network Protocols (TCP/IP, HTTP, MQTT)
  - *Description*: The rules and conventions for communication between network devices. Includes foundational protocols like TCP/IP and application-layer protocols like HTTP and MQTT.
  - *Examples*: TCP/IP, HTTP, WebSockets

- **P0220**: Virtual Networks & Firewalls
  - *Description*: Software-defined networks (e.g., VPCs) that provide isolation and security, and firewalls that control incoming and outgoing network traffic based on security rules.
  - *Examples*: VPC, iptables, pf

- **P0230**: Service Discovery & Mesh
  - *Description*: Mechanisms for services to find and communicate with each other in a distributed system. A service mesh adds reliability, security, and observability features.
  - *Examples*: Consul, Istio, Linkerd

- **P0240**: Real-Time & HPC Interconnects
  - *Description*: High-bandwidth, low-latency networking technologies designed for demanding applications like high-performance computing (HPC), real-time systems, and data centers.
  - *Examples*: InfiniBand, Time-Sensitive Networking (TSN), DDS

- **P0299**: Provisional Networking Item
  - *Description*: A temporary holding category for Networking items that do not fit other defined items. Use sparingly and submit a 'Suggestion' issue to have the component formally added to the Scindex.

### Section: P03 - Runtime Environments
_The environment in which a program is executed. Includes language-specific runtimes, the underlying operating system, and hardware abstraction layers (HALs)._

- **P0310**: Language Runtimes
  - *Description*: The environment that interprets or compiles code and manages its execution. Includes a virtual machine (e.g., JVM) or an interpreter (e.g., Python).
  - *Examples*: JVM, Node.js, Python Interpreter

- **P0320**: Operating Systems
  - *Description*: System software that manages computer hardware and software resources and provides common services for computer programs. Includes general-purpose and real-time OS (RTOS).
  - *Examples*: Linux, Windows, RTOS

- **P0330**: Hardware Abstraction Layers (HAL)
  - *Description*: An abstraction layer between a computer's physical hardware and its software. It provides a consistent interface for applications, hiding hardware-specific details.
  - *Examples*: CMSIS, Android HAL

- **P0399**: Provisional Runtime Environments Item
  - *Description*: A temporary holding category for Runtime Environments items that do not fit other defined items. Use sparingly and submit a 'Suggestion' issue to have the component formally added to the Scindex.

### Section: P04 - Orchestration & Management
_Tools for automating the deployment, management, scaling, and networking of containerized applications and infrastructure._

- **P0410**: Container Orchestration
  - *Description*: Automates the deployment, scaling, and management of containerized applications. Manages the lifecycle of containers across a cluster of machines.
  - *Examples*: Kubernetes, Amazon ECS, Docker Swarm

- **P0420**: Infrastructure Provisioning & IaC
  - *Description*: Managing and provisioning computer data centers through machine-readable definition files (Infrastructure as Code), rather than physical hardware configuration.
  - *Examples*: Terraform, AWS CloudFormation, Ansible

- **P0430**: Cluster Management
  - *Description*: Software that manages a collection of computer servers (a cluster) as a single system, handling resource allocation, scheduling, and fault tolerance.
  - *Examples*: Apache Mesos, HashiCorp Nomad

- **P0499**: Provisional Orchestration & Management Item
  - *Description*: A temporary holding category for Orchestration & Management items that do not fit other defined items. Use sparingly and submit a 'Suggestion' issue to have the component formally added to the Scindex.

### Section: P05 - System Startup & Firmware
_Low-level software that initializes hardware during the boot process. Includes bootloaders, device drivers, and firmware update mechanisms._

- **P0510**: Bootloaders
  - *Description*: The first software that runs when a device is powered on. It initializes the hardware and loads the operating system kernel into memory.
  - *Examples*: U-Boot, GRUB, Barebox

- **P0520**: Device Drivers
  - *Description*: Software that allows the operating system to communicate with and control a specific hardware device, such as a network card, printer, or storage controller.
  - *Examples*: Linux Kernel Modules, Peripheral Drivers (e.g., for CAN, I2C, SPI)

- **P0530**: Firmware Update Agents
  - *Description*: Software components responsible for securely and reliably updating the firmware of a device, often over-the-air (OTA), to add features or patch vulnerabilities.
  - *Examples*: OTA Clients, Secure Update Handlers

- **P0599**: Provisional System Startup & Firmware Item
  - *Description*: A temporary holding category for System Startup & Firmware items that do not fit other defined items. Use sparingly and submit a 'Suggestion' issue to have the component formally added to the Scindex.

### Section: P99 - Provisional PLATFORM & INFRASTRUCTURE Section
_A temporary holding section for PLATFORM & INFRASTRUCTURE components that do not fit into any other defined section. Use sparingly and submit a 'Suggestion' issue to have a formal section added._

- **P9999**: Uncategorized PLATFORM & INFRASTRUCTURE Component
  - *Description*: A provisional item for a component in the PLATFORM & INFRASTRUCTURE division that lacks a formal section or item category. Please open a 'Suggestion' issue to have this component and its category formally added.

## Division: S - SYSTEM SERVICES
*This division includes cross-cutting concerns and supporting services that are not part of the core application logic.*

### Section: S01 - Security
_Ensures the confidentiality, integrity, and availability of the system. Covers authentication, authorization, cryptography, and threat detection._

- **S0110**: Authentication Services
  - *Description*: Verify the identity of users or systems. Includes protocols like OAuth for delegated access and SSO for unified login.
  - *Examples*: OAuth, SSO

- **S0120**: Authorization & Permissions
  - *Description*: Define and enforce access control policies, determining what authenticated users are allowed to do. Includes RBAC and ACL models.
  - *Examples*: RBAC, ACLs, JWT Claims

- **S0130**: Cryptography & Secrets Management
  - *Description*: Secure data at rest and in transit using encryption. Manages sensitive information like API keys and passwords through vaults.
  - *Examples*: AES, RSA, HashiCorp Vault

- **S0140**: Anomaly & Threat Detection
  - *Description*: Monitor and analyze system activity to identify potential security threats, intrusions, or unusual behavior in real-time.
  - *Examples*: Snort, Falco

- **S0199**: Provisional Security Item
  - *Description*: A temporary holding category for Security items that do not fit other defined items. Use sparingly and submit a 'Suggestion' issue to have the component formally added to the Scindex.

### Section: S02 - Observability
_Provides insights into system behavior through logs, metrics, and traces, enabling debugging, monitoring, and performance analysis._

- **S0210**: Logging
  - *Description*: Record discrete events from applications and infrastructure. Essential for debugging, auditing, and understanding system activity.
  - *Examples*: Log4j, Winston, Serilog

- **S0220**: Metrics & Monitoring
  - *Description*: Collect and visualize numerical data over time to track system health, performance, and resource utilization.
  - *Examples*: Prometheus, Grafana, Datadog

- **S0230**: Tracing & Performance Analysis
  - *Description*: Track requests as they flow through a distributed system, providing insights into latency, dependencies, and performance bottlenecks.
  - *Examples*: Jaeger, Zipkin, OpenTelemetry

- **S0299**: Provisional Observability Item
  - *Description*: A temporary holding category for Observability items that do not fit other defined items. Use sparingly and submit a 'Suggestion' issue to have the component formally added to the Scindex.

### Section: S03 - Communication
_Mechanisms for data exchange between different parts of a system or between different systems._

- **S0310**: Message Queues
  - *Description*: Enable asynchronous communication between services, decoupling senders and receivers and improving system resilience and scalability.
  - *Examples*: RabbitMQ, SQS

- **S0320**: Event Streams
  - *Description*: Handle real-time data streams for high-throughput, fault-tolerant processing. Used for event-driven architectures and data pipelines.
  - *Examples*: Kafka, Kinesis

- **S0330**: Inter-Process Communication (IPC)
  - *Description*: Mechanisms that allow different processes on the same machine to communicate and synchronize their actions.
  - *Examples*: Pipes, Sockets, Shared Memory

- **S0399**: Provisional Communication Item
  - *Description*: A temporary holding category for Communication items that do not fit other defined items. Use sparingly and submit a 'Suggestion' issue to have the component formally added to the Scindex.

### Section: S04 - Utilities
_General-purpose supporting services that provide common functionalities across the application._

- **S0410**: Configuration Management
  - *Description*: Manage and distribute application configuration data, allowing for dynamic updates and consistent settings across environments.
  - *Examples*: Consul, etcd, Spring Cloud Config

- **S0420**: Scheduling & Background Jobs
  - *Description*: Execute tasks at specified times or intervals, or run long-running processes in the background without blocking the main application.
  - *Examples*: cron, Celery, Hangfire

- **S0430**: Feature Flagging
  - *Description*: Enable or disable functionality dynamically without deploying new code, allowing for A/B testing, canary releases, and controlled rollouts.
  - *Examples*: LaunchDarkly, Flagsmith

- **S0499**: Provisional Utilities Item
  - *Description*: A temporary holding category for Utilities items that do not fit other defined items. Use sparingly and submit a 'Suggestion' issue to have the component formally added to the Scindex.

### Section: S05 - Memory Management
_Techniques for efficient allocation, usage, and freeing of memory resources._

- **S0510**: Custom Memory Allocators
  - *Description*: Specialized allocators (e.g., pool, slab) designed to improve performance or reduce fragmentation for specific memory usage patterns.
  - *Examples*: Pool Allocators, Slab Allocators

- **S0520**: Garbage Collection Services
  - *Description*: Automated memory management that reclaims memory occupied by objects that are no longer in use by the program.
  - *Examples*: Generational GC, Real-time GC

- **S0530**: Memory Safety & Leak Detection
  - *Description*: Tools and techniques to prevent memory-related bugs like buffer overflows and to identify memory that is no longer used but not released.
  - *Examples*: Valgrind, AddressSanitizer (ASan), Rust Borrow Checker

- **S0599**: Provisional Memory Management Item
  - *Description*: A temporary holding category for Memory Management items that do not fit other defined items. Use sparingly and submit a 'Suggestion' issue to have the component formally added to the Scindex.

### Section: S06 - Concurrency & Synchronization
_Manages the simultaneous execution of multiple tasks and ensures safe access to shared resources._

- **S0610**: Threading & Tasking Models
  - *Description*: Frameworks for managing concurrent execution, including thread pools for reusing threads and actor models for message-passing concurrency.
  - *Examples*: Thread Pools, Actor Models, Async/Await Runtimes

- **S0620**: Synchronization Primitives
  - *Description*: Low-level mechanisms like mutexes and semaphores used to coordinate access to shared resources and prevent race conditions.
  - *Examples*: Mutexes, Semaphores, Atomics

- **S0630**: Deadlock Detection & Prevention
  - *Description*: Algorithms and strategies to identify and resolve or prevent circular dependencies between threads waiting for resources.
  - *Examples*: Lock Ordering, Wait-for Graph Analysis, Banker's Algorithm

- **S0699**: Provisional Concurrency & Synchronization Item
  - *Description*: A temporary holding category for Concurrency & Synchronization items that do not fit other defined items. Use sparingly and submit a 'Suggestion' issue to have the component formally added to the Scindex.

### Section: S07 - Fault Tolerance & Resilience
_Ensures the system remains operational despite failures. Includes health monitoring, redundancy, and graceful degradation._

- **S0710**: Health Monitoring & Watchdogs
  - *Description*: Mechanisms that monitor the state of system components and can trigger recovery actions if a component becomes unresponsive.
  - *Examples*: Hardware Watchdog Timers, Heartbeat Mechanisms, Supervisor Daemons

- **S0720**: Redundancy & Failover Management
  - *Description*: Systems that provide backup components (redundancy) and automatically switch to them (failover) when a primary component fails.
  - *Examples*: Active-Passive Failover, Active-Active Load Balancing, RAID Controllers

- **S0730**: Graceful Degradation & Recovery Services
  - *Description*: Strategies that allow a system to continue operating at a reduced level of functionality during failures, rather than failing completely.
  - *Examples*: Circuit Breaker Pattern, Load Shedding, Safe Mode Operation

- **S0799**: Provisional Fault Tolerance & Resilience Item
  - *Description*: A temporary holding category for Fault Tolerance & Resilience items that do not fit other defined items. Use sparingly and submit a 'Suggestion' issue to have the component formally added to the Scindex.

### Section: S99 - Provisional SYSTEM SERVICES Section
_A temporary holding section for SYSTEM SERVICES components that do not fit into any other defined section. Use sparingly and submit a 'Suggestion' issue to have a formal section added._

- **S9999**: Uncategorized SYSTEM SERVICES Component
  - *Description*: A provisional item for a component in the SYSTEM SERVICES division that lacks a formal section or item category. Please open a 'Suggestion' issue to have this component and its category formally added.

## Division: C - APPLICATION CORE
*This division contains the primary business logic, algorithms, and unique functional components of the software.*

### Section: C01 - Business Logic
_The core logic that encodes the real-world business rules and processes that the software is designed to automate._

- **C0110**: Rules Engines
  - *Description*: Systems that externalize business logic from application code, allowing rules to be defined and managed independently.
  - *Examples*: Drools, Jess

- **C0120**: Domain Logic & Services (including adapters for 3rd-party logic)
  - *Description*: The implementation of the core business concepts, entities, and processes that define the application's primary function.
  - *Examples*: Business Services, Domain Models, Anti-corruption Layers

- **C0130**: Workflow & Orchestration Logic
  - *Description*: Manages the sequence of tasks and interactions required to complete a business process, often spanning multiple services.
  - *Examples*: Camunda, AWS Step Functions

- **C0199**: Provisional Business Logic Item
  - *Description*: A temporary holding category for Business Logic items that do not fit other defined items. Use sparingly and submit a 'Suggestion' issue to have the component formally added to the Scindex.

### Section: C02 - Data Processing & Algorithms
_Core algorithms for transforming, analyzing, and processing data to generate insights or new information._

- **C0210**: Search & Indexing Algorithms
  - *Description*: Algorithms for efficiently finding and retrieving information from large datasets by creating and querying optimized data structures (indexes).
  - *Examples*: Elasticsearch, Lucene, TF-IDF

- **C0220**: Machine Learning Models & Inference
  - *Description*: The use of statistical models to make predictions or decisions. Inference is the process of using a trained model to make predictions.
  - *Examples*: TensorFlow, PyTorch, scikit-learn

- **C0230**: Signal & Image Processing
  - *Description*: Algorithms for analyzing, modifying, and synthesizing signals, such as audio, images, and sensor data.
  - *Examples*: OpenCV, FFT, Wavelets

- **C0240**: Data Transformation & ETL Logic
  - *Description*: Processes for extracting data from sources, transforming it into a desired format, and loading it into a target system (Extract, Transform, Load).
  - *Examples*: Apache Spark, Pandas, dbt

- **C0299**: Provisional Data Processing & Algorithms Item
  - *Description*: A temporary holding category for Data Processing & Algorithms items that do not fit other defined items. Use sparingly and submit a 'Suggestion' issue to have the component formally added to the Scindex.

### Section: C03 - State Management
_Manages the state of the application, including user sessions and real-time data synchronization._

- **C0310**: Application State
  - *Description*: The data that represents the current condition of the application, often managed in a centralized store in client-side applications.
  - *Examples*: Redux, Vuex, Recoil

- **C0320**: Session Management
  - *Description*: The process of tracking a user's interaction with an application across multiple requests, typically using tokens or cookies.
  - *Examples*: JWT, OAuth2 Sessions, Cookie-based Sessions

- **C0330**: Real-Time State Synchronization
  - *Description*: Ensuring that state is kept consistent across multiple clients or between client and server in real-time applications.
  - *Examples*: Firebase Realtime Database, Socket.IO

- **C0399**: Provisional State Management Item
  - *Description*: A temporary holding category for State Management items that do not fit other defined items. Use sparingly and submit a 'Suggestion' issue to have the component formally added to the Scindex.

### Section: C04 - Execution & Scheduling Models
_Defines how and when different parts of the code are executed, from real-time schedulers to event-driven models._

- **C0410**: Real-Time Schedulers
  - *Description*: Scheduling algorithms used in real-time operating systems to ensure that tasks meet their deadlines.
  - *Examples*: Rate-Monotonic, Earliest Deadline First

- **C0420**: Event-Driven & Reactive Models
  - *Description*: Architectural patterns where the flow of the program is determined by events, such as user actions or messages from other services.
  - *Examples*: Reactor Pattern, Proactor Pattern, ReactiveX

- **C0430**: Control Loops & Cyclic Executives
  - *Description*: A common model in embedded systems where a main loop continuously runs, executing a fixed set of tasks in a repeating cycle.
  - *Examples*: Main Loop, Fixed-Period Schedulers

- **C0440**: Behavior Trees & State Machines
  - *Description*: Models for representing and controlling the flow of logic, commonly used in AI, robotics, and game development.
  - *Examples*: FSMs, Behavior Trees

- **C0499**: Provisional Execution & Scheduling Models Item
  - *Description*: A temporary holding category for Execution & Scheduling Models items that do not fit other defined items. Use sparingly and submit a 'Suggestion' issue to have the component formally added to the Scindex.

### Section: C05 - Resource Management Logic
_Logic for allocating and managing system resources like bandwidth, CPU, and power._

- **C0510**: Resource Reservation & Admission Control
  - *Description*: Mechanisms to reserve resources for specific tasks and to control access to resources to prevent overload.
  - *Examples*: Token Bucket Algorithm, Semaphore-based Limiting

- **C0520**: Quality of Service (QoS) Management
  - *Description*: Techniques for managing network traffic and other resources to ensure a certain level of performance for critical applications.
  - *Examples*: Traffic Shaping, Priority Queues

- **C0530**: Power Management Logic
  - *Description*: Algorithms and strategies for optimizing power consumption, especially in battery-powered or embedded devices.
  - *Examples*: CPU Throttling, Sleep Modes

- **C0599**: Provisional Resource Management Logic Item
  - *Description*: A temporary holding category for Resource Management Logic items that do not fit other defined items. Use sparingly and submit a 'Suggestion' issue to have the component formally added to the Scindex.

### Section: C06 - Time & Synchronization Logic
_Manages time within the system, including synchronization with external time sources and logical clocks._

- **C0610**: Time Source Management
  - *Description*: Managing and synchronizing the system clock with external, accurate time sources like NTP or GPS.
  - *Examples*: NTP Clients, PTP Stacks, GPSD

- **C0620**: Logical Clocks & Timestamping
  - *Description*: Algorithms for ordering events in a distributed system without relying on a single, global clock.
  - *Examples*: Lamport Timestamps, Vector Clocks

- **C0630**: Time-Triggered Logic
  - *Description*: A model where actions are triggered at predetermined points in time, common in safety-critical and real-time systems.
  - *Examples*: Time-Triggered Architectures (TTA)

- **C0699**: Provisional Time & Synchronization Logic Item
  - *Description*: A temporary holding category for Time & Synchronization Logic items that do not fit other defined items. Use sparingly and submit a 'Suggestion' issue to have the component formally added to the Scindex.

### Section: C99 - Provisional APPLICATION CORE Section
_A temporary holding section for APPLICATION CORE components that do not fit into any other defined section. Use sparingly and submit a 'Suggestion' issue to have a formal section added._

- **C9999**: Uncategorized APPLICATION CORE Component
  - *Description*: A provisional item for a component in the APPLICATION CORE division that lacks a formal section or item category. Please open a 'Suggestion' issue to have this component and its category formally added.

## Division: I - INTERFACES
*This division covers all components related to interaction with users, devices, or other software systems.*

### Section: I01 - Graphical User Interfaces (GUI)
_Visual interfaces that allow users to interact with the software through graphical icons and visual indicators._

- **I0110**: Desktop Application Interfaces
  - *Description*: The native windows and widgets of a desktop operating system's GUI framework.
  - *Examples*: WinForms, Cocoa

- **I0120**: Web Interfaces (HTML, CSS, Web Components)
  - *Description*: User interfaces built with web technologies that run in a web browser.
  - *Examples*: React, Vue, Angular, Lit

- **I0130**: Mobile Application Screens (iOS/Android native UI)
  - *Description*: The native screens and UI components of mobile operating systems like iOS and Android.
  - *Examples*: SwiftUI, Jetpack Compose

- **I0199**: Provisional Graphical User Interfaces (GUI) Item
  - *Description*: A temporary holding category for Graphical User Interfaces (GUI) items that do not fit other defined items. Use sparingly and submit a 'Suggestion' issue to have the component formally added to the Scindex.

### Section: I02 - Non-Graphical Human Interfaces
_Interfaces that allow human interaction without a graphical display, such as command-line, voice, or haptic feedback._

- **I0210**: Command Line Interfaces (CLI)
  - *Description*: Text-based interfaces used to run programs, manage computer files, and interact with the system.
  - *Examples*: argparse, Cobra, oclif

- **I0220**: Voice User Interfaces (VUI)
  - *Description*: Interfaces that allow users to interact with a system using voice commands.
  - *Examples*: Alexa Skills, Google Actions

- **I0230**: Text-Based User Interfaces (TUI)
  - *Description*: Interfaces that use text, symbols, and colors in a terminal environment to create a user interface.
  - *Examples*: ncurses, Rich, Bubble Tea

- **I0240**: Haptic & Tactile Interfaces
  - *Description*: Interfaces that provide feedback to the user through the sense of touch, such as vibrations or force feedback.
  - *Examples*: Core Haptics, Vibration API

- **I0299**: Provisional Non-Graphical Human Interfaces Item
  - *Description*: A temporary holding category for Non-Graphical Human Interfaces items that do not fit other defined items. Use sparingly and submit a 'Suggestion' issue to have the component formally added to the Scindex.

### Section: I03 - Programmatic Interfaces (API)
_Interfaces that allow different software components or systems to communicate with each other._

- **I0310**: REST APIs
  - *Description*: An architectural style for designing networked applications, using a stateless, client-server communication model based on HTTP.
  - *Examples*: OpenAPI (Swagger), RAML

- **I0320**: GraphQL APIs
  - *Description*: A query language for APIs and a runtime for fulfilling those queries with your existing data. It gives clients the power to ask for exactly what they need.
  - *Examples*: Apollo, Relay

- **I0330**: gRPC / RPC Endpoints
  - *Description*: A high-performance, open-source universal RPC framework. gRPC is based on defining a service, specifying the methods that can be called remotely with their parameters and return types.
  - *Examples*: Protocol Buffers, Thrift

- **I0340**: Library APIs / SDKs (Provided by this system)
  - *Description*: A set of tools, libraries, and documentation provided by this system to allow other developers to build applications that interact with it.
  - *Examples*: C++ SDK, Python SDK, Java SDK

- **I0350**: External API Interfaces (Consumed by this system)
  - *Description*: Interfaces that this system uses to communicate with and consume services from third-party systems.
  - *Examples*: Stripe API, Twilio API

- **I0399**: Provisional Programmatic Interfaces (API) Item
  - *Description*: A temporary holding category for Programmatic Interfaces (API) items that do not fit other defined items. Use sparingly and submit a 'Suggestion' issue to have the component formally added to the Scindex.

### Section: I04 - Hardware & Sensor Interfaces
_Interfaces for interacting with physical hardware, sensors, and actuators._

- **I0410**: General Purpose Input/Output (GPIO)
  - *Description*: A generic pin on an integrated circuit whose behavior can be controlled by the user at run time.
  - *Examples*: libgpiod, RPi.GPIO

- **I0420**: Sensor Data Ingestion
  - *Description*: The process of collecting and importing data from various sensors for storage and analysis.
  - *Examples*: accelerometer, GPS

- **I0430**: Actuator Control
  - *Description*: The control of mechanical or electrical devices that perform a physical action, such as motors, valves, or switches.
  - *Examples*: PWM Servo Control, Stepper Motor Drivers

- **I0499**: Provisional Hardware & Sensor Interfaces Item
  - *Description*: A temporary holding category for Hardware & Sensor Interfaces items that do not fit other defined items. Use sparingly and submit a 'Suggestion' issue to have the component formally added to the Scindex.

### Section: I05 - Diagnostic & Debug Interfaces
_Covers interfaces used primarily for system diagnostics, debugging, and real-time monitoring, which may be separate from the main application interfaces._

- **I0510**: Debug Ports
  - *Description*: Low-level hardware interfaces used for in-circuit debugging, programming, and testing of microcontrollers and other integrated circuits.
  - *Examples*: JTAG, SWD

- **I0520**: Telemetry & Monitoring Endpoints
  - *Description*: Dedicated endpoints for exporting application or system metrics, logs, and telemetry data to monitoring tools.
  - *Examples*: Prometheus Exporters, StatsD, Custom UDP Streams

- **I0530**: Hardware-in-the-Loop (HIL) Interfaces
  - *Description*: Interfaces that connect a real-time system to a simulated environment, allowing for testing of the system's hardware and software components together.
  - *Examples*: FPGA-based HIL, dSPACE, Opal-RT

- **I0599**: Provisional Diagnostic & Debug Interfaces Item
  - *Description*: A temporary holding category for Diagnostic & Debug Interfaces items that do not fit other defined items. Use sparingly and submit a 'Suggestion' issue to have the component formally added to the Scindex.

### Section: I06 - Industrial & Field Bus Interfaces
_Specialized, often rugged, communication protocols (buses) used for real-time control and data acquisition in industrial, automotive, and avionics environments._

- **I0610**: Automotive Buses
  - *Description*: Protocols designed for communication between electronic control units (ECUs) within vehicles, optimized for reliability and real-time performance.
  - *Examples*: CAN bus, LIN bus, FlexRay, Automotive Ethernet

- **I0620**: Industrial Automation Buses
  - *Description*: Protocols used for communication and control of machinery and equipment in industrial settings, such as factory floors and processing plants.
  - *Examples*: Modbus, PROFIBUS, EtherCAT

- **I0630**: Avionics Buses
  - *Description*: Data buses specifically designed for the high-reliability, safety-critical environment of aircraft and spacecraft electronics.
  - *Examples*: ARINC 429, MIL-STD-1553, AFDX

- **I0699**: Provisional Industrial & Field Bus Interfaces Item
  - *Description*: A temporary holding category for Industrial & Field Bus Interfaces items that do not fit other defined items. Use sparingly and submit a 'Suggestion' issue to have the component formally added to the Scindex.

### Section: I07 - System Management & Control Interfaces
_Interfaces designed for out-of-band management, low-level hardware control, and monitoring of the physical system's health and environment._

- **I0710**: Baseboard Management Controllers (BMC)
  - *Description*: A specialized service processor on a server motherboard that allows for remote monitoring and management of the host system, independent of the main CPU and OS.
  - *Examples*: IPMI, Redfish, iDRAC, iLO

- **I0720**: Power & Clock Control Interfaces
  - *Description*: Interfaces and standards for managing the power states, clock speeds, and thermal properties of system components to optimize performance and energy consumption.
  - *Examples*: ACPI, PMBus

- **I0730**: System Health & Environmental Sensors
  - *Description*: Interfaces for reading data from onboard sensors that monitor the physical health of the system, such as fan speeds, component temperatures, and voltage levels.
  - *Examples*: Fan Speed Sensors, Temperature Sensors, Voltage Monitors

- **I0799**: Provisional Industrial & Field Bus Interfaces Item
  - *Description*: A temporary holding category for Industrial & Field Bus Interfaces items that do not fit other defined items. Use sparingly and submit a 'Suggestion' issue to have the component formally added to the Scindex.

### Section: I07 - System Management & Control Interfaces
_Interfaces designed for out-of-band management, low-level hardware control, and monitoring of the physical system's health and environment._

- **I0710**: Baseboard Management Controllers (BMC)
  - *Description*: A specialized service processor on a server motherboard that allows for remote monitoring and management of the host system, independent of the main CPU and OS.
  - *Examples*: IPMI, Redfish, iDRAC, iLO

- **I0720**: Power & Clock Control Interfaces
  - *Description*: Interfaces and standards for managing the power states, clock speeds, and thermal properties of system components to optimize performance and energy consumption.
  - *Examples*: ACPI, PMBus

- **I0730**: System Health & Environmental Sensors
  - *Description*: Interfaces for reading data from onboard sensors that monitor the physical health of the system, such as fan speeds, component temperatures, and voltage levels.
  - *Examples*: Fan Speed Sensors, Temperature Sensors, Voltage Monitors

- **I0799**: Provisional System Management & Control Interfaces Item
  - *Description*: A temporary holding category for System Management & Control Interfaces items that do not fit other defined items. Use sparingly and submit a 'Suggestion' issue to have the component formally added to the Scindex.

### Section: I99 - Provisional INTERFACES Section
_A temporary holding section for INTERFACES components that do not fit into any other defined section. Use sparingly and submit a 'Suggestion' issue to have a formal section added._

- **I9999**: Uncategorized INTERFACES Component
  - *Description*: A provisional item for a component in the INTERFACES division that lacks a formal section or item category. Please open a 'Suggestion' issue to have this component and its category formally added.

## Division: N - DISTRIBUTION & PACKAGING
*This division defines the final form of the software product as delivered to the end-user or system.*

### Section: N01 - Packaged & Deployed Artifacts
_The final form of the software as a distributable or deployable unit. Includes installers, container images, firmware, and reusable libraries for consumption by end-users or other systems._

- **N0110**: Desktop Installers
  - *Description*: Packages used to install software on desktop operating systems, such as MSI for Windows, DMG for macOS, and .deb for Debian-based Linux.
  - *Examples*: MSI, DMG, .deb

- **N0120**: Mobile App Bundles
  - *Description*: The package format used to distribute and install mobile applications, such as APK for Android and IPA for iOS.
  - *Examples*: APK, IPA

- **N0130**: Container Images
  - *Description*: A lightweight, standalone, executable package of software that includes everything needed to run an application.
  - *Examples*: Docker Image

- **N0140**: Firmware Images
  - *Description*: A file that contains the complete contents and structure of a device's firmware, used for flashing or updating the device.
  - *Examples*: .bin, .hex

- **N0150**: Web Application Builds (e.g., static assets)
  - *Description*: The compiled and optimized static files (HTML, CSS, JavaScript) that make up a web application, ready for deployment.
  - *Examples*: Webpack build, Vite build

- **N0160**: Published Packages
  - *Description*: Libraries published to a public or private package registry for easy consumption by other developers.
  - *Examples*: to npm, PyPI, Maven

- **N0170**: Shared Libraries
  - *Description*: Libraries that are loaded by programs when they start. They are shared among multiple programs, saving memory and disk space.
  - *Examples*: .dll, .so

- **N0199**: Provisional Packaged & Deployed Artifacts Item
  - *Description*: A temporary holding category for Packaged & Deployed Artifacts items that do not fit other defined items. Use sparingly and submit a 'Suggestion' issue to have the component formally added to the Scindex.

### Section: N04 - Source & Intermediate Distributions
_Deliverables where the end-user is expected to compile, build, or integrate the software themselves, common for SDKs, embedded systems, and open-source projects._

- **N0410**: Source Code Archives
  - *Description*: The complete, uncompiled source code of a software project, compressed into a single archive file for distribution.
  - *Examples*: .tar.gz, .zip

- **N0420**: Build System & Toolchain Packages
  - *Description*: Packages and configuration files for specialized build systems, used to compile a complete, custom operating system and application for a target device.
  - *Examples*: Yocto Layers, Buildroot Configs, Crosstool-NG

- **N0430**: Pre-compiled Object & Static Libraries
  - *Description*: Files containing compiled code (.o, .obj) or archives of object files (.a, .lib) that are linked into a final executable during the build process.
  - *Examples*: .o, .a, .lib

- **N0499**: Provisional Source & Intermediate Distributions Item
  - *Description*: A temporary holding category for Source & Intermediate Distributions items that do not fit other defined items. Use sparingly and submit a 'Suggestion' issue to have the component formally added to the Scindex.

### Section: N05 - Provisioned Hardware & Appliances
_Covers scenarios where the software is delivered pre-installed on physical hardware or as a complete, self-contained virtual machine image._

- **N0510**: Pre-flashed Hardware
  - *Description*: Physical hardware, such as microcontrollers or complete devices, that is delivered to the end-user with the software firmware already installed ('flashed').
  - *Examples*: Pre-flashed Microcontrollers, Development Kits

- **N0520**: Virtual Appliances
  - *Description*: A pre-packaged virtual machine image that contains a pre-configured operating system and all the necessary application software, ready to be run in a hypervisor.
  - *Examples*: OVA, VHD, QCOW2

- **N0530**: Bootable Media
  - *Description*: A storage medium (e.g., USB drive, CD/DVD, or ISO file) that contains a bootable operating system and application, allowing a user to run the software without installing it on their hard drive.
  - *Examples*: Live ISOs, USB Boot Images

- **N0599**: Provisional Provisioned Hardware & Appliances Item
  - *Description*: A temporary holding category for Provisioned Hardware & Appliances items that do not fit other defined items. Use sparingly and submit a 'Suggestion' issue to have the component formally added to the Scindex.

### Section: N06 - Live & Dynamic Distributions
_Mechanisms for delivering updates or new components to a system that is already running, which is critical for high-availability systems that cannot be shut down._

- **N0610**: Live Patches & Hotfixes
  - *Description*: Applying critical code changes (patches) to a running system in memory without restarting the service or machine, often to fix urgent bugs or security vulnerabilities.
  - *Examples*: Kernel Live Patches, Dynamic Hot-swapping

- **N0620**: Dynamic Module Loading
  - *Description*: The capability of an application to load new code modules, such as plugins or shared libraries, at runtime to extend or modify its functionality without a restart.
  - *Examples*: Plugin Systems, Dynamic Library Loading

- **N0630**: Over-the-Air (OTA) Update Payloads
  - *Description*: The package containing the software update that is delivered wirelessly to a device. Payloads can be small delta patches or complete firmware images.
  - *Examples*: Delta Update Packages, Full Image Updates

- **N0699**: Provisional Live & Dynamic Distributions Item
  - *Description*: A temporary holding category for Live & Dynamic Distributions items that do not fit other defined items. Use sparingly and submit a 'Suggestion' issue to have the component formally added to the Scindex.

### Section: N99 - Provisional DISTRIBUTION & PACKAGING Section
_A temporary holding section for DISTRIBUTION & PACKAGING components that do not fit into any other defined section. Use sparingly and submit a 'Suggestion' issue to have a formal section added._

- **N9999**: Uncategorized DISTRIBUTION & PACKAGING Component
  - *Description*: A provisional item for a component in the DISTRIBUTION & PACKAGING division that lacks a formal section or item category. Please open a 'Suggestion' issue to have this component and its category formally added.