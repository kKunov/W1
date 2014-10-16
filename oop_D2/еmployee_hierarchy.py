class Employee:

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class HourlyEmployee(Employee):

    def __init__(self, name, wage_for_houre):
        super().__init__(name)
        self.wage_for_houre = wage_for_houre

    def weekly_pay(self, hours):
        if hours >= 40:
            return self.wage_for_houre * hours
        else:
            return "Not enought hours!!! Your solary is 0 LOSEEER!!!"


class SalariedEmployee(Employee):

    def __init__(self, name, weekly_wage):
        super().__init__(name)
        self.weekly_wage = weekly_wage

    def weekly_pay(self, hours):
        return self.weekly_wage


class Manager(SalariedEmployee):

    def __init__(self, name, weekly_wage, bonuses):
        super().__init__(name, weekly_wage)
        self.bonuses = bonuses

    def weekly_pay(self, hours):
        return self.weekly_wage + self.bonuses


staff = []
staff.append(HourlyEmployee("Morgan, Harry", 30.0))
staff.append(SalariedEmployee("Lin, Sally", 52000.0))
staff.append(Manager("Smith, Mary", 104000.0, 50.0))
for employee in staff:
    hours = int(input("Hours worked by " + employee.get_name() + ": "))
    pay = employee.weekly_pay(hours)
    print("Salary: %.2f" % pay)
