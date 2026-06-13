from datetime import date
from enum import Enum

from pydantic import BaseModel, EmailStr, Field


class EmploymentStatus(str, Enum):
    active = "active"
    inactive = "inactive"
    terminated = "terminated"


class EmployeeBase(BaseModel):
    first_name: str = Field(..., min_length=1, max_length=50, examples=["Asha"])
    last_name: str = Field(..., min_length=1, max_length=50, examples=["Sharma"])
    email: EmailStr = Field(..., examples=["asha.sharma@example.com"])
    department: str = Field(..., min_length=1, max_length=80, examples=["Engineering"])
    role: str = Field(..., min_length=1, max_length=80, examples=["Backend Developer"])
    salary: float = Field(..., ge=0, examples=[85000])
    hire_date: date = Field(..., examples=["2025-01-15"])
    status: EmploymentStatus = EmploymentStatus.active


class EmployeeCreate(EmployeeBase):
    pass


class EmployeeUpdate(BaseModel):
    first_name: str | None = Field(default=None, min_length=1, max_length=50)
    last_name: str | None = Field(default=None, min_length=1, max_length=50)
    email: EmailStr | None = None
    department: str | None = Field(default=None, min_length=1, max_length=80)
    role: str | None = Field(default=None, min_length=1, max_length=80)
    salary: float | None = Field(default=None, ge=0)
    hire_date: date | None = None
    status: EmploymentStatus | None = None


class Employee(EmployeeBase):
    id: int


class HealthResponse(BaseModel):
    status: str
    service: str
    version: str
