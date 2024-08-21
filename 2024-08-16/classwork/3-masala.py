class Product:
    def __init__(self, name, price, manufacturer):
        self.name = name
        self.price = price
        self.manufacturer = manufacturer


class Market(Product):
    def __init__(self, name, price, manufacturer, created_date, product_sale):
        Product.__init__(self, name, price, manufacturer)
        self.created_date = created_date
        self.product_sale = product_sale

    def sale(self, date: int):
        if self.created_date > date:
            self.price *= self.product_sale


products = [Market('Apple', 1000, 'Apple Inc.', 2021, 0.9),
            Market('Samsung', 900, 'Samsung Inc.', 2020, 0.8),
            Market('Xiaomi', 800, 'Xiaomi Inc.', 2019, 0.7),
            Market('Huawei', 700, 'Huawei Inc.', 2018, 0.6),
            Market('Oppo', 600, 'Oppo Inc.', 2017, 0.5),
            Market('Vivo', 500, 'Vivo Inc.', 2016, 0.4),
            Market('OnePlus', 400, 'OnePlus Inc.', 2015, 0.3),]

for product in products:
    product.sale(2020)
    print(product.price)
