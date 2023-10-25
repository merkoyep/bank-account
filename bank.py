from BankAccount import BankAccount
class Bank:
    def __init__(self, list_of_accounts):
        """Instantiates with a list of BankAccounts"""
        self.accounts = list_of_accounts
    
    def deposit(self, amount, acc_number):
        '''takes an ammount and account number that will add the amount to the account. If the bank account is not entered, an error will throw.'''
        for account in self.accounts:
            if account.account_number == acc_number:
                account.balance += amount
                print(f'You have deposited {amount}. Your account balance is now {account.balance}')
                return
        return 'Error, invalid number.'
    
    def withdraw(self, amount, acc_number):
        '''Takes an ammount and an account number and will deduct the ammount from the balance of the given account. If account doesn't exit, an error with throw.'''
        for account in self.accounts:
            if account.account_number == acc_number:
                account.balance -= amount
                print(f'You have withdrwan ${amount}. Your balance is now {account.balance}')
        return 'Error, invalid number.'
    
    def transfer(self, amount, original_acc, transfer_acc):
        '''takes an ammount and two account numbers. This function will transfer the amount from the first account to the second.'''
        for account in self.accounts:
            if account.account_number == original_acc:
                account.balance -= amount
        for account in self.accounts:
            if account.account_number == transfer_acc:
                account.balance += amount
                print(f'You have transferred ${amount} to account #{transfer_acc}.')
                return
        return 'Error, invalid number.'     
      
    def statement(self, acc_number):
        '''takes an account number and will display account information to the user.'''
        for account in self.accounts:
            if account.account_number == acc_number:
                print(f'{account.full_name}\nAccount No.: ****{str(account.account_number)[-4:]}\nBalance: ${account.balance}')

    def create_account(self, full_name, account_number, account_type, balance):
        '''takes full name, accoutn number, account_type, and balance to create an account and append it to the list of bankaccounts.'''
        new_account = BankAccount(full_name, account_type, account_number=account_number, balance=balance)
        self.accounts.append(new_account)

# Instantiated examples of BankAccount. Please uncomment lines to see working examples.
marco = BankAccount("Marco Yip", account_number=12345678, balance=100)
joi = BankAccount("Joy Anderson", account_number=87654321, balance=200)
mike = BankAccount("Mike Lee", balance=300)
mitchell = BankAccount("Mitchell Hudson", account_number=13141592, balance = 400)
ben = BankAccount("Ben Joe", balance = 100)
amy = BankAccount("Amy Joe", "savings", balance = 300)
bank = [marco, joi, mike, mitchell, ben, amy]

# Instantiated Bank using above accounts.
banklist = Bank(bank)
#Please uncomment the following lines for working examples
# banklist.create_account("Suesan Varley", account_number=66666666, account_type='savings', balance=400)
# banklist.statement('66666666')
# banklist.deposit(100, '66666666')
# banklist.statement('66666666')
# banklist.withdraw(100, '12345678')
# banklist.statement('13141592')
# banklist.transfer(50, '12345678', '13141592')
# banklist.statement('13141592')

# banklist.statement('12345678')