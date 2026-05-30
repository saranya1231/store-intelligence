# Store Intelligence Platform - Design Document

## Overview

The Store Intelligence Platform processes retail store events generated from CCTV video analytics and provides business insights through REST APIs. The system captures visitor movements, dwell time, zone interactions, queue behavior, and purchase funnel metrics.

## Architecture

### Components

1. Computer Vision Pipeline
   - YOLOv8-based object detection
   - Person detection from images and video streams
   - Event generation from detections

2. Event Ingestion API
   - FastAPI-based REST service
   - Batch event ingestion
   - Event validation and deduplication

3. Data Storage
   - SQLite database
   - Event persistence
   - Metrics aggregation

4. Intelligence APIs
   - Store metrics
   - Conversion funnel analysis
   - Heatmap analytics
   - Anomaly detection

## Event Flow

Video/Image Input
→ YOLO Detection
→ Event Generation
→ POST /events/ingest
→ SQLite Storage
→ Analytics APIs

## Database Design

### Events Table

Stores:
- Event ID
- Store ID
- Camera ID
- Visitor ID
- Event Type
- Timestamp
- Zone ID
- Dwell Time
- Staff Flag
- Confidence Score

### Event Types

- ENTRY
- EXIT
- ZONE_ENTER
- BILLING_QUEUE_JOIN
- PURCHASE

## Analytics Layer

### Metrics API

Provides:
- Unique visitors
- Average dwell time

### Funnel API

Tracks:
- Entry count
- Zone visits
- Billing queue visits
- Purchases

### Heatmap API

Provides:
- Zone popularity
- Average dwell time per zone

### Anomaly API

Detects:
- Queue spikes
- Low conversion situations

## Deployment

The application is containerized using Docker and can be started using:

docker compose up

## Future Enhancements

- ByteTrack integration
- Multi-camera tracking
- PostgreSQL migration
- Real-time streaming analytics
- Dashboard visualization