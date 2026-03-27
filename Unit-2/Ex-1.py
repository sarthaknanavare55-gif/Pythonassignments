class BankAccount:
    def __init__(self,account_number,balance=0.0):
        self.account_number=account_number
        self.balance=balance
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"Deposited:Rs.{amount:.2f}")
        else:
            print(f"Deposit amount must be greater than zero.") 
    def withdraw(self,amount):
        if 0 < amount <= self.balance:
            self.balance-=amount
            print(f"Withdrawn:Rs.{amount:.2f}")
        elif amount > self.balance:
            print(f"Insufficient Balance!")
        else:
            print(f"Withdrawal amount must be greater than zero.")
    def check_balance(self):
        print(f"Account {self.account_number} Balance:Rs.{self.balance:.2f}") 

account=BankAccount("05023028571",10000.00)
account.check_balance()
account.deposit(50000)
account.withdraw(2000)
account.check_balance()