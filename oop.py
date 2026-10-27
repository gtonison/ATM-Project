class Bank_Account:
    def __init__(self, account_name, balance):
        self.account_name = account_name
        self.balance = balance
    
    def Deposit(self, amount):
        self.balance += amount
        print("Deposited successfully:", amount)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print("Withdrawal successful:", amount)
        
    def check_balance(self):
        print("Balance:", self.balance)


account = Bank_Account("Goodluck", 90000000)

account.Deposit(10000)
account.withdraw(10000)
account.check_balance()
