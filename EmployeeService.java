
package com.example.employees.service;
import com.example.employees.entity.Employee;
import com.example.employees.repository.EmployeeRepository;
import org.springframework.data.domain.*; import org.springframework.stereotype.Service;
@Service
public class EmployeeService{
 private final EmployeeRepository repo;
 public EmployeeService(EmployeeRepository repo){this.repo=repo;}
 public Page<Employee> getAll(int page,int size){return repo.findAll(PageRequest.of(page,size));}
 public Employee create(Employee e){return repo.save(e);}
}
