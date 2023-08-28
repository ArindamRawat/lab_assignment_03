class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeTable:
    def __init__(self, employees):
        self.employees = employees

    def sort_by_age(self):
        self.employees.sort(key=lambda emp: emp.age)

    def sort_by_name(self):
        self.employees.sort(key=lambda emp: emp.name)

    def sort_by_salary(self):
        self.employees.sort(key=lambda emp: emp.salary)

    def print_table(self):
        print("{:<10} {:<10} {:<5} {:<10}".format("Emp ID", "Name", "Age", "Salary"))
        print("="*40)
        for emp in self.employees:
            print("{:<10} {:<10} {:<5} {:<10}".format(emp.emp_id, emp.name, emp.age, emp.salary))

if __name__ == "__main__":
    employees = [
        Employee("161E90", "Raman", 41, 56000),
        Employee("161F91", "Himadri", 38, 67500),
        Employee("161F99", "Jaya", 51, 82100),
        Employee("171E20", "Tejas", 30, 55000),
        Employee("171G30", "Ajay", 45, 44000)
    ]

    emp_table = EmployeeTable(employees)

    print("Employee Table:")
    emp_table.print_table()

    print("\nSort Employee Table:")
    print("1. Age")
    print("2. Name")
    print("3. Salary")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        emp_table.sort_by_age()
    elif choice == 2:
        emp_table.sort_by_name()
    elif choice == 3:
        emp_table.sort_by_salary()
    else:
        print("Invalid choice")

    print("\nSorted Employee Table:")
    emp_table.print_table()
