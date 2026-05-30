import requests

event = {
    "event_id": "EVT900",
    "store_id": "STORE_BLR_002",
    "camera_id": "CAM_ENTRY_01",
    "visitor_id": "VIS900",
    "event_type": "ENTRY",
    "timestamp": "2026-05-30T12:00:00Z",
    "zone_id": "SKINCARE",
    "dwell_ms": 3000,
    "is_staff": False,
    "confidence": 0.95
}

response = requests.post(
    "http://127.0.0.1:8000/events/ingest",
    json=[event]
)

print(response.status_code)
print(response.json())