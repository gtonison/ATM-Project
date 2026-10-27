class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def display_employee(self):
        print(self.name, self.position, self.salary)

    def increase(self, percentage):
        increase = self.salary * (percentage / 100)
        self.salary = increase + self.salary


employee1 = Employee("Rhema Abraham", "CTO of Pulse", 900000)
employee2 = Employee("Godgift", "Chief Production", 750000)
employee3 = Employee("Goodluck Tonison", "CEO of SafeCore", 1000000)