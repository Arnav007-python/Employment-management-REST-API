from datetime import date

from app.models import Employee, EmployeeCreate, EmployeeUpdate, EmploymentStatus


class EmployeeRepository:
    def __init__(self) -> None:
        self._employees: dict[int, Employee] = {}
        self._next_id = 1
        self.seed()

    def seed(self) -> None:
        if self._employees:
            return

        sample_employees = [
            EmployeeCreate(
                first_name="Asha",
                last_name="Sharma",
                email="asha.sharma@example.com",
                department="Engineering",
                role="Backend Developer",
                salary=85000,
                hire_date=date(2025, 1, 15),
                status=EmploymentStatus.active,
            ),
            EmployeeCreate(
                first_name="Rahul",
                last_name="Mehta",
                email="rahul.mehta@example.com",
                department="Human Resources",
                role="HR Manager",
                salary=76000,
                hire_date=date(2024, 8, 1),
                status=EmploymentStatus.active,
            ),
        ]

        for employee in sample_employees:
            self.create(employee)

    def list(
        self,
        *,
        department: str | None = None,
        status: EmploymentStatus | None = None,
        search: str | None = None,
    ) -> list[Employee]:
        employees = list(self._employees.values())

        if department:
            employees = [
                employee
                for employee in employees
                if employee.department.lower() == department.lower()
            ]

        if status:
            employees = [employee for employee in employees if employee.status == status]

        if search:
            needle = search.lower()
            employees = [
                employee
                for employee in employees
                if needle in employee.first_name.lower()
                or needle in employee.last_name.lower()
                or needle in employee.email.lower()
                or needle in employee.role.lower()
            ]

        return employees

    def get(self, employee_id: int) -> Employee | None:
        return self._employees.get(employee_id)

    def get_by_email(self, email: str) -> Employee | None:
        return next(
            (
                employee
                for employee in self._employees.values()
                if employee.email.lower() == email.lower()
            ),
            None,
        )

    def create(self, payload: EmployeeCreate) -> Employee:
        employee = Employee(id=self._next_id, **payload.model_dump())
        self._employees[employee.id] = employee
        self._next_id += 1
        return employee

    def update(self, employee_id: int, payload: EmployeeUpdate) -> Employee | None:
        current = self.get(employee_id)
        if current is None:
            return None

        updated_data = current.model_dump()
        updated_data.update(payload.model_dump(exclude_unset=True))
        employee = Employee(**updated_data)
        self._employees[employee_id] = employee
        return employee

    def delete(self, employee_id: int) -> bool:
        if employee_id not in self._employees:
            return False

        del self._employees[employee_id]
        return True
