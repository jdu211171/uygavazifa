class Product:

    def __init__(self, name: str, price: float, produced_year: str) -> None:
        self.name = name
        self.price = price
        self.produced_year = produced_year


class Farm(Product):

    def __init__(self, name: str, price: float, produced_year: str, delivered_date: str) -> None:
        super().__init__(name, price, produced_year)
        self.delivered_date = delivered_date

    def delivered_period(self):
        produced = list(map(int, self.produced_year.split('-')))
        delivered = list(map(int, self.delivered_date.split('-')))

        year_diff = delivered[0] - produced[0]
        month_diff = delivered[1] - produced[1]
        day_diff = delivered[2] - produced[2]

        total_days = year_diff * 365 + month_diff * 30 + day_diff
        return total_days // 30


product1 = Farm('Apple', 1.5, '2024-07-15', '2024-08-16')
product2 = Farm('Banana', 2.5, '2024-05-13', '2024-08-16')
print(product1.delivered_period())
print(product2.delivered_period())
