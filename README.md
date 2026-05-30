# Store Intelligence Platform

## Overview

The Store Intelligence Platform processes retail store events generated from CCTV analytics and provides actionable business insights through REST APIs.

The system combines computer vision, event processing, analytics, and anomaly detection to help retailers understand visitor behavior and store performance.

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
* Event Generation Pipeline
* Future support for Multi-Object Tracking

### Deployment

* Docker Support
* Swagger Documentation
* SQLite Database

---

## Project Structure

store-intelligence/

├── app/

│ ├── main.py

│ ├── database.py

│ ├── models.py

│ ├── schemas.py

│ ├── ingestion.py

│ ├── metrics.py

│ ├── funnel.py

│ ├── heatmap.py

│ └── anomalies.py

│

├── pipeline/

│ ├── detect.py

│ ├── tracker.py

│ └── emit.py

│

├── docs/

│ ├── README.md

│ ├── DESIGN.md

│ └── CHOICES.md

│

├── tests/

├── data/

├── database/

├── logs/

├── Dockerfile

├── docker-compose.yml

├── requirements.txt

└── README.md

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

---

## Future Enhancements

* ByteTrack Integration
* Multi-Camera Tracking
* PostgreSQL Support
* Real-Time Analytics
* Dashboard Visualization
* Advanced Anomaly Detection
