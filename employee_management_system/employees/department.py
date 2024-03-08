## Department class


class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee_id):
        for employee in self.employees:
            if employee.employee_id == employee_id:
                self.employees.remove(employee)
                return True
        return False

    def list_employees(self):
        print(f"Employees in Department {self.name}:")
        for employee in self.employees:
            print(f"- {employee}")

