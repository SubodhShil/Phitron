from rich.console import Console


class Book:
    def __init__(self, id, bookName, quantity) -> None:
        self.id = id
        self.bookName = bookName
        self.quantity = quantity


class User:
    def __init__(self, id, name, designation, password) -> None:
        self.id = id
        self.name = name
        self.designation = designation
        self.password = password
        self.borrowedBooks = []
        self.returnedBooks = []


class Library:
    def __init__(self, library_name) -> None:
        self.library_name = library_name
        self.users = []
        self.books = []

    def addBook(self, id, bookName, quantity):
        # id = total_user_size + 1 ==> len(self.books) + 1
        book = Book(id, bookName, quantity)
        self.books.append(book)
        console.print(f"[bold red]{book.bookName}[/] added to library successfully!")

    def addUser(self, id, name, designation, password):
        user = User(id, name, designation, password)
        self.users.append(user)
        return user

    def borrowBook(self, user, token):
        for book in self.books:
            if book.bookName == token:
                # Check already borrowed or not
                if book in user.borrowedBooks:
                    print("Book already in your borrow list")
                    return
                elif book.quantity == 0:
                    print("Sorry, the book is not available currently")
                    return

            user.borrowedBooks.append(book)
            book.quantity -= 1  
            return

        print(f"No such book found with name: {token}")

    def returnBook(self, user, token):
            for book in self.books:
                if book.bookName == token:
                    # Check already borrowed or not
                    if book in user.borrowedBooks:
                        print("Book already in your borrow list")
                        return
                    elif book.quantity == 0:
                        print("Sorry, the book is not available currently")
                        return

                user.borrowedBooks.append(book)
                book.quantity -= 1  
                return

            print(f"No such book found with name: {token}")

# Rich library "console" object
console = Console()

library1 = Library("Dhaka Central Library")
# Admin Information
admin = library1.addUser(1000, "Pulkit Sharma", "ADMIN", "1234@admin")

# User
print("Enter user details\n----------------")
# user1 = library1.addUser(int(input("Enter user ID: ")), input("Enter user name: "), input("Enter library designation: "), input("Enter password: "))
# Book details
book1 = library1.addBook(11, "CP Book by Felix Halim", 3)

# Working with current user: already logged in or have to create an acount
currentUser = None
while currentUser == None:

    option = input("Login or Register: [L/R] ")

    if option == "L":
        id = int(input("Enter ID: "))
        password = input("Enter password: ")

        match = False
        for user in library1.users:
            if user.id == id and user.password == password:
                currentUser = user
                match = True
                break
        if match == False:
            print("No user found, create an account")
        else:
            console.print("[bold underline green]Logged in successful[/]")

    elif option == "R":
        id = int(input("Give an ID: "))
        name = input("Enter name: ")
        designation = input("Enter your designation: ")
        while designation.upper() == "ADMIN":
            designation = input("Can't be Admin, Enter designation: ")
        password = input("Enter Password: ")

        for user in library1.users:
            if user.id == id:
                print("User already exist\n")

        console.print("[bold Green]Registration successful!![/]")
        newUser = library1.addUser(id, name, designation, password)
        currentUser = newUser

# Showing message
# console.print(f"Welcome back [bold cyan]{currentUser.name}![/]\n")

choice = None
while currentUser == admin and (choice == None):
    print("Options:\n-----------")
    console.print("[bold yellow]⮞[/]  1: Add book")
    console.print("[bold yellow]⮞[/]  2: Add user")
    console.print("[bold yellow]⮞[/]  3: Show all books")
    console.print("[bold yellow]⮞[/]  4: Logout\n")
    choice = int(input("Enter option: "))

    # User choice for adding a book
    if choice == 1:
        bookID = int(input("Enter book ID: "))
        bookName = input("Enter book name: ")
        quantity = int(input("Enter No of books: "))
        library1.addBook(bookID, bookName, quantity)
        # library1.addBook(int(input("Enter book ID: ")), input("Enter book name: "), int(input("Enter No of books: ")))

    # User choice for adding an user
    elif choice == 2:
        pass

    # Showing all the books
    elif choice == 3:
        print(f"The library has the following books")
        for book in library1.books:
            print(f"{book.id}\t{book.bookName}\t{book.quantity}")
        print("\n")

    # Log out
    elif choice == 4:
        console.print(f"[bold red underline]Logging Out[/]")
    else:
        choice = None
        console.print(f"\n[bold red underline]Invalid choice[/]")

while currentUser != admin:
    print(f"\nWelcome {currentUser.name}, choose what are you looking for")
    print("Options:\n-----------")
    console.print("[bold yellow]⮞[/]  1: Borrow book")
    console.print("[bold yellow]⮞[/]  2: Request Book")
    console.print("[bold yellow]⮞[/]  3: Show borrowed books")
    console.print("[bold yellow]⮞[/]  3: Show history")
    console.print("[bold yellow]⮞[/]  4: Logout\n")
    choice = int(input("Enter option: "))
