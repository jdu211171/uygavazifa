class Employee:

    def __init__(self, name: str, salary: float) -> None:
        self.name = name
        self.salary = salary

    def get_details(self) -> str:
        return f'name: {self.name}, salary: {self.salary}'

    def calculate_bonus(self) -> float:
        return 0.0


class Manager(Employee):

    def __init__(self, name: str, salary: float, department: str) -> None:
        super().__init__(name, salary)
        self.department = department

    def get_details(self) -> str:
        return super().get_details() + f', departmant: {self.department}\n'

    def calculate_bonus(self) -> float:
        return self.salary * .1


class Developer(Employee):

    def __init__(self, name: str, salary: float, programming_language: str) -> None:
        super().__init__(name, salary)
        self.programming_language = programming_language

    def get_details(self) -> str:
        return super().get_details() + f', programming language: {self.programming_language}\n'

    def calculate_bonus(self) -> float:
        return self.salary * .5


manager = Manager(name="Alice", salary=120000, department="Sales")
developer = Developer(name="Bob", salary=100000, programming_language="Python")
print(manager.get_details())
print(developer.get_details())
print(manager.calculate_bonus())
print(developer.calculate_bonus())
