class CashDesk:

    def __init__(self):
        self.money = {}

    def take_money(self, cash):
        # take input  money from dictionary

        for key in cash:
         self.money[key] = cash[key]
        return self.money

    def total(self):
        #return money
        #self.money=_to_sum
        sum = 0
        for key in self.money:
            sum+= key * self.money[key]

        return sum



    def can_withdraw_money(self, amount_of_money):

        if amount_of_money >= self.total():
            return False
        else:
            return True





my_cash_desk = CashDesk()
my_cash_desk.take_money({1:2, 50:1, 20:1})
print(my_cash_desk.total()) # 72
print(my_cash_desk.can_withdraw_money(30)) #False
print(my_cash_desk.can_withdraw_money(70)) #True
