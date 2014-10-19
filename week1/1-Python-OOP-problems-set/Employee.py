class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def getName(self):
        return self.name

    def weeklyPay(self, hours):
        return self.salary * hours

class HourlyEmployee(Employee):

    def __init__(self, name, salary):
        super().__init__(name, salary)


#self.hours = hours
class SalariedEmployee(Employee):

    def __init__(self, name, salary):
        super().__init__(name, salary)


class Manager(SalariedEmployee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

staff = []
staff.append(HourlyEmployee("Morgan, Harry", 30.0))
staff.append(SalariedEmployee("Lin, Sally", 52000.0))
staff.append(Manager("Smith, Mary", 104000.0, 50.0))
for employee in staff :
    hours = int(input("Hours worked by " + employee.getName() + ": "))
    pay = employee.weeklyPay(hours)
    print("Salary: %.2f" % pay)
