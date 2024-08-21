import random


class Employee:
    def __init__(self, surname: str, position: str, salary: float):
        self.surname = surname
        self.position = position
        self.salary = salary


class EnterpriseEmployee(Employee):
    def __init__(self, surname: str, position: str, salary: float, rating: int):
        super().__init__(surname, position, salary)
        self.rating = rating


def raise_salary(rating: int, salary: float):
    if 60 <= rating < 70:
        return salary * 1.2
    if 75 <= rating < 90:
        return salary * 1.4
    if 90 <= rating <= 100:
        return salary * 1.6
    return salary


employees = []

for i in range(20):
    surname = f"Surname{i + 1}"
    position = f"Position{i + 1}"
    salary = random.uniform(30000, 100000)
    rating = random.randint(1, 100)
    employee = EnterpriseEmployee(surname, position, salary, rating)
    employees.append(employee)

for emp in employees:
    print(f"Surname: {emp.surname}, Position: {emp.position}, Salary: {emp.salary:.2f}, Rating: {emp.rating}")

employees = list(
    map(lambda emp: EnterpriseEmployee(emp.surname, emp.position, raise_salary(emp.rating, emp.salary), emp.rating),
        employees))

for emp in employees:
    print(f"Surname: {emp.surname}, Position: {emp.position}, New Salary: {emp.salary:.2f}, Rating: {emp.rating}")
