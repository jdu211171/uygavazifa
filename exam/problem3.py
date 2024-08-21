from typing import List


class Market:

    def __init__(self, name: str, address: str) -> None:
        self.name = name
        self.address = address

        self.products: List[dict] = []
        self.balance = 0

    def get_products_info(self) -> str:
        info = ''
        for item in range(len(self.products)):
            for name in self.products[item]:
                info += f'{name} - {self.products[item][name]["price"]} so\'m, {self.products[item][name]["quantity"]} dona\n'
        return info

    def add_product(self, product: str, price: float, quantity: int) -> None:
        self.products.append({product: {'price': price, 'quantity': quantity}})

    def remove_product(self, product: str) -> None:
        for item in range(len(self.products)):
            for name in self.products[item]:
                if name == product:
                    self.products.pop(item)
                    return

    def add_money(self, amount: float) -> None:
        self.balance += amount

    def sell(self, product: str, quantity: int) -> None:
        for item in range(len(self.products)):
            for name in self.products[item]:
                if name == product:
                    if self.products[item][name]["quantity"] > quantity:
                        self.products[item][name]["quantity"] -= quantity
                        self.balance += self.products[item][name]["price"] * quantity
                    else:
                        print('Can\'t sell that much quantity')


bozor = Market(name="Supermarket", address="Toshkent, O'zbekiston")
bozor.add_product(product="Olma", price=5000, quantity=10)
bozor.add_product(product="Banan", price=7000, quantity=5)
print(bozor.get_products_info())
bozor.sell(product="Olma", quantity=3)
print(bozor.get_products_info())
bozor.remove_product(product="Banan")
print(bozor.get_products_info())
