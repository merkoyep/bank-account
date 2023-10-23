import random

class BankAccount:

    def __init__(self, full_name, account_type="checking", account_number=random.randint(10000000, 99999999)):
        self.full_name = full_name
        self.account_type = account_type
        self.account_number = account_number
        self.balance = 0
    def deposit(self, amount):
        self.balance += amount
        print(f'Amount deposited: ${amount} new balance: ${self.balance}')
    
    def withdraw(self, amount):
        if amount > self.balance:
            print(f'Insufficient funds. Overdraft fee: $10.00')
            self.balance -= (amount + 10)
            self.balance = round(self.balance, 2)
            print(f'Amount withdrawn: ${amount} new balance: ${self.balance}')
        else:
            self.balance -= amount
            self.balance = round(self.balance, 2)
            print(f'Amount withdrawn: ${amount} new balance: ${self.balance}')

    def get_balance(self):
        print(f'Balance: ${self.balance}')
        return self.balance
    
    def add_interest(self):
        print(self.balance)
        if self.account_type == 'savings':
            interest = round((self.balance * 0.01), 2)
            self.balance += interest
            print(self.balance)
        else:
            interest = round((self.balance * 0.00083), 2)
            self.balance += interest
            print(self.balance)

    def print_statement(self):
        print(f'{self.full_name}\nAccount No.: ****{str(self.account_number)[-4:]}\nBalance: ${self.balance}')


#Example 1
marco = BankAccount("Marco Yip")
# marco.deposit(100)
# marco.withdraw(50)
# marco.add_interest()
# marco.print_statement()


#Example 2
joi = BankAccount("Joy Anderson")
# joi.withdraw(50)
# joi.add_interest()
# joi.print_statement()

#Example 3
mike = BankAccount("Mike Lee")
# mike.deposit(200)
# mike.withdraw(100)
# mike.get_balance()
# mike.add_interest()
# mike.print_statement()

#Example code for Mitchell
mitchell = BankAccount("Mitchell Hudson", 3141592)
# mitchell.deposit(400)
# mitchell.print_statement()
# mitchell.add_interest()
# mitchell.print_statement()
# mitchell.withdraw(150)
# mitchell.print_statement()

#add savings account
ben = BankAccount("Ben Joe")
# ben.deposit(1000)
# ben.add_interest()
# ben.print_statement()

amy = BankAccount("Amy Joe", "savings")
# amy.deposit(1000)
# amy.add_interest()
# amy.print_statement()

bank = [marco, joi, mike, mitchell, ben, amy]

def adding_interest():
    for account in bank:
        account.add_interest()
adding_interest()