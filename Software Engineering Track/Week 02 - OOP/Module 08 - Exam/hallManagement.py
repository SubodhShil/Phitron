from rich.console import Console
import inquirer
from beautifultable import BeautifulTable

class Star_Cinema:
    hall_list = []

    def _entry_hall(self, name):
        hall = Hall(name)
        self.hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no) -> None:
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no

        # Creating table with "BeautifulTable" package
        self.movie_list_table = BeautifulTable()
        self.movie_list_table.columns.header = ["ID", "Movie Name", "Time"]
        self.movie_list_table.set_style((BeautifulTable.STYLE_BOX_DOUBLED))

    def view_show_list(self):
        print(self.movie_list_table)

    def entry_show(self, id, movie_name, time):
        show_details = (id, movie_name, time)
        self.__show_list.append(show_details)
        self.movie_list_table.rows.append([id, movie_name, time])
        self.allocate_seats(self.__rows, self.__cols, id)

    # This function will create empty 2D array to visualize the seats in the hall
    def allocate_seats(self, rows, columns, id):
        current_movie_seats = [[0 for _ in range(columns)] for _ in range(rows)]
        self.__seats[id] = current_movie_seats

    def book_seats(self, id):
        if id in self.__seats:
            ticket_quantity = int(input("Number of tickets: "))

            for i in range(ticket_quantity):
                print(f"\n---------------\nTicket {i + 1}\n---------------")
                reserve_seat_row, reserve_seat_column = (0, 0)

                no_error = True
                while no_error == True:

                    # Invalid seat booking error handling -> row error
                    reserve_seat_row = int(input("Enter Seat Row: "))
                    if reserve_seat_row > self.__rows or reserve_seat_row < 1:
                        print("Invalid row size")
                        continue

                    # Invalid seat booking error handling -> column error
                    reserve_seat_column = int(input("Enter Seat Column: "))
                    if reserve_seat_column > self.__cols or reserve_seat_row < 1:
                        print("Invalid column size")
                        continue
                    
                    # Error handle if seat is already booked
                    if self.__seats[id][reserve_seat_row - 1][reserve_seat_column - 1] == 1:
                        print("Seat already booked, try for other seats\n")
                        continue

                    no_error = False
                
                # allocating seat
                self.__seats[id][reserve_seat_row - 1][reserve_seat_column - 1] = 1
                console.print(f"[bold green]Your seat booked at ({reserve_seat_row} x {reserve_seat_column}) position")

        # Wrong id input error handling
        else:
            console.print("[bold red]Invalid!! No such movie or show")

    def view_available_seats(self, id):
        if id in self.__seats:
            available_seats = self.__seats[id]
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
hall_no = int(input("Enter hall no: "))

# Invalid seat booking error handling -> row error
hall_rows = int(input("Enter hall rows: "))
while hall_rows < 1: 
    print("Invalid row size")
    hall_rows = int(input("Enter hall rows: "))

# Invalid seat booking error handling -> column error
hall_columns = int(input("Enter hall columns: "))
while hall_columns < 1:
    print("Invalid column size")
    hall_columns = int(input("Enter hall columns: "))

# Adding new movie to show
currentHall = Hall(hall_rows, hall_columns, hall_no)
currentHall.entry_show(111, "Titanic", "12:00 PM")
currentHall.entry_show(112, "Mr. Bean", "12:30 PM")
currentHall.entry_show(113, "Jawan", "1:00 PM")

console.print(f"[bold underline red]\nWelcome to {hall_name} Cineplex[/]\n")

options = [
    "View all show today",
    "View available seats",
    "Book tickets",
    "Exit"
]

userOptions = [inquirer.List('options', message="I would like to", choices=options)]

while True:
    answers = inquirer.prompt(userOptions)
    user_selected_option = answers['options']

    if user_selected_option == options[-1]:
        console.print(f"[bold underline red]You picked[/]: {user_selected_option}\n")
        break

    console.print(f"[bold underline green]You picked[/]: {user_selected_option}\n")

    if user_selected_option == options[0]:
        currentHall.view_show_list()

    if user_selected_option == options[1]:
        movie_id = int(input("Enter movie ID: "))
        currentHall.view_available_seats(movie_id)

    if user_selected_option == options[2]:
        movie_id = int(input("Enter movie ID: "))
        currentHall.book_seats(movie_id)

    print()