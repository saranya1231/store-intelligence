# Store Intelligence Platform

## Overview

The Store Intelligence Platform processes retail store events generated from CCTV analytics and provides actionable business insights through REST APIs and visual dashboards.

The system combines computer vision, event processing, analytics, anomaly detection, and dashboard visualization to help retailers understand visitor behavior and store performance.

---

## Features

### Event Ingestion

* Batch event ingestion API
* Event validation
* Duplicate event detection
* SQLite event storage

### Analytics APIs

* Store Metrics
* Conversion Funnel
* Heatmap Analytics
* Anomaly Detection
* Health Monitoring

### Computer Vision

* YOLOv8 Person Detection
* CCTV Video Processing
* Person Counting Analytics
* CSV Analytics Export
* Future support for Multi-Object Tracking

### Dashboard

* Streamlit Dashboard
* Peak Occupancy Analytics
* Average Occupancy Analytics
* Camera-wise Person Count Trends

### Deployment

* Docker Support
* Swagger Documentation
* SQLite Database

---

## Project Structure

```text
store-intelligence/

├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── ingestion.py
│   ├── metrics.py
│   ├── funnel.py
│   ├── heatmap.py
│   └── anomalies.py
│
├── pipeline/
│   ├── detect.py
│   ├── tracker.py
│   ├── emit.py
│   ├── event_generator.py
│   └── video_detector.py
│
├── docs/
│   ├── DESIGN.md
│   └── CHOICES.md
│
├── tests/
├── data/
├── database/
├── logs/
│
├── dashboard.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## Installation

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
.\venv\Scripts\Activate.ps1
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
uvicorn app.main:app --reload
```

Application URL:

```text
http://127.0.0.1:8000
```

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

## Docker Deployment

Build:

```bash
docker compose build
```

Run:

```bash
docker compose up
```

Swagger UI:

```text
http://localhost:8000/docs
```

---

## Run CCTV Video Analytics

Process CCTV videos and generate person-count analytics:

```bash
python pipeline/video_detector.py
```

Output:

```text
person_counts.csv
```

The CSV contains:

* Camera Name
* Frame Number
* Person Count

---

## Run Dashboard

Start the Streamlit dashboard:

```bash
streamlit run dashboard.py
```

Dashboard URL:

```text
http://localhost:8501
```

Dashboard Features:

* Camera Selection
* Peak Occupancy
* Average Occupancy
* Person Count Trend Graph

---

## Available APIs

### POST /events/ingest

Ingest visitor events into the platform.

### GET /stores/{store_id}/metrics

Returns:

* Unique Visitors
* Average Dwell Time

### GET /stores/{store_id}/funnel

Returns:

* Entries
* Zone Visits
* Billing Queue Visits
* Purchases

### GET /stores/{store_id}/heatmap

Returns:

* Zone Visit Counts
* Average Zone Dwell Time

### GET /stores/{store_id}/anomalies

Returns:

* Queue Spike Alerts
* Conversion Issues

### GET /health

Returns application health status.

---

## Technology Stack

* Python 3.11
* FastAPI
* SQLAlchemy
* SQLite
* Docker
* YOLOv8
* OpenCV
* Ultralytics
* Streamlit
* Pandas

---

## Event Log Output

The project includes a sample event log file:

```text
sample_events.jsonl
```

The file follows the required JSONL format and demonstrates retail event generation from CCTV analytics.

Supported event types include:

* ENTRY
* EXIT
* ZONE_ENTER
* ZONE_DWELL
* BILLING_QUEUE_JOIN
* PURCHASE

Additional attributes include:

* Store ID
* Camera ID
* Visitor ID
* Timestamp
* Zone ID
* Staff Identification Flag
* Detection Confidence Score

Each line in the file represents a valid JSON event record and follows the challenge event schema requirements.

---

## Testing

Run all tests:

```bash
pytest
```

Current Status:

* Health API Tests Passed
* Ingestion API Tests Passed
* Metrics API Tests Passed

Coverage:

```text
82%
```

---

## Future Enhancements

* ByteTrack Integration
* Multi-Camera Tracking
* Real-Time Event Streaming
* PostgreSQL Migration
* Advanced Anomaly Detection
* Live Retail Dashboard
* Multi-Store Analytics

---

## AI-Assisted Development

AI tools were used to accelerate development, generate initial code structures, create test templates, assist with Docker setup, and draft documentation.

All generated code was reviewed, modified, tested, and integrated manually into the final solution.
