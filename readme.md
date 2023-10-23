Bank Account 🏦
Description
Using object-oriented programming concepts, your task is to create a Python program that simulates a bank account.

Requirements
Submission Requirements:
    []Your submitted code should be in a new (public) repo on Github.
    []Your respository should have a minimum of 5 commits.
    []Your repository should include a README with the name of your project and a description.
    []Submit the link to your repo on Gradescope.
Assignment Requirements:
Your job is to create a Class that defines a bank account. It should define:
    [x]the owners name, 
    [x]account number, 
    [x]and balance as attributes.

Your BankAccount class should also define methods that perform common banking activities like 
    []deposit, 
    []withdraw, and 
    []get statement.

Follow the steps below:

[x]Your Python program should be created in one file called BankAccount.py.
    [x]Define a BankAccount class.
[x]A bank account should have the following attributes:
    [x]full_name - the full name of the bank account account owner.
    [x]account_number - randomly generated 8 digit number, unique per account.
    [x]balance - the balance of money in the account, should start at 0.
[]Then define the following methods for the BankAccount class:
    [x]The deposit method will take one parameter amount and will add amount to the balance. 
        [x]Also, it will print the message: “Amount deposited: $X.XX new balance: $Y.YY”

    [x]The withdraw method will take one parameter amount and will subtract amount from the balance. Also, 
        [x]it will print a message, like “Amount withdrawn: $X.XX new balance: $Y.YY”. 
        [x]If the user tries to withdraw an amount that is greater than the current balance, print ”Insufficient funds.” 
            []and charge them with an overdraft fee of $10

    [x]The get_balance method will print a user-friendly message with the account balance and 
        [x]then also return the current balance of the account.

    [x]The add_interest method adds interest to the users balance. 
        [x]The annual interest rate is 1% (i.e. 0.083% per month). Thus, the monthly interest is calculated by the following equation: interest = balance *  0.00083 .
    [x]The print_statement method prints a message with 
        [x]the account name, 
        [x]account number, and 
        [x]balance like this:
            Joi Anderson
            Account No.: ****5678
            Balance: $100.00

[x]Outside of the BankAccount class, define 3 different bank account examples using the BankAccount() object.
    [x]Your examples should show you using the different methods above to demonstrate them working.
[x]Include example code to do the following:
    [x]Create a new bank account instance: user: "Mitchell", account number: 03141592.
    [x]Deposit $400,000 into "Mitchell's" account.
    [x]Print a statement
    [x]Add interest to the account
    [x]Print a statement
    [x]Make a withdrawl of $150 (Mitchell needs some Yeezy's)
    [x]Print a statement

Stretch Challenges (Optional)
[]Add an attribute to set the account type: checking or savings.
[]A savings account gets 1.2% insterest (that's 1% per month)
[]Create a checking and a savings account
[]Add interest to each account
[]Print a statement for each account
[]Create a list called: bank. Add all of your accounts to bank. Write a function that loops over all accounts in the list and calls the add_interst method of each.
[]Create an "application". Use a loop to prompt us for an action. Actions can be:
    []Create account
    []Prompt for name, number, and balance.
    []Statement - prompts for the account number and prints the statement for that account.
    []Deposit - prompts for account number and amount. Then makes a deposit.
    []Withdraw - prompts for account number and amount. Then makes a withdrawl
    []Create a Bank class. This class will store a list of BackAccounts. It should implement the following methods:
    []create_account() - creates a new account.
    []deposit() - deposits an amount into an account with an account number
    []withdraw() - removes an amount from an account with an account number
    []transfer() - withdraws an amount from an account with an account number and deposits the same amount to an account with another number.
    []statement() - prints an statement for an account with an account number.