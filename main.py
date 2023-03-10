# Создать класс Person у которого есть свойство класса Wallet (кошелек).
# Создать класс Pay с методом оплаты с аргументом объекта Person и суммой покупки.
# При недостаточном количестве средств в кошельке его значение не меняется и выводится соответствующее сообщение.
# Если средств достаточно, то эта сумма списывается с кошелька пользователя.

class Person:
    def __init__(self, wallet = '') -> None:
        self.__wallet = wallet

    # def setwallet(self, value):
    #     print('setwallet')
    #     self.__wallet = value

    # def getwallet(self):
    #     print('setwallet')
    #     return self.__wallet
    # wallet = property(getwallet, setwallet)

    @property
    def wallet(self):
        return self.__wallet
    
    @wallet.setter
    def wallet(self, value):
        self.__wallet = value

p1 = Person() 
# p1.setwallet(10)
# p1.getwallet()
p1.wallet = 100
# print(p1.wallet)


class Pay:
    wallet = Person()
    def __init__(self, money_pay) -> None:
        self.money_pay = money_pay

    def pay(self):
        if self.wallet >= self.money_pay:
            return self.wallet - self.money_pay
        else:
            print("Не достаточно средств в кошельке")

p1 = Pay(100)
p1.wallet = 500
print(f"Остаток в кошельке: {p1.pay()} $")
p1.wallet = 50
print(p1.pay())