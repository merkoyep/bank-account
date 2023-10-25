import random
from bank import Bank

class BankAccount:

    def __init__(self, full_name, account_type="checking", account_number=random.randint(10000000, 99999999), balance=0):
        self.full_name = full_name
        self.account_type = account_type
        self.account_number = str(account_number)
        self.balance = balance
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

#add savings account
ben = BankAccount("Ben Joe", balance = 100)
# ben.deposit(1000)
# ben.add_interest()
# ben.print_statement()

amy = BankAccount("Amy Joe", "savings", balance = 300)
# amy.deposit(1000)
# amy.add_interest()
# amy.print_statement()

#Create bank
bank = [marco, joi, mike, mitchell, ben, amy]

#Create adding interest function loop
def adding_interest():
    for account in bank:
        account.add_interest()

def find_account(account_number):
    for account in bank:
        if account.account_number == account_number:
            return account
    return ('Error, no account exists.')

def another_transaction(account):
    again_input = input('Would you like to make another selection? (Y/N): ')
    if again_input.lower() == "y":
        transaction(account)
    elif again_input.lower() == "n":
        print ('Thank you, see you next time!')
        return
    else:
        print('Please try again.')
        another_transaction(account)

def transaction(account):
    transaction_input = input('Please make a selection: 1)Statement, 2)Deposit, 3)Withdraw: ')
    if transaction_input == '1':
        account.print_statement()
        another_transaction(account)
    elif transaction_input == '2':
        deposit_amount_input = int(input('Please enter your deposit amount: '))
        account.deposit(deposit_amount_input)
        another_transaction(account)
    elif transaction_input == '3':
        withdraw_amount_input = int(input('Please enter your deposit amount: '))
        account.withdraw(withdraw_amount_input)
        another_transaction(account)

def application():
    welcome_input = int(input('Please make a selection: 1)Create account, 2) Login'))
    if welcome_input == 1:
        new_full_name = input('Please enter your full name: ')
        new_account_type = int(input('What type of account would you like? 1)Checking, 2)Savings: '))
        if new_account_type == 1:
            new_account_type = "checking"
        elif new_account_type == 2:
            new_account_type = "savings"
        else:
            print('Entry error, please try again.')
            application()
        new_balance = float(input('Please deposit a starting balance for your account: '))
        new_account_number = random.randint(10000000, 99999999)
        new_account = BankAccount(new_full_name, new_account_type, account_number=new_account_number, balance=new_balance)
        bank.append(new_account)
        print(f'Welcome {new_full_name}! Your account with the number {new_account.account_number} has been created! Please login now.')
        application()
    elif welcome_input == 2:
        login_input = input('Please enter your account number: ')
        account = find_account(login_input)
        print(f'Welcome {account.full_name}.')
        transaction(account)
        

print('Welcome to the bank!') 
application()
