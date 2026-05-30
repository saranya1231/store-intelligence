# Store Intelligence Platform - Design Document

## Overview

The Store Intelligence Platform processes retail store events generated from CCTV video analytics and provides business insights through REST APIs. The system captures visitor movements, dwell time, zone interactions, queue behavior, and purchase funnel metrics.

The platform combines computer vision, event processing, analytics, and reporting capabilities to help retailers understand customer behavior and improve operational efficiency.

## Architecture

### Components

### 1. Computer Vision Pipeline

The computer vision layer is responsible for detecting people from images and video streams.

Features:

* YOLOv8-based object detection
* Person detection from CCTV feeds
* Event generation from detections
* Future support for multi-object tracking

### 2. Event Ingestion API

The ingestion layer receives events generated from the detection pipeline.

Features:

* FastAPI-based REST service
* Batch event ingestion
* Event validation
* Duplicate event detection
* Idempotent processing

### 3. Data Storage Layer

The storage layer persists events and supports analytics queries.

Features:

* SQLite database
* Event persistence
* Aggregated metric calculations
* Lightweight deployment

### 4. Intelligence APIs

The analytics layer exposes business intelligence metrics.

Features:

* Store Metrics API
* Conversion Funnel API
* Heatmap Analytics API
* Anomaly Detection API
* Health Monitoring API

## Event Flow

The platform follows an event-driven architecture.

Video/Image Input

→ YOLOv8 Detection

→ Event Generation

→ POST /events/ingest

→ SQLite Storage

→ Analytics APIs

→ Business Insights

This design separates detection from analytics, making the platform easier to scale and maintain.

## Database Design

### Events Table

The Events table stores all visitor activity within the store.

Attributes include:

* Event ID
* Store ID
* Camera ID
* Visitor ID
* Event Type
* Timestamp
* Zone ID
* Dwell Time
* Staff Flag
* Confidence Score

### Event Types

Supported event types:

* ENTRY
* EXIT
* ZONE_ENTER
* BILLING_QUEUE_JOIN
* PURCHASE

These event types are used to calculate visitor behavior metrics and conversion funnel analytics.

## Analytics Layer

### Metrics API

Provides:

* Unique visitor count
* Average dwell time
* Store-level engagement metrics

### Funnel API

Tracks visitor progression through the retail journey:

* Entry count
* Zone visits
* Billing queue visits
* Purchases

### Heatmap API

Provides:

* Zone popularity
* Visitor distribution
* Average dwell time by zone

### Anomaly API

Detects:

* Queue spikes
* Low conversion scenarios
* Operational anomalies

## Deployment

The application is containerized using Docker.

Run:

docker compose up

After startup, APIs are available through:

* Application URL: http://localhost:8000
* Swagger UI: http://localhost:8000/docs
* OpenAPI Specification: http://localhost:8000/openapi.json

## Testing Strategy

The project includes automated testing using Pytest.

Test Coverage Includes:

* Health endpoint validation
* Event ingestion testing
* Metrics API validation

Current coverage exceeds the minimum project requirement and helps ensure application stability.

## Future Enhancements

Planned improvements include:

* ByteTrack integration
* Multi-camera visitor tracking
* PostgreSQL migration
* Real-time streaming analytics
* Dashboard visualization
* Advanced anomaly detection
* Cloud deployment support

## AI-Assisted Decisions

AI-assisted tools were used during development to accelerate implementation, generate initial code templates, assist with debugging, and improve documentation quality.

### Areas Where AI Assistance Was Used

* FastAPI endpoint scaffolding and routing suggestions
* SQLAlchemy model and schema structure recommendations
* Pytest test template generation
* Docker and Docker Compose configuration guidance
* Documentation drafting and formatting
* API validation and troubleshooting support

### Developer Review Process

All AI-generated code and recommendations were manually reviewed, tested, and modified before being integrated into the project.

The final implementation, architecture decisions, testing strategy, and project structure were validated through local execution, automated testing, Docker deployment verification, and API endpoint testing.

### Benefits

Using AI-assisted development improved productivity by reducing boilerplate coding effort and accelerating troubleshooting while allowing focus on system design, business logic, analytics implementation, and production-readiness requirements.
