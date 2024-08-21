#
# class Book:
#
#     def __init__(self, name: str, author: str, price: float, genre: str, page: int):
#         self.name = name
#         self.author = author
#         self.price = price
#         self.genre = genre
#         self.page = page
#
#     def get_full_info(self) -> dict:
#         return {'name': self.name, 'author': self.author, 'price': self.price, 'genre': self.genre, 'page': self.page}
#
#     def change_price(self, new_price: float) -> None:
#         self.price = new_price
#

class Employee:

    def __init__(self, ID: int, first_name: str, last_name: str, salary: int):
        self.ID = ID
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def get_ID(self) -> int:
        return self.ID

    def get_first_name(self) -> str:
        return self.first_name

    def get_last_name(self) -> str:
        return self.last_name

    def get_name(self) -> str:
        return ''.join([self.first_name, self.last_name])

    def get_salary(self) -> int:
        return self.salary

    def set_salary(self, new_salary: int):
        self.salary = new_salary

    def get_annual_salary(self) -> int:
        return self.salary * 12

    def raise_salary(self, percent: int) -> int:
        self.salary *= (100 + percent)
        return self.salary

    def to_string(self):
        return (f'Employee['
                f'id: {self.get_ID()}, '
                f'name: {self.get_name()}, '
                f'salary: {self.get_salary()}]')