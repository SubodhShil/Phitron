from rich.console import Console
import inquirer
import pwinput

# Rich library "console" object
console = Console()

# external file import
from User import User

def authentication():
    # User credentials
    allUserVault = []
    
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

            if adminName == "Subodh" and adminPassword == "admin":
                console.print(f"[bold green]Welcome Manager {adminName}[/]")

        # * User Authentication
        elif allUserSelectedOption == authOptions[1]:
            general_bank_user = User(allUserVault)
            general_bank_user.userAuth()
            
        elif allUserSelectedOption == authOptions[-1]:
            console.print(
                f"[bold red]Thanks for using our bank, see you soon!![/]")
            break

def main():
    authentication()

if __name__ == '__main__':
    main()
    
