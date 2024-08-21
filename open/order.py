from dataclasses import dataclass, field
from enum import Enum
from typing import List


class OrderStatus(Enum):
    OPEN = "open"
    PAID = "paid"


@dataclass
class LineItem:
    name: str
    price: int
    quantity: int = 1

    @property
    def total(self) -> int:
        return self.price * self.quantity


@dataclass
class Order:
    order_id: int
    status: OrderStatus = OrderStatus.OPEN
    line_items: List[LineItem] = field(default_factory=list)

    @property
    def total(self) -> int:
        return sum(item.total for item in self.line_items)

    def pay(self):
        self.status = OrderStatus.PAID

    def add_item(self, item: LineItem):
        self.line_items.append(item)


def luhn_checksum(card_number: str) -> bool:
    def digits_of(n: str) -> List[int]:
        return [int(digit) for digit in str(n)]

    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(str(d * 2)))
    return checksum % 10 == 0
