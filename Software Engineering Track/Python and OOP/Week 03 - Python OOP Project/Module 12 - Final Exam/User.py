from rich.console import Console
import inquirer
import pwinput
import random
from beautifultable import BeautifulTable
from datetime import datetime

# Rich library "console" object
console = Console()

class User:
    def __init__(self, allUserVault:list) -> None:
    
        self.allUserVault = allUserVault # [{userName:key, [password, email:str, address:str, account_type, account_number]:value}]
        
        self.currentUserVault:dict = {}
        # A user can have multiple accounts
        self.current_user_accounts = []
        self.__balance = 0
        self.account_number = None
        self.loan_ask_time = 2
        self.user_loan = 0
        
        # * Auth options 
        self.auth_options = [
            "Login existing account",
            "Create new account"
        ]

        # * transactional history 
        self.transaction_history = [] # list of tuple [(time_when_transaction_was_made, transaction_type,  amount_of_transaction)]

        # * Table for displaying user data table
        self.current_user_bank_details = BeautifulTable()
        self.current_user_bank_details.columns.header = ["Name", "Password", "Email", "Address", "Account Type", "Account Number"]
        self.current_user_bank_details.set_style((BeautifulTable.STYLE_BOX_DOUBLED))

        # * List of user accounts details table 
        self.user_accounts_tables = []
        
        # * Table for display user transaction history table
        self.current_uesr_transaction_history = BeautifulTable()
        self.current_uesr_transaction_history.columns.header = ["Transaction Time", "Type of Transaction", "Amount"]

    # * User -> (3)
    def generate_account_number(self, name, mail, address, account_type):

        special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?~" 
        make_random_acnt_number = account_type[0] + str(random.randint(10, 299)) + random.choice(special_chars)
        for i in range (5):
            make_random_acnt_number += random.choice(mail)
            make_random_acnt_number += random.choice(name)
            make_random_acnt_number += random.choice(address)

        return make_random_acnt_number

    # & This class supervise all user deposite, withdraw and error regarding it
    # * User -> (4)
    def financialTransactions(self):

        while True:
            transactionOptions = [
                "Deposite money",
                "Withdraw money", 
                "Check previous transaction history", 
                "Loan",
                "Transfer Money",
                "Exit application"
            ]
            userOptions = [inquirer.List('transactionOptions', message="I would like to", choices = transactionOptions)]
            answers = inquirer.prompt(userOptions)
            selectedOption = answers['transactionOptions']

            current_transaction = ()

            if selectedOption == transactionOptions[0]:
                deposite_amount = float(input("Enter deposite amount: "))
                self.__balance += deposite_amount

                # * Collecting deposite history 
                transaction_time = datetime.now().isoformat()
                current_transaction = (transaction_time, selectedOption, deposite_amount)
                self.transaction_history.append(current_transaction)
                self.current_uesr_transaction_history.rows.append([transaction_time, selectedOption, str(deposite_amount) + " Taka"])

                # * Display currently happened transaction in table
                console.print(f"[bold green]Your transaction transcript is below")
                print(self.current_uesr_transaction_history)

                console.print(f"[bold green]After deposite your total balance: {self.__balance} taka[/]")

            elif selectedOption == transactionOptions[1]:

                withdrawal_amount = float(input("Enter withdraw amount: "))
                if self.__balance >= withdrawal_amount:

                    self.__balance -= withdrawal_amount

                    # * Collecting withdrawal history 
                    transaction_time = datetime.now().isoformat()
                    current_transaction = (transaction_time, selectedOption, withdrawal_amount)
                    self.transaction_history.append(current_transaction)
                    self.current_uesr_transaction_history.rows.append([transaction_time, selectedOption, str(withdrawal_amount) + " Taka"])

                    # * Display currently happened transaction in table
                    console.print(f"[bold green]Your transaction transcript is below")
                    print(self.current_uesr_transaction_history)

                    console.print(f"[yellow]You have withdrawn amount: {withdrawal_amount} taka\nCurrent balance: {self.__balance}")
                else:
                    console.print(f"[bold red underline]Withdrawal amount exceeded")

            elif selectedOption == transactionOptions[2]:
                self.check_transaction_history()
                
            elif selectedOption == transactionOptions[3]:
                self.take_loan()

            else:
                print(f"Exiting the application")
                exit()

    # ~ User -> (4)
    def available_balance(self):
        return f"Your current available balance is: {self.__balance}"

    # * User -> (5)
    def check_transaction_history(self):

        if not self.transaction_history:
            print(f"You've no transaction record")
        else:

            # ? Have error
            for transaction in self.transaction_history:
                for details in transaction:
                    print(f"{details[0]}\t{details[1]}\t{details[2]}")
                print("")

    # * User -> (1)
    def userAuth(self):

        isSuccessfulAuthentication: bool = False

        generalUserOptions = [
            "Login existing account",
            "Create new account"
        ]
        userOptions = [inquirer.List('generalUserOptions', message="Choice", choices = generalUserOptions)]
        answers = inquirer.prompt(userOptions)
        generalUserSelectedOption = answers['generalUserOptions']

        # * For user log in
        if generalUserSelectedOption == generalUserOptions[0]:
            userName = input(f"Enter User Name: ")
            userPassword = pwinput.pwinput("Enter User Password: ")

            for item in self.allUserVault:
                for key, value in item.items():
                    if key == userName and value[0] == userPassword:
                        isSuccessfulAuthentication = True
                        break

            if isSuccessfulAuthentication == True:
                console.print(f"[green underline]Authentication successful!!\nWelcome {userName}\n[/]")
                self.financialTransactions()
            else:
                console.print(f"[bold red underline]False credentials, no such user exist\n[/]")

        # * For user sign up or creating new account
        elif generalUserSelectedOption == generalUserOptions[1]:
            
            # list for storing pass, email, address, account_type
            userAccountDetails = []

            userName = input(f"Enter User Name: ")
            for item in self.allUserVault:
                while userName in item:
                    print(f"The username is taken, try another")
                    userName = input(f"Enter another username: ")
            
            userPassword = pwinput.pwinput("Enter User Password: ")
            userAccountDetails.append(userPassword)

            userEmail = input("Enter your email: ")
            userAccountDetails.append(userEmail)

            userAddress = input("Enter your address: ")
            userAccountDetails.append(userAddress)

            # * Choose account type
            console.print(f"[bold green]Enter your suitable account type[/]")
            account_type_options = [
                "Savings account",
                "Current account"
            ]
            userOptions = [inquirer.List('account_type_options', message="I want to create: ", choices = account_type_options)]
            userPick = inquirer.prompt(userOptions)
            generalUserSelectedOption = userPick['account_type_options']
            userAccountDetails.append(generalUserSelectedOption)

            # generate account number and store to the list
            self.account_number = self.generate_account_number(userName, userEmail, userAddress, generalUserSelectedOption)
            userAccountDetails.append(self.account_number)

            # storing new user data to the dictionary
            self.currentUserVault[userName] = userAccountDetails

            # collecting all user details in a tuple to show in a table
            self.current_user_bank_details.rows.append([userName, "●●●●●", userEmail, userAddress, generalUserSelectedOption, self.account_number])
            
            # Store account details table in list 
            self.user_accounts_tables.append(self.current_user_bank_details)
            
            # Display account details in table 
            print(self.current_user_bank_details)

            # ! Now store new current user to the allUserVault
            self.allUserVault.append(self.currentUserVault)
            isSuccessfulAuthentication = True

            self.current_user_accounts.append(self.currentUserVault)

            console.print(f"[bold yellow]\nThanks for choosing us for your service {userName}\n[/]")

            if isSuccessfulAuthentication == True:
                self.financialTransactions()

    # * User -> (6)
    def take_loan(self):

        if self.loan_ask_time >= 1:
            loan_amount = float(input("Enter the amount you ask for loan: "))
            console.print(f"[bold yellow]Loan granted[/]")

            self.__balance += loan_amount
            self.user_loan += loan_amount
            self.loan_ask_time -= 1
            
            # TODO: Loan transaction history
            
        else:
            print(f"Loan limit exceed")

    # * User -> (7)
    def money_transfer(self):
        pass

    def displayUserDetails(self):
        if self.current_user_accounts.size() >= 1:
            print(f"The user has {len(self.current_user_accounts) + 1} accounts")
            for i in range(len(self.user_accounts_tables)):
                print("Account {i + 1} details\n--------------------------")
                print(self.current_user_bank_details)
        else:
            print("No accounts created")

