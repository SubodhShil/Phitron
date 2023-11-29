from rich.console import Console
from rich.pretty import pprint
import inquirer
import pwinput
import shutil
import secrets
from beautifultable import BeautifulTable
from datetime import datetime

# ^ Admin Name: Subodh, Password: admin

# Rich library "console" object
console = Console()

class Bank:

    def main_menu():

        console.print(f"[bold green underline]Welcome to Royal Earth Bank")
        console.print(f"[bold yellow]\nSelect your user type")

        authOptions = [
            "Admin",
            "User",
            "Employee",
            "Exit Application"
        ]

        allUserOptions = [inquirer.List('authOptions', message = "Choice: ", choices=authOptions)]
        answers = inquirer.prompt(allUserOptions)
        allUserSelectedOption = answers['authOptions']

        while True:

            # * Manager-Admin Authentication
            if allUserSelectedOption == authOptions[0]:
                
                adminName = input(f"Enter Admin Name: ")
                adminPassword = pwinput.pwinput("Enter Admin Password: ")

                if bank_manager.isAdmin(adminName, adminPassword):
                    console.print(f"[bold green]\nWelcome Manager {adminName}[/]")
                    bank_manager.admin_privileges()
                else:
                    exit_application(1)

            # * User Authentication
            elif allUserSelectedOption == authOptions[1]:
                bank_user.user_menu()

            elif allUserSelectedOption == authOptions[2]:
                print(f"Not implemented yet")
                return

            else:
                console.print(f"[bold red]Thanks for using our bank, see you soon!![/]")
                exit()

# ** Admin class 
class Admin:

    def __init__(self) -> None:

        self.options = [
            "User menu",
            "Delete User Account",
            "See All User Accounts",
            "Available Bank Reserve",
            "Loan Feature Toggle",
            "Back to main menu",
            "Exit Application"
        ]

        # & Admin details
        self.name = "Subodh"
        self.password = "admin"

        # ^ User bank details -> stores user accounts
        # * structure (array of array): [ [userName, password, email, address, account_type, account_number, total_balance] ]
        self.all_user_vault = []

        # ^ Bank reserve: Assuming the bank has 1M taka initially 
        self.bank_total_reserve_balance = 0

        self.is_loan_active = True

        self.is_bankrupt = False

        self.maximum_loan_ask_time = 2
        
        self.total_loan_amount_grant = 0

    def isAdmin(self, name: str, password: str):
    
        if self.name == name and self.password == password:
            return True
        else:
            return False

    def admin_options(self):

        admin_options = [inquirer.List("options", message="Choice: ", choices = self.options)]
        answers = inquirer.prompt(admin_options)
        admin_selected_option = answers["options"]

        return admin_selected_option

    def admin_privileges(self):

        while True:
            current_selected_option = self.admin_options()

            if current_selected_option == self.options[0]:
                self.create_account()

            elif current_selected_option == self.options[1]:
                self.delete_user_account()

            elif current_selected_option == self.options[2]:
                self.see_all_user_accounts()

            elif current_selected_option == self.options[3]:
                self.see_bank_reserve()

            elif current_selected_option == self.options[4]:
                self.loan_amount_granted()
                
            elif current_selected_option == self.options[5]:
                Bank.main_menu()

            else:
                exit_application()

    # * Admin option -> 1
    def create_account(self):
        
        # Admin can create an account just like a general user
        bank_user.user_menu()

    # * Admin option -> 2
    def delete_user_account(self):

        if len(self.all_user_vault) == 0:
            print(f"Can't delete account, currently there are 0 account.")
            return

        target_account_name = input("Enter account name you want to delete: ")
        target_account_number = input("Enter account number: ")
        flag = False

        for item in self.all_user_vault:
            if target_account_name == item[0] and target_account_number == item[5]:
                print(f"Details found: {item}")
                self.all_user_vault.remove(item)
                flag = True
                break

        if flag == True:
            console.print(f"[red bold]Account found, deleting.\nCurrently have {len(self.all_user_vault)} users\n[/]")
        else:
            print("No such account found")


    # * Admin option -> 3
    def see_all_user_accounts(self):
        console.print(f"Currently there are {len(self.all_user_vault)} accounts")

        for index, value in enumerate(self.all_user_vault):
            console.print(f"[bold yellow]User {index + 1} 👉\t{value}[/]")

        print("")

    # * Admin option -> 4
    def see_bank_reserve(self):
        print(f"Bank total reserve is: {self.bank_total_reserve_balance} taka")

    # * Admin option -> 5
    def loan_amount_granted(self):
        print(f"Bank provided loan: {self.total_loan_amount_grant} taka")
        
    # * Admin option -> 6
    def loan_on_off(self):
        print(f"Enter digit 1 to turn on and digit 0 turn off loan feature")
        decision = int(input("Enter digit: "))
        if decision == 0:
            self.is_loan_active = False
        elif decision == 1:
            self.is_loan_active = True
        else:
            console.print("[red]Wrong input\n[/]")


