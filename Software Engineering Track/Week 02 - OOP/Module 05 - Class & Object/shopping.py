class Shopping:

    def __init__(self, name):
        self.name = name
        self.total_cost = 0
        self.cart = []

    def add_to_cart(self, item, price, quantity):
        self.total_cost += (price * quantity)
        product = {'item': item, 'price': price,
                   'quantity': quantity, 'total_cost': self.total_cost}
        self.cart.append(product)

    # To do later
    def update_cart(self, remove_item, update_quantity_amount = 0):
        for product in self.cart:
            if remove_item in product:
                self.cart.remove(product)

    def checkout(self, amount):
        for item in self.cart:
            print(item)

        print(f"Total bill: ৳{self.total_cost}")

        if amount < self.total_cost:
            print(
                f"Your bill is {self.total_cost} taka, Please provide more {abs(self.total_cost - amount)} taka to checkout")
            return

        if amount >= self.total_cost:

            extra = amount - self.total_cost
            if extra != 0:
                print(f"Thanks for purchasing, your changes are: ৳{extra}")
            else:
                print("Thanks from purchasing from us")


Motaleb = Shopping("Motaleb")
Motaleb.add_to_cart("Fish", 2000, 1)
Motaleb.add_to_cart("Mugdal", 60, 2)
Motaleb.add_to_cart("Chanachur", 50, 3)
# Motaleb.checkout(2269)
Motaleb.update_cart("Mugdal")
Motaleb.checkout(2269)
