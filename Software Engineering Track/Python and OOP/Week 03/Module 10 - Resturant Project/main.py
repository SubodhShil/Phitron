from Menu import Pizza, Burger, Drinks, Menu
from Restaurant import Restaurant
from User import Chef, Customer, Waiter, Manager
from Order import Order

def main():
    resturant_menu_items = Menu()

    # Add pizza to the menu
    pizza1 = Pizza("Vegetable Pizza", 400, 'Medium', ["Mushroom", "Onion", "Vegetables"])
    resturant_menu_items.add_menu_items('pizza', pizza1)
    pizza2 = Pizza("Cheese Pizza", 500, "Medium", ["Cheese", "Vegetables", "Fruits"])
    resturant_menu_items.add_menu_items('pizza', pizza2)
    pizza3 = Pizza("Chicken Pizza", 600, "Large", ["Chicken", "Tomato", "Cheese"])
    resturant_menu_items.add_menu_items('pizza', pizza3)

    # Add burger to the menu
    burger1 = Burger("Vegetable Burger", 200, "none", ['Vegetables', 'Lettuce', 'Tomato Sauce'])
    resturant_menu_items.add_menu_items('Bruger', burger1)
    burger2 = Burger("Chicken Burger", 300, "Chicken", ['Chicken', "Sauce"])
    resturant_menu_items.add_menu_items('burger', burger2)
    burger3 = Burger("Naga Cheese Burger", 500, "Chicken", ["Chicken", "Vegetables", "Naga Sauce"])
    resturant_menu_items.add_menu_items('burger', burger3)

    # Add drinks to the menu
    rc_cola = Drinks("RC Cola", 50, True)
    resturant_menu_items.add_menu_items('drinks', rc_cola)
    coffee = Drinks('Dalgona', 200, False)
    resturant_menu_items.add_menu_items('drinks', coffee)

    # Showing menu items
    resturant_menu_items.show_menu()

    # Setting up the resturant
    resturant = Restaurant("Diabari Resturant", resturant_menu_items)

    # Setting employees for the resturant
    resturant_manager = Manager("KalaChan", 999, "kalachan.manager@hotmail.com", "Kaliapur", 45000, "Jan 1, 2020", "Core team")
    resturant.add_employee("manager", resturant_manager)

    resturant_chef = Chef("Hakim", 333, "Hakim.chef@ppmail.com", "HuihuiPur", 30000, "March 1, 2021", "Cook", resturant_menu_items)
    resturant.add_employee("chef", resturant_chef)

    resturant_waiter = Waiter("Subodh", 444, "subodh.waiter@gmail.com", "Furfurinagar", 20000, "Jan 2, 2020", "Service")
    resturant.add_employee("waiter", resturant_waiter)

    # Show resturant employees
    resturant.show_employees()

    # customer objects
    customer_1 = Customer("Ankit", 123, "ankit.customer@gmail.com", "Dhaka", 20000)
    order_1 = Order(customer_1, [pizza2, coffee, pizza1, burger3, burger1, rc_cola])
    customer_1_bill = order_1.bill
    print(f"\nCustomer 1 bill: {customer_1_bill}")
    customer_1_payment = int(input("Enter payment amount: "))
    resturant.receive_payment(order_1, customer_1_payment, customer_1)

    if customer_1_bill <= customer_1_payment:
        customer_1.pay_for_order(order_1.bill)
        resturant.add_order(order_1)

    print(f"\nCustomer 1\n----------\nRevenue: {resturant.revenue} and Balance: {resturant.balance}")

    customer_2 = Customer("Raida", 123, "ankit.customer@gmail.com", "Barishal", 30000)
    order_2 = Order(customer_2, [pizza1, pizza3, burger1, rc_cola, burger2, coffee, burger3])
    customer_2_bill = order_2.bill
    print(f"Customer 2 bill: {customer_2_bill}")
    customer_2_payment = int(input("Enter payment amount: "))
    resturant.receive_payment(order_2, customer_2_payment, customer_2)    

    if customer_2_bill <= customer_2_payment:
        customer_2.pay_for_order(order_2.bill)
        resturant.add_order(order_2)
    
    print(f"\nCustomer 2\n----------\nRevenue: {resturant.revenue} and Balance: {resturant.balance}")

    # pay resturant rent
    resturant.pay_expense(resturant.rent, 'Rent')
    print(f"\nAfter rent\n----------\nRevenue: {resturant.revenue} and Balance: {resturant.balance}")
    
    # pay employee salary
    resturant.pay_salary(resturant_chef)
    print(f"\nAfter paying salary\n----------\nRevenue: {resturant.revenue} and Balance: {resturant.balance}")

# Call the main function
if __name__ == '__main__':
    main()