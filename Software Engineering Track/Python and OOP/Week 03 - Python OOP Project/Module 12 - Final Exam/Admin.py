from rich.console import Console
import inquirer
import pwinput

# Rich library "console" object
console = Console()

class Admin:

    def __init__(self) -> None:

        self.name = "Subodh"
        self.password = "admin"
        self.bank_total_reserve_balance = 0
        
        self.options = [
            "Create Account",
            "Delete User Account",
            "See All User Accounts",
            "Available Bank Reserve",
            "Loan Feature Toggle",
            "Exit Application"
        ]

    def isAdmin(self, name: str, password: str):
    
        if self.name == name and self.password == password:
            return True
        else:
            return False

    def admin_options(self):

        admin_options = [inquirer.List("options", message="Choice: ", choices=self.options)]
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
                self.loan_features()

            else:
                print(f"Exiting the application Manager {self.name}")
                exit()

    # * Admin option -> 1
    def create_account(self):
        print("no")

    # * Admin option -> 2
    def delete_user_account(self):
        print("no")

    # * Admin option -> 3
    def see_all_user_accounts(self):
        print("no")

    # * Admin option -> 4
    def see_bank_reserve(self):
        print("no")

    # * Admin option -> 5
    def loan_features(self):
        print("no")
