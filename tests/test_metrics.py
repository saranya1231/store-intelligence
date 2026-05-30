# PROMPT:
# Generate a FastAPI test for a metrics endpoint using pytest and TestClient.
# Verify that metrics are returned successfully for a given store.

# CHANGES MADE:
# Adapted the endpoint path to match the Store Intelligence API.
# Simplified validation to focus on successful API response.
# Updated test data to use an existing store identifier.



from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_metrics():

    response = client.get(
        "/stores/STORE_BLR_002/metrics"
    )

    assert response.status_code == 200