"""
Employee Management System offline script

This will be used for below operations:
- Add Department
- Remove Department
- Display Departments
- Add Employee to Department
- Remove Employee from Department
- List Employees in Department
- Save Data
- Load Data

08-03-2024 Aditya Shekhar  First Draft
"""

import json
from employees.employee import Employee
from employees.department import Department


class EmployeeManagementSystem:
    def __init__(self):
        self.company = {}
        self.load_data("data/company_data.json")

    def add_department(self, department_name):
        '''
        Method to add departments in the company
        '''
        if department_name not in self.company:
            self.company[department_name] = Department(department_name)
            print(f"Department '{department_name}' added successfully.")
        else:
            print(f"Department '{department_name}' already exists.")

    def remove_department(self, department_name):
        '''
        Method to remove the specified department from the company
        '''
        if department_name in self.company:
            del self.company[department_name]
            print(f"Department '{department_name}' removed successfully.")
        else:
            print(f"Department '{department_name}' does not exist.")

    def display_departments(self):
        '''
        Method to display the departments which are created/present.
        '''
        print("Departments:")
        for department_name, department in self.company.items():
            print(f"- {department_name}")

    def add_employee_to_department(self, employee_name, employee_id, title, department_name):
        '''
        Method to add employee to the specified department
        '''
        if department_name in self.company:
            employee = Employee(employee_name, employee_id, title, department_name)
            self.company[department_name].add_employee(employee)
            print(f"Employee '{employee_name}' added to department '{department_name}'.")
        else:
            print(f"Department '{department_name}' does not exist.")

    def remove_employee_from_department(self, employee_id, department_name):
        '''
        Method to remove existing employee from the department
        '''
        if department_name in self.company:
            if self.company[department_name].remove_employee(employee_id):
                print(f"Employee with ID '{employee_id}' removed from department '{department_name}'.")
            else:
                print(f"Employee with ID '{employee_id}' not found in department '{department_name}'.")
        else:
            print(f"Department '{department_name}' does not exist.")

    def list_employees_in_department(self, department_name):
        '''
        Method to list the employees for specified department
        '''
        if department_name in self.company:
            self.company[department_name].list_employees()
        else:
            print(f"Department '{department_name}' does not exist.")

    def save_data(self, filename):
        '''
        Method to save the data in company's json file after adding any
        '''
        with open(filename, 'w') as file:
            json.dump({dept_name: [str(emp) for emp in dept.employees] for dept_name, dept in self.company.items()}, file)
        print("Data saved successfully.")

    def load_data(self, filename):
        '''
        Method to load back the saved company data from company json file
        '''
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                for dept_name, employees in data.items():
                    department = Department(dept_name)
                    for emp_str in employees:
                        emp_name, emp_id = emp_str.split(" (ID: ")
                        emp_id = emp_id[:-1]
                        department.add_employee(Employee(emp_name, emp_id, "", dept_name))
                    self.company[dept_name] = department
            print("Data loaded successfully.")
        except FileNotFoundError:
            print("No saved data found.")


def print_menu():
    '''
    Menu to print all the available operations.
    '''
    print("\nEmployee Management System Menu:")
    print("1. Add Department")
    print("2. Remove Department")
    print("3. Display Departments")
    print("4. Add Employee to Department")
    print("5. Remove Employee from Department")
    print("6. List Employees in Department")
    print("7. Save Data")
    print("8. Load Data")
    print("9. Exit")


if __name__ == "__main__":
    emp_sys = EmployeeManagementSystem()
    filename = "data/company_data.json"
    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            department_name = input("Enter department name: ")
            emp_sys.add_department(department_name)
        elif choice == "2":
            department_name = input("Enter department name: ")
            emp_sys.remove_department(department_name)
        elif choice == "3":
            emp_sys.display_departments()
        elif choice == "4":
            employee_name = input("Enter employee name: ")
            employee_id = input("Enter employee ID: ")
            title = input("Enter employee title: ")
            department_name = input("Enter department name: ")
            emp_sys.add_employee_to_department(employee_name, employee_id, title, department_name)
        elif choice == "5":
            employee_id = input("Enter employee ID: ")
            department_name = input("Enter department name: ")
            emp_sys.remove_employee_from_department(employee_id, department_name)
        elif choice == "6":
            department_name = input("Enter department name: ")
            emp_sys.list_employees_in_department(department_name)
        elif choice == "7":
            emp_sys.save_data(filename)
        elif choice == "8":
            emp_sys.load_data(filename)
        elif choice == "9":
            break
        else:
            print("Invalid choice. Please choose again.")
