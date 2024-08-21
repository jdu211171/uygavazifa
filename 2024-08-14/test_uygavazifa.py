import unittest
from uygavazifa import BankAccount


class TestBankAccount(unittest.TestCase):

    def test_balance_is_updated_after_adding_money(self):
        account = BankAccount(100.0, "John Doe", 123, "998991234567")
        account.add_to_balance(50.0)
        self.assertEqual(account.get_balance(), "balance: 150.0")

    def test_balance_is_not_updated_with_invalid_amount(self):
        account = BankAccount(100.0, "John Doe", 123, "998991234567")
        with self.assertRaises(ValueError):
            account.add_to_balance(-50.0)

    def test_phone_number_is_updated_with_valid_number(self):
        account = BankAccount(100.0, "John Doe", 123, "998991234567")
        account.set_owner_phone_number("998993456789")
        self.assertEqual(account.get_owner_phone_number(), "phone number: 998993456789")

    def test_phone_number_is_not_updated_with_invalid_number(self):
        account = BankAccount(100.0, "John Doe", 123, "998991234567")
        with self.assertRaises(ValueError):
            account.set_owner_phone_number("998123456789")

    def test_transfer_money_between_accounts(self):
        account1 = BankAccount(100.0, "John Doe", 123, "998991234567")
        account2 = BankAccount(50.0, "Jane Doe", 456, "998993456789")
        account1.transfer_money(account2, 30.0)
        self.assertEqual(account1.get_balance(), "balance: 70.0")
        self.assertEqual(account2.get_balance(), "balance: 80.0")

    def test_transfer_money_fails_with_invalid_amount(self):
        account1 = BankAccount(100.0, "John Doe", 123, "998991234567")
        account2 = BankAccount(50.0, "Jane Doe", 456, "998993456789")
        with self.assertRaises(AssertionError):
            account1.transfer_money(account2, -30.0)

    def test_transfer_money_fails_with_insufficient_balance(self):
        account1 = BankAccount(100.0, "John Doe", 123, "998991234567")
        account2 = BankAccount(50.0, "Jane Doe", 456, "998993456789")
        with self.assertRaises(AssertionError):
            account1.transfer_money(account2, 130.0)


if __name__ == '__main__':
    unittest.main()
