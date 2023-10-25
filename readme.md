# Bank Account 🏦

## Introduction

Project: Using object-oriented programming concepts, your task is to create a Python program that simulates a bank account.
I was able to complete the working code and add commented out examples in the BankAccount.py file. After this program ran and passed my tests, I proceeded to build a second version of the program with the bank.py file where the Bank class takes a list of bank accounts and is able to handle the same functionality. Finally, I created a third file called application.py that utilizes helper functions and methods from the BankAccount class to create a CLI program.

Since I ran out of time, I was unable to explore creating a CLI program usint O. This is something I hope to accomplish in the future.

## Instructions
### BankAccount.py
To run the program, please uncomment lines 55-93 to see examples left to showcase all working functions, then run the file.

### bank.py
See lines 53-60 for examples. Please comment them out and run the file in the terminal to see the program working.

### application.py
This program is setup recursively. To run the program, run the file and it will call line 100 of the file to begin the program. Read the instructions on the terminal and interact with the terminal. to exit out of the terminal, follow intsrutions on the screen, or ctrl+c to quit. The program will continue to run and work with new accounts that are created until the program stops.

## Requirements
### Submission Requirements:
    [x]Your submitted code should be in a new (public) repo on Github.
    [x]Your respository should have a minimum of 5 commits.
    [x]Your repository should include a README with the name of your project and a description.
    [x]Submit the link to your repo on Gradescope.
### Assignment Requirements:
Your job is to create a Class that defines a bank account. It should define:
    [x]the owners name, 
    [x]account number, 
    [x]and balance as attributes.

### Your BankAccount class should also define methods that perform common banking activities like 
    [x]deposit, 
    [x]withdraw, and 
    [x]get statement.

## Follow the steps below:

[x]Your Python program should be created in one file called BankAccount.py.
    [x]Define a BankAccount class.
[x]A bank account should have the following attributes:
    [x]full_name - the full name of the bank account account owner.
    [x]account_number - randomly generated 8 digit number, unique per account.
    [x]balance - the balance of money in the account, should start at 0.
[x]Then define the following methods for the BankAccount class:
    [x]The deposit method will take one parameter amount and will add amount to the balance. 
        [x]Also, it will print the message: “Amount deposited: $X.XX new balance: $Y.YY”

[x]The withdraw method will take one parameter amount and will subtract amount from the balance. Also, 
    [x]it will print a message, like “Amount withdrawn: $X.XX new balance: $Y.YY”. 
    [x]If the user tries to withdraw an amount that is greater than the current balance, print ”Insufficient funds.” 
        [x]and charge them with an overdraft fee of $10

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

## Stretch Challenges (Optional)
[x]Add an attribute to set the account type: checking or savings.
[x]A savings account gets 1.2% insterest (that's 1% per month)
[x]Create a checking and a savings account
[x]Add interest to each account
[x]Print a statement for each account
[x]Create a list called: bank. Add all of your accounts to bank. Write a function that loops over all accounts in the list and calls the add_interst method of each.
[x]Create an "application". Use a loop to prompt us for an action. Actions can be:
    [x]Create account
        [x]Prompt for name, number, and balance.
    [x]Statement - prompts for the account number and prints the statement for that account.
    [x]Deposit - prompts for account number and amount. Then makes a deposit.
    [x]Withdraw - prompts for account number and amount. Then makes a withdrawl

[x]Create a Bank class. This class will store a list of BackAccounts. It should implement the following methods:
    [x]create_account() - creates a new account.
    [x]deposit() - deposits an amount into an account with an account number
    [x]withdraw() - removes an amount from an account with an account number
    [x]transfer() - withdraws an amount from an account with an account number and deposits the same amount to an account with another number.
    [x]statement() - prints an statement for an account with an account number.
