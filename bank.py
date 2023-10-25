from BankAccount import BankAccount
class Bank:
    def __init__(self, list_of_accounts):
        self.accounts = list_of_accounts
    
    def deposit(self, amount, acc_number):
        for account in self.accounts:
            if account.account_number == acc_number:
                account.balance += amount
                return
        return 'Error, invalid number.'
    
    def withdraw(self, amount, acc_number):
        for account in self.accounts:
            if account.account_number == acc_number:
                account.balance -= amount
        return 'Error, invalid number.'
    def transfer(self, amount, original_acc, transfer_acc):
        for account in self.accounts:
            if account.account_number == original_acc:
                account.balance -= amount
        for account in self.accounts:
            if account.account_number == transfer_acc:
                account.balance += amount
                return
        return 'Error, invalid number.'       
    def statement(self, acc_number):
        for account in self.accounts:
            if account.account_number == acc_number:
                print(f'{account.full_name}\nAccount No.: ****{str(account.account_number)[-4:]}\nBalance: ${account.balance}')
    def create_account(self, full_name, account_type, balance):
        new_account = BankAccount(full_name, account_type, balance=balance)
        self.accounts.append(new_account)

