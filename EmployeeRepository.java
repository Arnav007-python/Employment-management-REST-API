
package com.example.employees.repository;
import com.example.employees.entity.Employee;
import org.springframework.data.jpa.repository.*;
public interface EmployeeRepository extends JpaRepository<Employee,Long>{}
