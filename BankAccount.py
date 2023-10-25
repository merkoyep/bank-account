import random

class BankAccount:
    '''BankAccount is a class that contains the name of the account holder, type of account, account number and balance. 
    The associated methods allow for the depositing and withdrawal of funds, as well as displaying account information and adding
    interest.'''
    def __init__(self, full_name, account_type="checking", account_number=random.randint(10000000, 99999999), balance=0):
        '''Instantiates the BankAccount Class'''
        self.full_name = full_name
        self.account_type = account_type
        self.account_number = str(account_number)
        self.balance = balance
    def deposit(self, amount):
        '''takes a number and adds the value to the account.'''
        self.balance += amount
        print(f'Amount deposited: ${amount} new balance: ${self.balance}')
    
    def withdraw(self, amount):
        '''takes a number and subtracts the number from the balance. If the balance is less than the amount,
        an additional $10 is removed from the balance, and a warning message will be displayed.'''
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
        '''displays the balance of the account to the user'''
        print(f'Balance: ${self.balance}')
        return self.balance
    
    def add_interest(self):
        '''adds interest to the account balance depending on the account type'''
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
        '''displays account information including name, last 4 digits of the account number, and the balance to the user'''
        print(f'{self.full_name}\nAccount No.: ****{str(self.account_number)[-4:]}\nBalance: ${self.balance}')

# Instantiated examples of BankAccount. Please uncomment lines to see working examples.
#Example 1
marco = BankAccount("Marco Yip", account_number=12345678, balance=100)
# marco.deposit(100)
# marco.withdraw(50)
# marco.add_interest()
# marco.print_statement()


#Example 2
joi = BankAccount("Joy Anderson", account_number=87654321, balance=200)
# joi.withdraw(50)
# joi.add_interest()
# joi.print_statement()

#Example 3
mike = BankAccount("Mike Lee", balance=300)
# mike.deposit(200)
# mike.withdraw(100)
# mike.get_balance()
# mike.add_interest()
# mike.print_statement()

#Example code for Mitchell
mitchell = BankAccount("Mitchell Hudson", account_number=13141592, balance = 400)
# mitchell.deposit(400)
# mitchell.print_statement()
# mitchell.add_interest()
# mitchell.print_statement()
# mitchell.withdraw(150)
# mitchell.print_statement()


ben = BankAccount("Ben Joe", balance = 100)
# ben.deposit(1000)
# ben.add_interest()
# ben.print_statement()

amy = BankAccount("Amy Joe", "savings", balance = 300)
# amy.deposit(1000)
# amy.add_interest()
# amy.print_statement()
