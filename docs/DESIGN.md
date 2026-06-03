# Store Intelligence Platform - Design Document

## Overview

The Store Intelligence Platform converts CCTV video observations into actionable retail intelligence. The system processes visitor activity, generates structured events, stores them in a centralized repository, computes analytics, and exposes business insights through REST APIs and a live dashboard.

The primary business objective is to help retailers understand customer behavior, identify operational issues, and improve store conversion rates.

---

# System Architecture

The platform follows a modular event-driven architecture consisting of four major layers:

1. Detection Layer
2. Event Processing Layer
3. Intelligence API Layer
4. Dashboard Layer

## High-Level Flow

Video/Image Input

→ Detection Pipeline

→ Structured Events

→ Event Ingestion API

→ SQLite Storage

→ Analytics Engine

→ REST APIs

→ Live Dashboard

This separation ensures that detection logic remains independent from analytics and reporting components.

---

# Component Design

## 1. Detection Pipeline

The detection layer is responsible for identifying customers from CCTV footage and generating business events.

Responsibilities:

* Person detection using YOLOv8
* Detection confidence evaluation
* Event creation
* Visitor activity tracking
* Structured event generation

Output events include:

* ENTRY
* EXIT
* ZONE_ENTER
* BILLING_QUEUE_JOIN
* PURCHASE

The detection layer acts as the producer in the event-driven architecture.

---

## 2. Event Ingestion API

The ingestion service receives events from the detection pipeline.

Responsibilities:

* Event validation
* Schema enforcement
* Duplicate detection
* Idempotent ingestion
* Event persistence

The API accepts event batches and stores validated records in the database.

---

## 3. Storage Layer

SQLite is used as the persistence layer.

Responsibilities:

* Store event records
* Support analytics queries
* Maintain visitor activity history
* Enable reporting APIs

SQLite was selected because it requires no additional infrastructure and simplifies reviewer setup.

---

## 4. Intelligence API Layer

The intelligence layer transforms raw events into business metrics.

Supported APIs:

### Metrics API

Provides:

* Unique visitors
* Average dwell time
* Store engagement metrics

### Funnel API

Tracks visitor progression:

ENTRY → ZONE_VISIT → BILLING_QUEUE → PURCHASE

Provides:

* Funnel counts
* Conversion rates
* Drop-off percentages

### Heatmap API

Provides:

* Zone popularity
* Visitor distribution
* Average dwell time by zone

### Anomaly API

Detects:

* Queue spikes
* Conversion drops
* Operational abnormalities

### Health API

Provides:

* Service availability
* Basic platform diagnostics

---

# Database Design

## Events Table

Stores all visitor activity.

Attributes:

* Event ID
* Store ID
* Camera ID
* Visitor ID
* Event Type
* Timestamp
* Zone ID
* Dwell Time
* Confidence Score
* Staff Flag

This structure enables downstream analytics without requiring access to raw video.

---

# Event Flow

1. CCTV footage is processed by the detection pipeline.
2. Person detections are converted into business events.
3. Events are submitted to the ingestion API.
4. Events are validated and stored.
5. Analytics services compute business metrics.
6. REST APIs expose results.
7. Dashboard visualizes store performance.

---

# Testing Strategy

Automated testing was implemented using Pytest.

Coverage includes:

* Health endpoint testing
* Event ingestion validation
* Metrics endpoint verification
* API response validation

Testing helps ensure reliability and maintainability of the platform.

---

# AI-Assisted Decisions

AI tools were used throughout development to accelerate implementation and evaluate design alternatives.

## Decision 1: Database Selection

AI initially suggested PostgreSQL because it is commonly used in production analytics systems.

Decision Taken:

SQLite was selected instead.

Reason:

* Simpler reviewer setup
* No external database dependency
* Faster challenge deployment

Trade-Off:

SQLite sacrifices horizontal scalability but significantly improves ease of evaluation.

---

## Decision 2: Detection Architecture

AI suggested exploring more advanced tracking approaches such as DeepSORT and ByteTrack.

Decision Taken:

A simplified YOLOv8-based detection pipeline was implemented.

Reason:

* Faster implementation
* Lower complexity
* Sufficient for challenge requirements

Trade-Off:

Advanced tracking could improve re-identification accuracy but would increase implementation complexity.

---

## Decision 3: Analytics Architecture

AI suggested tightly coupling analytics calculations with ingestion logic.

Decision Taken:

Analytics computation was separated from ingestion.

Reason:

* Better maintainability
* Cleaner architecture
* Easier future scaling

Trade-Off:

Additional abstraction introduces slightly more complexity but improves long-term flexibility.

---

# Future Enhancements

Potential future improvements include:

* ByteTrack integration
* Multi-camera visitor tracking
* PostgreSQL migration
* Real-time streaming analytics
* Advanced anomaly detection
* Cloud deployment support
* Cross-store performance comparisons

---

# Conclusion

The Store Intelligence Platform demonstrates a complete retail analytics workflow from computer vision event generation to business intelligence reporting. The modular architecture supports future enhancements while remaining lightweight, easy to deploy, and suitable for rapid evaluation.
