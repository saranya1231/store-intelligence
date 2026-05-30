from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_ingest_event():

    payload = [
        {
            "event_id": "TEST1001",
            "store_id": "TEST_STORE",
            "camera_id": "CAM01",
            "visitor_id": "VIS01",
            "event_type": "ENTRY",
            "timestamp": "2026-05-30T10:00:00Z",
            "zone_id": "SKINCARE",
            "dwell_ms": 1000,
            "is_staff": False,
            "confidence": 0.95
        }
    ]

    response = client.post(
        "/events/ingest",
        json=payload
    )

    assert response.status_code == 200