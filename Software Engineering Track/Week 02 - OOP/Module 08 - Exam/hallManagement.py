from rich.console import Console
import inquirer
from beautifultable import BeautifulTable


class Star_Cinema:
    def __init__(self) -> None:
        # empty list
        self.hall_list = []

    def entry_hall(self):
        hall = Hall()
        self.hall_list.append(hall)


class Hall:
    def __init__(self) -> None:
        self.seats = {}
        self.show_list = []
        self.rows = None
        self.cols = None
        self.hall_no = None

    def entry_show(self, id, movie_name, time):
        pass

    def book_seats(self):
        pass

    def view_show_list(self):
        pass

    def view_available_seats(self):
        pass


# Rich library "console" object
console = Console()

movie_list_table = BeautifulTable()
movie_list_table.rows.append([111, "Titanic"])
movie_list_table.rows.append([112, "Scam 2023"])
movie_list_table.rows.append([113, "Parasyte"])
movie_list_table.columns.header = ["Movie Name", "ID"]
movie_list_table.set_style((BeautifulTable.STYLE_BOX_DOUBLED))

console.print("[bold underline red]Welcome to Dhaka Cineplex[/]\n")

options = [
    "View all show today",
    "View available seats",
    "Book tickets",
    "Exit"
]

userOptions = [
    inquirer.List('options', message="I would like to", choices=options)]

answers = inquirer.prompt(userOptions)
user_selected_option = answers['options']
console.print(f"[bold underline green]You picked[/]: {user_selected_option}\n")

if user_selected_option == options[0]:
    print(movie_list_table)
