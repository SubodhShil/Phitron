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
                    console.print(f"[bold green]\nWelcome Manager {adminName}[/]\n")
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
                console.print(f"[bold red]Thanks for using our bank, see you soon!!\n[/]")
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
        
        self.current_user_flag = None

        # & Admin details
        self.name = "Subodh"
        self.password = "admin"

        # ^ User bank details -> stores user accounts
        # * structure (array of array): [ [userName, password, email, address, account_type, account_number, total_balance] ]
        self.all_user_vault = []

        # ^ Bank reserve: Assuming the bank has 1Koti taka initially 
        self.bank_total_reserve_balance = 10000000

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
                exit_application(0)

    # * Admin option -> 1
    def create_account(self):
        
        # Admin can create an account just like a general user
        bank_user.user_menu()

    # * Admin option -> 2
    def delete_user_account(self):

        if len(self.all_user_vault) == 0:
            console.print(f"[bold red]Can't delete account, currently there are 0 account.[/]")
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
        console.print(f"Currently there are {len(self.all_user_vault)} accounts\n")

        for index, value in enumerate(self.all_user_vault):
            if index == 7:
                break
            console.print(f"[bold yellow]User {index + 1} 👉\t{value}[/]\n")

        print("")

    # * Admin option -> 4
    def see_bank_reserve(self):
        console.print(f"[bold green]Bank total reserve is: {self.bank_total_reserve_balance} taka\n[/]")

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
        self.current_user_bank_details.columns.header = ["Name", "Password", "Email", "Address", "Account Type", "Account Number"]
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
            user_password = pwinput.pwinput("Enter User Password: ")

            for item in bank_manager.all_user_vault:
                if user_name == item[0] and user_password == item[1]:
                    isSuccessfulAuthentication = True
                    # ^ tracking the current user
                    bank_manager.current_user_flag = item[5]
                    break

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

            user_password = pwinput.pwinput("Enter User Password: ")
            current_user_account_details.append(user_password)

            user_email = input("Enter your email: ")
            current_user_account_details.append(user_email)

            user_address = input("Enter your address: ")
            current_user_account_details.append(user_address)

            # * Choose account type
            console.print(f"[bold green]\nEnter your suitable account type[/]")
            
            account_type_selected_option = self.user_options(self.account_type_options)
            current_user_account_details.append(account_type_selected_option)

            # ^ generate random account number for new user
            self.account_number = secrets.token_hex(5)

            # ^ current user
            bank_manager.current_user_flag = self.account_number
            current_user_account_details.append(self.account_number)

            # collecting all user details in a tuple to show in a table
            self.current_user_bank_details.rows.append([user_name, "●●●●●", user_email, user_address, account_type_selected_option, self.account_number])

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
                self.financial_transactions(self.account_number)

        elif auth_selected_option == self.auth_options[2]:
            Bank.main_menu()

        else:
            exit_application(0)

    # & This method supervise all user deposite, withdraw and error regarding it
    def financial_transactions(self, account_number):

        flag = False
        current_user = None
        current_user_index = None
        for index, item in enumerate(bank_manager.all_user_vault):
            if item[5] == account_number:
                current_user = bank_manager.all_user_vault[index]
                current_user_index = index
                flag = True
                break
        
        # ^ adding two more fields
        # * at index 6 for tracking balance 
        current_user.append(0)
        # * at index 7 for tracking history
        current_user.append([])

        if not flag:
            print("No such user exist")
            return

        while flag:
            selected_transaction_option = self.user_options(self.transaction_options)
            current_transaction = ()

            # ^ Deposite money
            if selected_transaction_option == self.transaction_options[0]:
                deposite_amount = float(input("Enter deposite amount: "))

                # * adding deposite money to bank total revenue and user account
                bank_manager.bank_total_reserve_balance += deposite_amount
                current_user[6] += deposite_amount

                # ! Collecting deposite history
                transaction_time = datetime.now().isoformat()
                current_transaction = (transaction_time, selected_transaction_option, deposite_amount)
                self.transaction_history.append(current_transaction)
                self.current_uesr_transaction_history.rows.append([transaction_time, selected_transaction_option, str(deposite_amount) + " Taka"])

                # * Adding history to main bank account to track later
                current_user[7].append(current_transaction)

                # * Display currently happened transaction in table
                console.print(f"[bold green]Your transaction transcript is below")
                print(self.current_uesr_transaction_history)

                console.print(f"[bold green]After deposite your total balance: {current_user[6]} taka\n[/]")

            # ^ Withdraw money
            elif selected_transaction_option == self.transaction_options[1]:
                
                if bank_manager.is_bankrupt == True:
                    print(center_text("The bank is bankrupt, now sieged by BD Police, you'll be refunded your money soon"))
                    return 

                withdrawal_amount = float(input("Enter withdraw amount: "))
                if current_user[6] >= withdrawal_amount:
                    bank_manager.bank_total_reserve_balance -= withdrawal_amount
                    current_user[6] -= withdrawal_amount

                    # * Collecting withdrawal history 
                    transaction_time = datetime.now().isoformat()
                    current_transaction = (transaction_time, selected_transaction_option, withdrawal_amount)
                    self.transaction_history.append(current_transaction)
                    self.current_uesr_transaction_history.rows.append([transaction_time, selected_transaction_option, str(withdrawal_amount) + " Taka"])

                    # * Adding history to main bank account to track later
                    if len(current_user) - 1 < 7:
                        current_user.append([])
                    current_user[7].append(current_transaction)

                    # * Display currently happened transaction in table
                    console.print(f"[bold green]Your transaction transcript is below[/]")
                    print(self.current_uesr_transaction_history)

                    console.print(f"[bold yellow]You have withdrawn amount: {withdrawal_amount} taka\nCurrent balance: {current_user[6]} taka\n[/]")
                else:
                    console.print(f"[bold red underline]Your current balance is: {current_user[6]} taka, You can't withdraw {withdrawal_amount} taka\n[/]")

            # ^ see history == done
            elif selected_transaction_option == self.transaction_options[2]:
                self.check_all_transaction_history(current_user_index)

            # ^ Taking loan from bank == done
            elif selected_transaction_option == self.transaction_options[3]:
                self.take_loan(current_user_index)

            # ^ Transfer money == done 
            elif selected_transaction_option == self.transaction_options[4]:
                self.money_transfer(current_user_index)

            # ^ Check available balance == done
            elif selected_transaction_option == self.transaction_options[5]:
                self.available_balance(current_user_index)

            # ^ Back to user menu
            elif selected_transaction_option == self.transaction_options[6]:
                self.user_menu()
            
            else:
                exit_application(0)


    # * User -> (4)
    def available_balance(self, current_user_index):
        current_user = bank_manager.all_user_vault[current_user_index]
        console.print(f"[bold yellow]The user {current_user[0]} has currently balance: {current_user[6]} taka\n[/]")

    # * User -> (5)
    def check_all_transaction_history(self, user_index):
        current_user = bank_manager.all_user_vault[user_index]

        if not current_user[7]:
            console.print("[bold red]You have no transactional history[/]\n")
            return

        for index, item in enumerate(current_user[7]):
            console.print(f"[bold yellow]History {index + 1}: {item}[/]")

        print("")

    # * User -> (6)
    def take_loan(self, user_index):
    
        current_user = bank_manager.all_user_vault[user_index]

        if bank_manager.is_loan_active == False:
            print("Sorry, Manager turned off the loan for maintenance. Try for loan later.")
            return

        loan_amount = float(input("Enter the amount you ask for loan: "))
        if self.loan_ask_time >= 1 and bank_manager.bank_total_reserve_balance > loan_amount:
            console.print(f"[bold yellow]Loan granted\n[/]")
            bank_manager.bank_total_reserve_balance -= loan_amount
            current_user[6] += loan_amount
            self.user_loan += loan_amount
            self.loan_ask_time -= 1
            bank_manager.total_loan_amount_grant += loan_amount
        else:
            print(f"Loan limit exceed")


    # * User -> (7)
    def money_transfer(self, current_user_index):
    
        current_user = bank_manager.all_user_vault[current_user_index]
        receiver_name = input("Enter receiver account name: ")
        receiver_account_number = input("Enter receiver account number: ")
        isExist = False

        for index, item in enumerate(bank_manager.all_user_vault):
            if item[0] == receiver_name and item[5] == receiver_account_number:
                isExist = True
                send_amount = float(input("The user exist!! Enter amount you want to send: "))
                
                if current_user[6] >= send_amount:
                    current_user[6] -= send_amount
                    # updating receiver balance
                    bank_manager.all_user_vault[index][6] += send_amount
                    console.print(f"[bold green]\nMoney transfer successful!!\n[/]")
                else:
                    console.print(f"[bold red]You don't have sufficient amount to send money\n[/]")
                
                break

        if not isExist:
            console.print("[bold red]Account does not exist[/]\n")

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
        console.print(f"[bold red underline]\nWrong credentials input\n[/]")

    print(center_text("Exiting the application\n"))
    exit()

def main():
    Bank.main_menu()

if __name__ == '__main__':
    main()