class Restaurant:
    def __init__(self, name, menu = []) -> None:
        self.name = name
        
        # chef, server, manager objects will pass
        self.chef = None
        self.server = None
        self.manager = None

        self.menu = menu
        self.revenue = 0
        self.expense = 0
        self.balance = 0
        self.profit = 0

    def add_employee(self, employee_type, employee):
        if employee_type == 'chef':
            self.chef = employee
        elif employee_type == 'server':
            self.server = employee
        elif employee_type == 'manager':
            self.manager = employee

    def receive_payment(self, order, amount, customer):
        if amount >= order.bill:
            self.revenue += order.bill
            self.balance += order.bill
            customer.due_amount = 0
            remaining = amount - order.bill
            return remaining

    def pay_expense(self, expense_amount, description):
        if self.balance > expense_amount:
            self.expense += expense_amount
            self.balance -= expense_amount
            print(f"Expense {expense_amount} for {description}")

    def pay_salary(self, employee):
        if self.balance > employee.salary:
            employee.receive_salary()

    