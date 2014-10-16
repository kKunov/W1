class CashDesk:

    def __init__(self, money={100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}):
        self.money_types = [100, 50, 20, 10, 5, 2, 1]
        self.money = money

    def take_money(self, money):
        self.money = money

    def total(self):
        summ = 0
        for key in self.money:
            summ += key * self.money[key]
        return summ

    def can_withdraw_money(self, money):
        for key in self.money_types:
            if key in self.money:
                if money >= key and self.money[key] * key >= money:
                    self.money[key] -= money // key
                    money -= (money // key) * key
                elif money >= key and self.money[key] * key < money:
                    money -= self.money[key] * key
                    self.money[key] = 0
        if money > 0:
            return False
        else:
            return True


my_cash_desk = CashDesk()
my_cash_desk.take_money({1: 2, 50: 1, 20: 1})
print (my_cash_desk.total())  # 72
print(my_cash_desk.money)
print(my_cash_desk.can_withdraw_money(70))
