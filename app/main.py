from typing import Annotated

from fastapi import FastAPI, HTTPException, Query, status

from app.config import settings
from app.models import (
    Employee,
    EmployeeCreate,
    EmployeeUpdate,
    EmploymentStatus,
    HealthResponse,
)
from app.repository import EmployeeRepository

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description=(
        "A REST API for managing employee records, departments, roles, "
        "and employment status."
    ),
)
repository = EmployeeRepository()


@app.get("/", tags=["Root"])
def root() -> dict[str, str]:
    return {
        "message": "Welcome to the Employment Management REST API",
        "docs": "/docs",
        "health": "/health",
    }


@app.get("/health", response_model=HealthResponse, tags=["Health"])
def health_check() -> HealthResponse:
    return HealthResponse(
        status="ok",
        service=settings.app_name,
        version=settings.app_version,
    )


@app.get("/employees", response_model=list[Employee], tags=["Employees"])
def list_employees(
    department: Annotated[
        str | None,
        Query(description="Filter by department"),
    ] = None,
    status_filter: Annotated[
        EmploymentStatus | None,
        Query(alias="status", description="Filter by employment status"),
    ] = None,
    search: Annotated[
        str | None,
        Query(min_length=1, description="Search employees"),
    ] = None,
) -> list[Employee]:
    return repository.list(department=department, status=status_filter, search=search)


@app.post(
    "/employees",
    response_model=Employee,
    status_code=status.HTTP_201_CREATED,
    tags=["Employees"],
)
def create_employee(payload: EmployeeCreate) -> Employee:
    if repository.get_by_email(payload.email):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="An employee with this email already exists.",
        )

    return repository.create(payload)


@app.get("/employees/{employee_id}", response_model=Employee, tags=["Employees"])
def get_employee(employee_id: int) -> Employee:
    employee = repository.get(employee_id)
    if employee is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found.")

    return employee


@app.patch("/employees/{employee_id}", response_model=Employee, tags=["Employees"])
def update_employee(employee_id: int, payload: EmployeeUpdate) -> Employee:
    current = repository.get(employee_id)
    if current is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found.")

    if payload.email and payload.email.lower() != current.email.lower():
        existing = repository.get_by_email(payload.email)
        if existing:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="An employee with this email already exists.",
            )

    employee = repository.update(employee_id, payload)
    if employee is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found.")

    return employee


@app.delete(
    "/employees/{employee_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Employees"],
)
def delete_employee(employee_id: int) -> None:
    deleted = repository.delete(employee_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found.")
