from typing import List


class Book:

    def __init__(self, name: str, page_count: int, price: float):
        self.name = name
        self.page_count = page_count
        self.price = price

    def increase_page_count(self):
        self.page_count += 10

    def decrease_price(self):
        self.increase_page_count()
        if self.page_count > 100:
            self.price /= 2


book_collection: List[Book] = []
for i in range(5):
    name = input('Enter book name: ')
    page_count = int(input('Enter book page count: '))
    price = float(input('Enter bookprice: '))
    book_collection.append(Book(name, page_count, price))

for book in book_collection:
    print(f"Book Name: {book.name}, Page Count: {book.page_count}, Price: ${book.price.__ceil__()}")

for book in book_collection:
    book.decrease_price()

for book in book_collection:
    print(f"Book Name: {book.name}, Page Count: {book.page_count}, Price: ${book.price.__ceil__()}")
