from BankAccount import BankAccount
import random

# Instantiated examples of BankAccount. Please uncomment lines to see working examples.
marco = BankAccount("Marco Yip", account_number=12345678, balance=100)
joi = BankAccount("Joy Anderson", account_number=87654321, balance=200)
mike = BankAccount("Mike Lee", balance=300)
mitchell = BankAccount("Mitchell Hudson", account_number=13141592, balance = 400)
ben = BankAccount("Ben Joe", balance = 100)
amy = BankAccount("Amy Joe", "savings", balance = 300)

#Stretch Challenges
# 2. Create list called bank and new function outside class that adds interest to each item in list of accounts
bank = [marco, joi, mike, mitchell, ben, amy]

#Create adding interest function loop
def adding_interest():
    '''iterates through the list of accounts and adds the appropriate interest to each account'''
    for account in bank:
        account.add_interest()

#Helper functions for application
def find_account(account_number):
    '''returns account belonging to given account number if the account exists. Otherwise an error message will appear'''
    for account in bank:
        if account.account_number == account_number:
            return account
    return False

def another_transaction(account):
    '''takes an account as an argument and will run transaction if user inputs y, or end program if user inputs n.'''
    again_input = input('Would you like to make another selection? (Y/N): ')
    if again_input.lower() == "y":
        transaction(account)
    elif again_input.lower() == "n":
        print (f'Thank you for banking with us {account.full_name}, see you next time!')
        return
    else:
        print('Please try again.')
        another_transaction(account)

def transaction(account):
    '''takes an account as an argument and will call print_statemet, deposit, withdraw or exit application depending on user input.'''
    transaction_input = input('Please make a selection: 1)Statement, 2)Deposit, 3)Withdraw, 4)Exit: ')
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
    elif transaction_input == '4':
        print (f'Thank you for banking with us {account.full_name}, see you next time!')
        return
    else:
        print('Please enter a valid selection from 1-4.')
        transaction(account)

def new_account():
    '''Takes user input to create a new BankAccount that is added to bank account list'''
    new_full_name = input('Please enter your full name: ')
    new_account_type = int(input('What type of account would you like? 1)Checking, 2)Savings: '))
    if new_account_type == 1:
        new_account_type = "checking"
    elif new_account_type == 2:
        new_account_type = "savings"
    else:
        print('Entry error, please try again.')
        new_account()
    new_balance = float(input('Please deposit a starting balance for your account: '))
    new_account_number = random.randint(10000000, 99999999)
    print(f'Welcome {new_full_name}! Your account with the number {new_account_number} has been created! Please login now.')
    return BankAccount(new_full_name, new_account_type, account_number=new_account_number, balance=new_balance)

def application():
    '''this main application function will receive user input to navigate through banking transactions.
    This function is recursive and will continue to run until a user chooses to exit using one of many base cases.'''
    welcome_input = int(input('Please make a selection: 1)Create account, 2) Login, 3) Exit'))
    if welcome_input == 1:
        bank.append(new_account())
        application()
    elif welcome_input == 2:
        login_input = input('Please enter your account number: ')
        if find_account(login_input):
            account = find_account(login_input)
            print(f'Welcome {account.full_name}.')
            transaction(account)
        else:
            print('Invalid Entry. Please try again.')
            application()
    elif welcome_input == 3:
        print('Thank you and come again!')
        return
    else:
        print('Invalid Entry, please try again.')
        application()
        
##Main function call
print('Welcome to the bank!')
application()



