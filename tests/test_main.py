from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_check() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_list_employees() -> None:
    response = client.get("/employees")

    assert response.status_code == 200
    assert len(response.json()) >= 2


def test_create_get_update_and_delete_employee() -> None:
    payload = {
        "first_name": "Neha",
        "last_name": "Kapoor",
        "email": "neha.kapoor@example.com",
        "department": "Finance",
        "role": "Financial Analyst",
        "salary": 72000,
        "hire_date": "2025-03-10",
        "status": "active",
    }

    create_response = client.post("/employees", json=payload)
    assert create_response.status_code == 201
    employee = create_response.json()
    employee_id = employee["id"]

    get_response = client.get(f"/employees/{employee_id}")
    assert get_response.status_code == 200
    assert get_response.json()["email"] == payload["email"]

    update_response = client.patch(
        f"/employees/{employee_id}",
        json={"role": "Senior Financial Analyst", "salary": 81000},
    )
    assert update_response.status_code == 200
    assert update_response.json()["role"] == "Senior Financial Analyst"

    delete_response = client.delete(f"/employees/{employee_id}")
    assert delete_response.status_code == 204

    missing_response = client.get(f"/employees/{employee_id}")
    assert missing_response.status_code == 404


def test_duplicate_email_returns_conflict() -> None:
    payload = {
        "first_name": "Asha",
        "last_name": "Sharma",
        "email": "asha.sharma@example.com",
        "department": "Engineering",
        "role": "Backend Developer",
        "salary": 85000,
        "hire_date": "2025-01-15",
        "status": "active",
    }

    response = client.post("/employees", json=payload)

    assert response.status_code == 409


def test_filter_employees_by_department() -> None:
    response = client.get("/employees", params={"department": "Engineering"})

    assert response.status_code == 200
    assert all(employee["department"] == "Engineering" for employee in response.json())
