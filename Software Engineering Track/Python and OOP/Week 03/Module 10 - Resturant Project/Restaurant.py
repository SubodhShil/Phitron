class Restaurant:
    def __init__(self, name, menu:object = []) -> None:
        self.name = name
        self.orders = []

        # chef, waiter, manager objects will pass
        self.chef = None
        self.waiter = None
        self.manager = None

        self.rent = 5000
        self.menu = menu
        self.revenue = 0
        self.expense = 0
        self.balance = 0
        self.profit = 0

    def add_employee(self, employee_type:str, employee:object):
        if employee_type == 'chef':
            self.chef = employee
        if employee_type == 'waiter':
            self.waiter = employee
        if employee_type == 'manager':
            self.manager = employee

    def receive_payment(self, order, amount, customer):
        if amount >= order.bill:
            self.revenue += order.bill
            self.balance += order.bill
            customer.due_amount = 0
            remaining = amount - order.bill
            return remaining
        else:
            print("Not enough money")

    def add_order(self, order):
        self.orders.append(order)

    def pay_expense(self, expense_amount, description):
        if self.balance > expense_amount:
            self.expense += expense_amount
            self.balance -= expense_amount
            print(f"Expense {expense_amount} for {description}")
        else:
            print(f"Don't have enough money to pay for: {description}")
            
    def pay_salary(self, employee):
        # TODO: error handling
        if self.balance > employee.salary:
            print(f"Paying salary for: {employee.name} and salary: {employee.salary}")
            self.balance -= employee.salary
            self.expense += employee.salary
            employee.receive_salary()
        else:
            print(f"Not adequate balance to pay employee salary")

    def show_employees(self):
        print("\nShowing Employees\n--------------------")
        if self.chef is not None:
            print(f"Chef Name: {self.chef.name}\tSalary {self.chef.salary}")

        if self.waiter is not None:
            print(f"Waiter Name: {self.waiter.name}\tSalary {self.waiter.salary}")
            
        if self.manager is not None:
            print(f"Manager Name: {self.manager.name}\tSalary {self.manager.salary}")
