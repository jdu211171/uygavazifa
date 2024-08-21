class Product:
    def __init__(self, name, price, year_create):
        self.name = name
        self.price = price
        self.year_create = year_create


class License_Product(Product):
    def __init__(self, name, price, year_create, date_price):
        super().__init__(name, price, year_create)
        self.date_price = date_price

    def __str__(self):
        return f"{self.name} {self.price} {self.year_create} {self.date_price}"

    def passed_time(self):
        return self.date_price - self.year_create


products = [License_Product("Windows", 100, 2020, 2041),
            License_Product("Office", 50, 2021, 2032),
            License_Product("Adobe", 200, 2019, 2027)]

for product in products:
    print(product.passed_time())
