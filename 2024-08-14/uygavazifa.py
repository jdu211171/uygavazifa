import re


class BankAccount:

    def __init__(self, balance: float, owner_name: str, owner_id: int, owner_phone_number: str):
        self.__balance = balance
        self.__owner_name = owner_name
        self.__owner_id = owner_id
        self.__owner_phone_number = owner_phone_number
        self.__payment_history = list()

    def get_account_info(self):
        return (f'{self.get_balance()}\n'
                f'{self.get_owner_name()}\n'
                f'{self.get_owner_id()}\n'
                f'{self.get_owner_phone_number()}\n'
                f'{self.get_payment_history()}\n')

    def get_payment_history(self):
        return f'payment history: {self.__payment_history}'

    def get_owner_id(self):
        return f'owner id: {self.__owner_id}'

    def get_owner_name(self):
        return f'owner name: {self.__owner_name}'

    def get_balance(self):
        return f'balance: {self.__balance}'

    def get_owner_phone_number(self):
        return f'phone number: {self.__owner_phone_number}'

    def set_owner_name(self, new_name: str):
        if not isinstance(new_name, str):
            raise NameError('name should be string')
        self.__owner_name = new_name

    def set_owner_phone_number(self, new_number: str):
        pattern = r'^998(33|55|77|89|90|93|94|99)\d{5}$'
        match = re.match(pattern, new_number)
        if match:
            self.__owner_phone_number = new_number
        else:
            raise ValueError('please enter valid number')

    def add_to_balance(self, amount: float):
        if amount > 0 and isinstance(amount, float):
            self.__balance += amount
        else:
            raise ValueError('please enter valid amount of money')

    def widthdraw_balance(self, amount: float):
        if self.__balance - amount > 0 and isinstance(amount, float):
            return True
        return False

    def transfer_money(self, account: 'BankAccount', amount: float):
        if isinstance(account, BankAccount) and amount > 0:
            self.widthdraw_balance(amount)
            return account.add_to_balance(amount)
        raise AssertionError('Please check for amount of money or account name')
