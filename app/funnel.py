from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Event

router = APIRouter()


@router.get("/stores/{store_id}/funnel")
def get_funnel(
    store_id: str,
    db: Session = Depends(get_db)
):

    entry_count = (
        db.query(Event)
        .filter(
            Event.store_id == store_id,
            Event.event_type == "ENTRY"
        )
        .count()
    )

    zone_count = (
        db.query(Event.visitor_id)
        .filter(
            Event.store_id == store_id,
            Event.event_type == "ZONE_ENTER"
        )
        .distinct()
        .count()
    )

    queue_count = (
        db.query(Event.visitor_id)
        .filter(
            Event.store_id == store_id,
            Event.event_type == "BILLING_QUEUE_JOIN"
        )
        .distinct()
        .count()
    )

    purchase_count = (
        db.query(Event.visitor_id)
        .filter(
            Event.store_id == store_id,
            Event.event_type == "PURCHASE"
        )
        .distinct()
        .count()
    )

    return {
        "entry": entry_count,
        "zone_visit": zone_count,
        "billing_queue": queue_count,
        "purchase": purchase_count
    }