from fastapi import FastAPI

from app.database import engine
from app.models import Base

from app.ingestion import router as ingestion_router

from app.metrics import router as metrics_router

from app.funnel import router as funnel_router

from app.heatmap import router as heatmap_router

from app.anomalies import router as anomalies_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Store Intelligence API",
    version="1.0.0"
)

app.include_router(ingestion_router)
app.include_router(metrics_router)
app.include_router(funnel_router)
app.include_router(heatmap_router)
app.include_router(anomalies_router)

@app.get("/")
def root():
    return {
        "message": "Store Intelligence API Running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }