from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database import get_db
from app.models import Event

router = APIRouter()


@router.get("/stores/{store_id}/heatmap")
def get_heatmap(
    store_id: str,
    db: Session = Depends(get_db)
):

    results = (
        db.query(
            Event.zone_id,
            func.count(Event.zone_id),
            func.avg(Event.dwell_ms)
        )
        .filter(Event.store_id == store_id)
        .group_by(Event.zone_id)
        .all()
    )

    response = []

    for zone_id, visit_count, avg_dwell in results:

        response.append(
            {
                "zone": zone_id,
                "visit_count": visit_count,
                "avg_dwell_ms": avg_dwell or 0
            }
        )

    return response