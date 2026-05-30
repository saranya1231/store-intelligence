from typing import List

from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Event
from app.schemas import EventCreate

router = APIRouter()


@router.post("/events/ingest")
def ingest_events(
    events: List[EventCreate],
    db: Session = Depends(get_db)
):

    processed = 0
    duplicates = 0
    failed = 0

    for event in events:

        existing_event = db.query(Event).filter(
            Event.event_id == event.event_id
        ).first()

        if existing_event:
            duplicates += 1
            continue

        try:
            new_event = Event(
                event_id=event.event_id,
                store_id=event.store_id,
                camera_id=event.camera_id,
                visitor_id=event.visitor_id,
                event_type=event.event_type,
                timestamp=event.timestamp,
                zone_id=event.zone_id,
                dwell_ms=event.dwell_ms,
                is_staff=event.is_staff,
                confidence=event.confidence
            )

            db.add(new_event)
            processed += 1

        except Exception:
            failed += 1

    db.commit()

    return {
        "processed": processed,
        "duplicates": duplicates,
        "failed": failed
    }