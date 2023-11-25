from rich.console import Console
import inquirer
import pwinput
import random
from beautifultable import BeautifulTable

# Rich library "console" object
console = Console()

class User:
    def __init__(self, allUserVault:list) -> None:
        self.allUserVault = allUserVault # [{userName:key, [password, email:str, address:str, account_type, account_number]:value}]
        self.currentUserVault:dict = {}
        self.__balance = 0
        self.account_number = None
        
        # * Creating display table with "BeautifulTable" package
        self.current_user_bank_details = BeautifulTable()
        self.current_user_bank_details.columns.header = ["Name", "Password", "Email", "Address", "Account Type", "Account Number"]
        self.current_user_bank_details.set_style((BeautifulTable.STYLE_BOX_DOUBLED))

    def generate_account_number(self, name, mail, address, account_type):

        special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?~" 
        make_random_acnt_number = account_type[0] + str(random.randint(10, 299)) + random.choice(special_chars)
        for i in range (5):
            make_random_acnt_number += random.choice(mail)
            make_random_acnt_number += random.choice(name)
            make_random_acnt_number += random.choice(address)

        return make_random_acnt_number

    # ! This class supervise all user deposite, withdraw and error regarding it
    def financialTransactions(self):
        
        transactionOptions = [
            "Deposite money",
            "Withdraw money"
        ]
        userOptions = [inquirer.List('transactionOptions', message="I would like to: ", choices = transactionOptions)]
        answers = inquirer.prompt(userOptions)
        selectedOption = answers['transactionOptions']
        
        if selectedOption == transactionOptions[0]:
            deposite_amount = int(input("Enter deposite amount: "))
            self.__balance += deposite_amount
            console.print(f"[bold green]After deposite your total balance: {self.__balance} taka[/]")
        else:
            pass

    def userAuth(self):

        isSuccessfulAuthentication: bool = False
        generalUserOptions = [
            "Login existing account",
            "Create new account"
        ]
        userOptions = [inquirer.List('generalUserOptions', message="Choice: ", choices = generalUserOptions)]
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

            # ! Now store new current user to the allUserVault
            self.allUserVault.append(self.currentUserVault)
            isSuccessfulAuthentication = True

            console.print(f"[bold yellow]\nThanks for choosing us for your service {userName}\n[/]")

            self.displayUserDetails()

            if isSuccessfulAuthentication == True:
                self.financialTransactions()

    def displayUserDetails(self):
        print(self.current_user_bank_details)