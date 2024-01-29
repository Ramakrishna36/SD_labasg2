class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def display(self):
        print(f"{self.emp_id}\t{self.name}\t{self.age}\t{self.salary}")


class EmployeeTable:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def display_table(self):
        print("Employee ID\tName\tAge\tSalary")
        for employee in self.employees:
            employee.display()

    def sort_table(self, sort_key):
        self.employees.sort(key=lambda x: getattr(x, sort_key))


def main():
    emp_table = EmployeeTable()

    emp_table.add_employee(Employee("161E90", "Ramu", 35, 59000))
    emp_table.add_employee(Employee("171E22", "Tejas", 30, 82100))
    emp_table.add_employee(Employee("171G55", "Abhi", 25, 100000))
    emp_table.add_employee(Employee("152K46", "Jaya", 32, 85000))

    print("Original Employee Table:")
    emp_table.display_table()

    print("\nChoose sorting parameter:")
    print("1. Age\n2. Name\n3. Salary")
    choice = int(input("Enter your choice (1/2/3): "))

    if choice == 1:
        sort_key = "age"
    elif choice == 2:
        sort_key = "name"
    elif choice == 3:
        sort_key = "salary"
    else:
        print("Invalid choice. Exiting.")
        return

    emp_table.sort_table(sort_key)

    print("\nSorted Employee Table:")
    emp_table.display_table()


if __name__ == "__main__":
    main()
