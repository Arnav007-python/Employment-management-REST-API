
package com.example.employees.controller;
import com.example.employees.entity.Employee;
import com.example.employees.service.EmployeeService;
import org.springframework.data.domain.Page;
import org.springframework.web.bind.annotation.*;
@RestController
@RequestMapping("/api/employees")
public class EmployeeController{
 private final EmployeeService service;
 public EmployeeController(EmployeeService service){this.service=service;}
 @GetMapping
 public Page<Employee> all(@RequestParam(defaultValue="0") int page,@RequestParam(defaultValue="10") int size){
   return service.getAll(page,size);
 }
 @PostMapping
 public Employee create(@RequestBody Employee e){ return service.create(e);}
}
