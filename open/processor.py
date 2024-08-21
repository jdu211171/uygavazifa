from datetime import datetime
from card import CreditCard


def validate_card(card: CreditCard) -> bool:
    if len(card.number) != 16:
        return False
    current_date = datetime.now()
    if current_date.year > card.expiry_year or \
            (current_date.year == card.expiry_year and current_date.month > card.expiry_month):
        return False
    return True


class PaymentProcessor:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def _check_api_key(self) -> bool:
        return self.api_key == "valid"

    def charge(self, card: CreditCard, amount: int) -> None:
        if not self._check_api_key():
            raise ValueError("Invalid API key")
        if not validate_card(card):
            raise ValueError("Invalid card")
        print(f"Charging {amount} to card {card.number}")
