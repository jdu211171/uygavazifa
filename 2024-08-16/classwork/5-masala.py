class Book:
    def __init__(self, name, page_count, price):
        self.name = name
        self.page_count = page_count
        self.price = price

    def average_page_price(self):
        return self.price / self.page_count

    def new_price(self):
        if 'programming' in self.name.lower():
            self.price *= 2


books = [Book('Python Programming', 500, 1000),
        Book('Java Programming', 600, 1200),
        Book('C Programming', 400, 800),
        Book('C++ Programming', 700, 1400),
        Book('JavaScript Programming', 300, 600),
        Book('HTML Programming', 200, 400)]

for book in books:
    book.new_price()
    print(f'{book.name} - {book.price} - {book.average_page_price()}')
