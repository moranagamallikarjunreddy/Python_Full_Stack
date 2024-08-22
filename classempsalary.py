class Department:
    def __init__(self, department_id, department_name, min_salary, max_salary):
        self.department_id = department_id
        self.department_name = department_name
        self.min_salary = min_salary
        self.max_salary = max_salary

class Employee:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.department = None
        self.salary = 0

class Company:
    def __init__(self):
        self.departments = {}
        self.employees = {}

    def add_department(self, department_id, department_name, min_salary, max_salary):
        if department_id in self.departments:
            print(f"Department ID {department_id} already exists.")
            return
        self.departments[department_id] = Department(department_id, department_name, min_salary, max_salary)
        print(f"Added Department: {department_name}")

    def add_employee(self, employee_id, name):
        if employee_id in self.employees:
            print(f"Employee ID {employee_id} already exists.")
            return
        self.employees[employee_id] = Employee(employee_id, name)
        print(f"Added Employee: {name}")

    def assign_employee_to_department(self, employee_id, department_id, salary):
        if employee_id not in self.employees:
            print(f"Employee ID {employee_id} does not exist.")
            return
        if department_id not in self.departments:
            print(f"Department ID {department_id} does not exist.")
            return
        department = self.departments[department_id]
        if not (department.min_salary <= salary <= department.max_salary):
            print(f"Salary {salary} is out of bounds for the {department.department_name} department.")
            return
        employee = self.employees[employee_id]
        employee.department = department
        employee.salary = salary
        print(f"Assigned {employee.name} to {department.department_name} with salary {salary}")

# Example usage
company = Company()

# Adding departments
company.add_department(1, "IT", 10000, 150000)
company.add_department(2, "Admin", 8000, 50000)

# Adding employees
company.add_employee(101, "Ameet")
company.add_employee(102, "Naga")

# Assigning employees to departments with a salary
company.assign_employee_to_department(101, 2, 30000)  # Ameet to Admin with salary 30000
company.assign_employee_to_department(102, 1, 120000)  # Naga to IT with salary 120000
