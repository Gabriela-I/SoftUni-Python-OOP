class Account:
    def __init__(self, id_account: int, balance: int, pin: int):
        self.__id = id_account
        self.balance = balance
        self.__pin = pin

    def get_id(self, pin):
        if pin == self.__pin:
            return self.__id
        return 'Wrong pin'

    def change_pin(self, old, new):
        if old == self.__pin:
            self.__pin = new
            return 'Pin changed'
        return 'Wrong pin'


account = Account(8827312, 100, 3421)

print(account.get_id(1111))

print(account.get_id(3421))

print(account.balance)

print(account.change_pin(2212, 4321))

print(account.change_pin(3421, 1234))
