# Technology Choices and Design Rationale

This document explains key architectural and technology decisions made during development of the Store Intelligence Platform.

---

# Decision 1: Detection Model

## Options Considered

1. YOLOv8
2. YOLOv9
3. RT-DETR

## Selected Option

YOLOv8

## Why YOLOv8

* Mature ecosystem
* Strong person detection performance
* Easy Python integration
* Lightweight deployment
* Extensive documentation

## Why Other Options Were Not Selected

### YOLOv9

Pros:

* Newer architecture

Cons:

* Less mature tooling
* Limited deployment familiarity

### RT-DETR

Pros:

* High detection quality

Cons:

* More complex integration
* Higher implementation effort

Given the challenge timeline, YOLOv8 provided the best balance between accuracy, simplicity, and deployment speed.

---

# Decision 2: Event Schema Design

## Options Considered

### Raw Detection Storage

Store every frame-level detection.

### Structured Event Storage

Store business events such as ENTRY, EXIT, ZONE_ENTER, and PURCHASE.

## Selected Option

Structured Event Storage

## Reason

Business analytics operate on visitor behavior rather than frame-level detections.

Structured events:

* Reduce storage requirements
* Simplify analytics queries
* Improve maintainability
* Align directly with business KPIs

---

# Decision 3: API Architecture

## Options Considered

### Monolithic Processing

Detection and analytics tightly coupled.

### Event-Driven Processing

Detection emits events that are processed independently.

## Selected Option

Event-Driven Processing

## Reason

Benefits include:

* Better modularity
* Easier maintenance
* Future scalability
* Clear separation of concerns

This approach also mirrors real-world retail analytics architectures.

---

# Decision 4: Database Selection

## Options Considered

### SQLite

### PostgreSQL

## Selected Option

SQLite

## Reason

SQLite offers:

* Zero configuration
* Lightweight deployment
* Fast setup
* Simple evaluation environment

## Trade-Off

PostgreSQL would provide better scalability and concurrency but increases operational complexity.

For challenge requirements, SQLite was the most practical choice.

---

# Decision 5: Framework Selection

## Options Considered

### FastAPI

### Flask

### Django REST Framework

## Selected Option

FastAPI

## Reason

FastAPI provides:

* High performance
* Automatic Swagger documentation
* Strong validation through Pydantic
* Type safety
* Excellent developer productivity

These features significantly reduced development effort while improving API quality.

---

# Decision 6: Deployment Strategy

## Options Considered

### Native Local Setup

### Dockerized Deployment

## Selected Option

Docker

## Reason

Docker provides:

* Reproducible builds
* Environment consistency
* Dependency isolation
* One-command deployment

This aligns directly with challenge requirements.

---

# AI Usage Reflection

AI tools were used for:

* Initial architecture brainstorming
* API scaffolding suggestions
* Test generation templates
* Documentation drafting
* Deployment troubleshooting

All generated content was manually reviewed, modified, tested, and validated before inclusion in the final solution.

Several AI recommendations were intentionally not adopted, including PostgreSQL deployment and advanced tracking architectures, because they increased complexity without providing proportional benefit for the challenge objectives.

The final design prioritizes simplicity, maintainability, reviewer experience, and alignment with the business goals of the challenge.
