import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_dashboard_stats(client):
    res = client.get("/api/dashboard/stats")
    assert res.status_code == 200
    data = res.get_json()
    assert data["status"] == "success"
    assert "kpis" in data["data"]
    assert data["data"]["kpis"]["total_threat_actors"] >= 10
    assert data["data"]["kpis"]["infrastructure_indicators"] >= 10

def test_get_actors(client):
    res = client.get("/api/actors")
    assert res.status_code == 200
    data = res.get_json()
    assert data["status"] == "success"
    assert len(data["data"]) >= 10

def test_get_actor_detail(client):
    # Fetch first actor
    res_list = client.get("/api/actors")
    actors = res_list.get_json()["data"]
    first_id = actors[0]["id"]

    res = client.get(f"/api/actors/{first_id}")
    assert res.status_code == 200
    actor = res.get_json()["data"]
    assert actor["id"] == first_id

def test_get_actor_handles(client):
    res_list = client.get("/api/actors")
    actors = res_list.get_json()["data"]
    first_id = actors[0]["id"]

    res = client.get(f"/api/actors/{first_id}/handles")
    assert res.status_code == 200
    data = res.get_json()
    assert data["status"] == "success"

def test_get_infrastructure(client):
    res = client.get("/api/infrastructure")
    assert res.status_code == 200
    data = res.get_json()
    assert data["status"] == "success"
    assert len(data["data"]) >= 10

def test_get_sources(client):
    res = client.get("/api/sources")
    assert res.status_code == 200
    data = res.get_json()
    assert data["status"] == "success"
    assert len(data["data"]) >= 5

def test_export_json_and_csv(client):
    res_list = client.get("/api/actors")
    actors = res_list.get_json()["data"]
    first_id = actors[0]["id"]

    # Test JSON export
    res_json = client.get(f"/api/export/actor/{first_id}/json")
    assert res_json.status_code == 200
    assert "application/json" in res_json.content_type

    # Test CSV export
    res_csv = client.get(f"/api/export/actor/{first_id}/csv")
    assert res_csv.status_code == 200
    assert "text/csv" in res_csv.content_type