# ** User class
class User:
    def __init__(self) -> None:

        # A user can have multiple accounts
        self.current_user_accounts = []
        self.__balance = 0
        self.account_number = None

        self.loan_ask_time = 2
        self.user_loan = 0

        # * current user transactional history 
        self.transaction_history = [] # list of tuple [(time_when_transaction_was_made, transaction_type,  amount_of_transaction)]

        # * Auth options 
        self.auth_options = [
            "Login existing account",
            "Create new account", 
            "Back to main menu",
            "Exit application"
        ]

        # * Transactional options
        self.transaction_options = [
            "Deposite money",
            "Withdraw money", 
            "Check previous transaction history", 
            "Loan",
            "Transfer Money",
            "Check your bank balance",
            "Back to user menu", 
            "Exit application"
        ]

        # * Bank account type
        self.account_type_options = [
            "Savings account",
            "Current account"
        ]

        # * Table for displaying user data table
        self.current_user_bank_details = BeautifulTable()
        self.current_user_bank_details.columns.header = ["Name", "Password", "Email", "Address", "Account Type", "Account Number", "Balance"]
        self.current_user_bank_details.set_style((BeautifulTable.STYLE_BOX_DOUBLED))

        # * List of user accounts details table 
        self.user_accounts_tables = []
        
        # * Table for display user transaction history table
        self.current_uesr_transaction_history = BeautifulTable()
        self.current_uesr_transaction_history.columns.header = ["Transaction Time", "Type of Transaction", "Amount"]


    def user_options(self, option_list:list):
        
        receive_option_list = option_list
        user_options = [inquirer.List("receive_option_list", message="Choice: ", choices = receive_option_list)]
        answers = inquirer.prompt(user_options)
        user_selected_option = answers["receive_option_list"]

        return user_selected_option


    # * User -> (1)
    def user_menu(self):
        console.print(f"[bold orchid]\nWelcome to the User Menu[/]")
        isSuccessfulAuthentication: bool = False

        auth_selected_option = self.user_options(self.auth_options)

        # * For user log in
        if auth_selected_option == self.auth_options[0]:
            user_name = input(f"Enter User Name: ")
            userPassword = pwinput.pwinput("Enter User Password: ")

            for item in bank_manager.all_user_vault:
                if user_name == item[0] and userPassword == item[1]:
                    isSuccessfulAuthentication = True
                    break

            if isSuccessfulAuthentication == True:
                console.print(f"[green underline]Authentication successful!!\nWelcome {user_name}\n[/]")
                self.financial_transactions()
            else:
                console.print(f"[bold red underline]False credentials, no such user exist\n[/]")
                Bank.main_menu()

        # * For user sign up or creating new account
        elif auth_selected_option == self.auth_options[1]:

            # list for storing user_name, pass, email, address, account_type, account_number
            current_user_account_details = []

            user_name = input(f"Enter User Name: ")
            for item in bank_manager.all_user_vault:
                while user_name == item[0]:
                    print(f"The username is taken, try another")
                    user_name = input(f"Enter another username: ")
            current_user_account_details.append(user_name)

            userPassword = pwinput.pwinput("Enter User Password: ")
            current_user_account_details.append(userPassword)

            user_email = input("Enter your email: ")
            current_user_account_details.append(user_email)

            user_address = input("Enter your address: ")
            current_user_account_details.append(user_address)

            # * Choose account type
            console.print(f"[bold green]\nEnter your suitable account type[/]")
            
            account_type_selected_option = self.user_options(self.account_type_options)
            current_user_account_details.append(account_type_selected_option)

            self.account_number = secrets.token_hex(5)
            current_user_account_details.append(self.account_number)
            
            # deposite money
            while True:
                new_account_deposite_money = float(input("Deposite money to create account (not less than 1000 taka): "))
                if new_account_deposite_money >= 1000.0:
                    self.__balance += new_account_deposite_money
                    current_user_account_details.append(self.__balance)
                    break

            # collecting all user details in a tuple to show in a table
            self.current_user_bank_details.rows.append([user_name, "●●●●●", user_email, user_address, account_type_selected_option, self.account_number, self.__balance])
        
            # Store account details table in list 
            self.user_accounts_tables.append(self.current_user_bank_details)

            # Display account details in table 
            print(self.current_user_bank_details)

            # ! Now store new current user to the all_user_vault
            bank_manager.all_user_vault.append(current_user_account_details)
            isSuccessfulAuthentication = True

            self.current_user_accounts.append(current_user_account_details)

            console.print(f"[bold yellow]\nThanks for choosing us for your service {user_name}\n[/]")

            if isSuccessfulAuthentication == True:
                self.financial_transactions()

        elif auth_selected_option == self.auth_options[2]:
            Bank.main_menu()

        else:
            exit_application()

    # & This method supervise all user deposite, withdraw and error regarding it
    def financial_transactions(self):

        while True:
            
            selected_transaction_option = self.user_options(self.transaction_options)

            current_transaction = ()

            if selected_transaction_option == self.transaction_options[0]:

                deposite_amount = float(input("Enter deposite amount: "))
                # * adding deposite money to bank total revenue 
                bank_manager.bank_total_reserve_balance += deposite_amount
                self.__balance += deposite_amount

                # * Collecting deposite history 
                transaction_time = datetime.now().isoformat()
                current_transaction = (transaction_time, selected_transaction_option, deposite_amount)
                self.transaction_history.append(current_transaction)
                self.current_uesr_transaction_history.rows.append([transaction_time, selected_transaction_option, str(deposite_amount) + " Taka"])

                # * Display currently happened transaction in table
                console.print(f"[bold green]Your transaction transcript is below")
                print(self.current_uesr_transaction_history)

                console.print(f"[bold green]After deposite your total balance: {self.__balance} taka\n[/]")

            elif selected_transaction_option == self.transaction_options[1]:
                
                if bank_manager.is_bankrupt == True:
                    print(center_text("The bank is bankrupt, now sieged by BD Police, you'll be refunded your money soon"))
                    return 
                
                withdrawal_amount = float(input("Enter withdraw amount: "))
                if self.__balance >= withdrawal_amount:

                    self.__balance -= withdrawal_amount
                    bank_manager.bank_total_reserve_balance -= withdrawal_amount

                    # * Collecting withdrawal history 
                    transaction_time = datetime.now().isoformat()
                    current_transaction = (transaction_time, selected_transaction_option, withdrawal_amount)
                    self.transaction_history.append(current_transaction)
                    self.current_uesr_transaction_history.rows.append([transaction_time, selected_transaction_option, str(withdrawal_amount) + " Taka"])

                    # * Display currently happened transaction in table
                    console.print(f"[bold green]Your transaction transcript is below")
                    print(self.current_uesr_transaction_history)

                    console.print(f"[yellow]You have withdrawn amount: {withdrawal_amount} taka\nCurrent balance: {self.__balance}")
                else:
                    console.print(f"[bold red underline]Your current balance is: {self.__balance} taka, You can't withdraw {withdrawal_amount} taka\n[/]")

            elif selected_transaction_option == self.transaction_options[2]:
                self.check_transaction_history()

            elif selected_transaction_option == self.transaction_options[3]:
                self.take_loan()

            # Transfer money
            elif selected_transaction_option == self.transaction_options[4]:
                self.money_transfer()
            
            # Check available balance 
            elif selected_transaction_option == self.transaction_options[5]:
                self.available_balance()

            # Back to user menu
            elif selected_transaction_option == self.transaction_options[6]:
                self.user_menu()
            
            else:
                exit_application(0)


    # * User -> (4)
    def available_balance(self):
        console.print(f"[bold yellow]Your current available balance is: {self.__balance}[/]")

    # * User -> (5)
    def check_transaction_history(self):
        if not self.transaction_history:
            print(f"You've no transaction record")
        else:
            # ? Have error
            for transaction in self.transaction_history:
                for details in transaction:
                    if isinstance(details, (list, tuple)):
                        print(f"{details[0]}\t{details[1]}\t{details[2]}")
                    else:
                        print(details)
                print("")


    # * User -> (6)
    def take_loan(self):

        if bank_manager.is_loan_active == True and self.loan_ask_time >= 1:
            loan_amount = float(input("Enter the amount you ask for loan: "))
            console.print(f"[bold yellow]Loan granted[/]")

            if bank_manager.bank_total_reserve_balance < loan_amount:

                self.__balance += loan_amount
                self.user_loan += loan_amount
                self.loan_ask_time -= 1
                bank_manager.total_loan_amount_grant += loan_amount

            # TODO: Loan transaction history
            
        else:
            print(f"Loan limit exceed")


    # * User -> (7)
    def money_transfer(self):
        receiver_name = input("Enter receiver account name: ")
        receiver_account_number = input("Enter receiver account number: ")

        for item in bank_manager.all_user_vault:
                if receiver_name == item[0] and receiver_account_number == item[5]:
                    console.print(f"[bold green]\nMoney transfer successful!![/]")
                else:
                    print(f"You don't have sufficient amount to send money")
                    self.user_options(self.transaction_options)

        console.print("[bold red]Account does not exist[/]")
        self.user_options(self.transaction_options)

    def displayUserDetails(self):

        if self.current_user_accounts.size() >= 1:
            print(f"The user has {len(self.current_user_accounts) + 1} accounts")
            for i in range(len(self.user_accounts_tables)):
                print("Account {i + 1} details\n--------------------------")
                print(self.current_user_bank_details)
        else:
            print("No accounts created")


# ** Bank admin object
bank_manager = Admin()

# ** Bank user
bank_user = User()

def center_text(text):
    terminal_width, _ = shutil.get_terminal_size()
    padding = (terminal_width - len(text)) // 2
    centered_text = f"{' ' * padding}{text}{' ' * padding}"
    return centered_text

def exit_application(is_wrong_credentials:bool):
    if is_wrong_credentials:
        console.print(f"[bold red underline]\nWrong credentials input[/]")

    print(center_text("Exiting the application\n"))
    exit()

def main():
    Bank.main_menu()

if __name__ == '__main__':
    main()