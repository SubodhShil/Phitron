
# ** Bank.py only used for run the application as entrypoint

from rich.console import Console
import inquirer
import pwinput

# Rich library "console" object
console = Console()

# external file import
from Logic import Admin, User

class Bank:

    def main_menu():

        # * User object
        general_bank_user = User()

        # * Admin object
        bank_admin = Admin()

        console.print(f"[bold green underline]Welcome to Royal Earth Bank")
        console.print(f"[bold yellow]\nSelect your user type")

        authOptions = [
            "Admin",
            "User",
            "Employee",
            "See all accounts",
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

                if bank_admin.isAdmin(adminName, adminPassword):
                    console.print(f"[bold green]Welcome Manager {adminName}[/]")
                    bank_admin.admin_privileges()

            # * User Authentication
            elif allUserSelectedOption == authOptions[1]:
                general_bank_user.userAuth()

            elif allUserSelectedOption == authOptions[3]:
                general_bank_user.current_user_accounts()
            
            elif allUserSelectedOption == authOptions[-1]:
                console.print(f"[bold red]Thanks for using our bank, see you soon!![/]")
                break

def main():
    Bank.main_menu()

if __name__ == '__main__':
    main()