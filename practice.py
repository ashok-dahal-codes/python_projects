# Create Account class with 2 attributes - balance & account no.
# Create methods for debit, credit & printing the balance
class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def debit(self, amount):
        self.balance -= amount
        print(f"the amount debited was {amount} ")
        print("the reamining is",self.remaining_balance())
    def credit(self, amount):
        self.balance += amount
        print(f"the amount credited was {amount}")
        print(f"the remainig amount is {self.remaining_balance()}")
    def remaining_balance(self):
        return self.balance
    
acc1 = Account(10000, 1223131)
acc1.debit(200)
acc1.credit(100)
