from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database import get_db
from app.models import Event

router = APIRouter()


@router.get("/stores/{store_id}/metrics")
def get_metrics(
    store_id: str,
    db: Session = Depends(get_db)
):

    unique_visitors = (
        db.query(Event.visitor_id)
        .filter(Event.store_id == store_id)
        .distinct()
        .count()
    )

    avg_dwell = (
        db.query(func.avg(Event.dwell_ms))
        .filter(Event.store_id == store_id)
        .scalar()
    )

    return {
        "store_id": store_id,
        "unique_visitors": unique_visitors,
        "avg_dwell_ms": avg_dwell or 0
    }