from rich.console import Console
import inquirer
from beautifultable import BeautifulTable

class Star_Cinema:
    hall_list = []

    def entry_hall(self, name):
        hall = Hall(name)
        self.hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self, name) -> None:
        self.name = name
        self.seats = {}
        self.rows = None
        self.cols = None
        self.show_list = []
        self.hall_no = None

        # Creating table with "BeautifulTable" package
        self.movie_list_table = BeautifulTable()
        self.movie_list_table.columns.header = ["Movie Name", "ID", "Time"]
        self.movie_list_table.set_style((BeautifulTable.STYLE_BOX_DOUBLED))

    def view_show_list(self):
        print(self.movie_list_table)

    def entry_show(self, id, movie_name, time):
        show_details = (id, movie_name, time)
        self.show_list.append(show_details)
        self.movie_list_table.rows.append([id, movie_name, time])
        self.allocate_seats(10, 10, id)

    def allocate_seats(self, rows, columns, id):
        current_movie_seats = [[0 for _ in range(columns)] for _ in range(rows)]
        self.seats[id] = current_movie_seats

    def book_seats(self, id):
        if id in self.seats:
            ticket_quantity = int(input("Number of tickets: "))

            for i in range(ticket_quantity):
                print(f"\n---------------\nTicket {i + 1}\n---------------")
                reserve_seat_row, reserve_seat_column = (0, 0)

                no_error = True
                while no_error == True:

                    # Invalid seat booking error handling -> row error
                    reserve_seat_row = int(input("Enter Seat Row: "))
                    if reserve_seat_row > 10 or reserve_seat_row < 1:
                        print("Invalid row size")
                        continue

                    # Invalid seat booking error handling -> column error
                    reserve_seat_column = int(input("Enter Seat Column: "))
                    if reserve_seat_column > 10 or reserve_seat_row < 1:
                        print("Invalid column size")
                        continue
                    
                    # Error handle if seat is already booked
                    if self.seats[id][reserve_seat_row - 1][reserve_seat_column - 1] == 1:
                        print("Seat already booked, try for other seats\n")
                        continue

                    no_error = False
                
                # allocating seat
                self.seats[id][reserve_seat_row - 1][reserve_seat_column - 1] = 1
                console.print(f"[bold green]Your seat booked at ({reserve_seat_row} x {reserve_seat_column}) position")

        # Wrong id input error handling
        else:
            console.print("[bold red]Invalid!! No such movie or show")

    def view_available_seats(self, id):
        if id in self.seats:
            available_seats = self.seats[id]
            available_seats_table = BeautifulTable()
            available_seats_table.set_style((BeautifulTable.STYLE_BOX_DOUBLED))

            for row in available_seats:
                available_seats_table.rows.append(row)
            print(available_seats_table)
        else:
            console.print("[bold red underline]Invalid movie ID[/]")

# Rich library "console" object
console = Console()

# Application starts here
hall_name = input("Enter hall name: ")
current_hall = Hall(hall_name)
console.print(f"[bold underline red]Welcome to {hall_name} Cineplex[/]\n")

options = [
    "View all show today",
    "View available seats",
    "Book tickets",
    "Exit"
]

userOptions = [inquirer.List('options', message="I would like to", choices=options)]

# Adding new movie to show
movieEntry = Hall(hall_name)
movieEntry.entry_show(111, "Titanic", "12:00 PM")
movieEntry.entry_show(112, "Mr. Bean", "12:30 PM")
movieEntry.entry_show(113, "Jawan", "1:00 PM")

while True:
    answers = inquirer.prompt(userOptions)
    user_selected_option = answers['options']

    if user_selected_option == options[-1]:
        console.print(f"[bold underline red]You picked[/]: {user_selected_option}\n")
        break

    console.print(f"[bold underline green]You picked[/]: {user_selected_option}\n")

    if user_selected_option == options[0]:
        movieEntry.view_show_list()

    if user_selected_option == options[1]:
        movie_id = int(input("Enter movie ID: "))
        movieEntry.view_available_seats(movie_id)

    if user_selected_option == options[2]:
        movie_id = int(input("Enter movie ID: "))
        movieEntry.book_seats(movie_id)

    print()