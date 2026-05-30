from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Event

router = APIRouter()


@router.get("/stores/{store_id}/anomalies")
def get_anomalies(
    store_id: str,
    db: Session = Depends(get_db)
):

    anomalies = []

    queue_count = (
        db.query(Event)
        .filter(
            Event.store_id == store_id,
            Event.event_type == "BILLING_QUEUE_JOIN"
        )
        .count()
    )

    if queue_count > 10:
        anomalies.append(
            {
                "severity": "WARN",
                "type": "QUEUE_SPIKE",
                "suggested_action": "Open additional billing counter"
            }
        )

    entry_count = (
        db.query(Event)
        .filter(
            Event.store_id == store_id,
            Event.event_type == "ENTRY"
        )
        .count()
    )

    purchase_count = (
        db.query(Event)
        .filter(
            Event.store_id == store_id,
            Event.event_type == "PURCHASE"
        )
        .count()
    )

    if entry_count > 0 and purchase_count == 0:

        anomalies.append(
            {
                "severity": "INFO",
                "type": "NO_PURCHASES",
                "suggested_action": "Check conversion funnel"
            }
        )

    return anomalies