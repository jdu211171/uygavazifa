from typing import Protocol
from card import CreditCard
from order import Order


class PaymentProcessor(Protocol):
    def charge(self, card: CreditCard, amount: int) -> None:
        ...


def pay_order(
        order: Order, payment_processor: PaymentProcessor, card: CreditCard
) -> None:
    if order.total == 0:
        raise ValueError("No items in order")
    payment_processor.charge(card, order.total)
    order.pay()
