class Shopping:

    def __init__(self, name):
        self.name = name
        self.total_cost = 0
        self.cart = []

    def add_to_cart(self, item, price, quantity):
        self.total_cost += (price * quantity)
        product = {'item': item, 'price': price,
                   'quantity': quantity, 'product_cost': int(price * quantity)}
        self.cart.append(product)

    def remove_cart(self, remove_item):
        # removing item
        for product in self.cart:
            if product.get('item') == remove_item:
                # remove the price for checkout
                self.total_cost -= (product['product_cost'])
                self.cart.remove(product)

    def update_cart(self, item_name, update_quantity_amount=0):
        # updating cart quantity
        for product in self.cart:
            if product.get('item') == item_name:
                # update the price for checkout
                product['quantity'] = int(update_quantity_amount)
                # remove the previous cost of this item
                self.total_cost -= product['product_cost']
                product['product_cost'] = int(
                    product['price'] * product['quantity'])
                # add new item cost
                self.total_cost += product['product_cost']

    def checkout(self, amount):
        for item in self.cart:
            print(item)

        print(f"Total bill: ৳{self.total_cost}")

        if amount < self.total_cost:
            print(
                f"Your bill is {self.total_cost} taka, Please provide {abs(self.total_cost - amount)} taka more to checkout")
            return

        if amount >= self.total_cost:

            extra = amount - self.total_cost
            if extra != 0:
                print(f"Thanks for purchasing, your changes are: ৳{extra}")
            else:
                print("Thanks from purchasing from us")


""" Motaleb = Shopping("Motaleb")
Motaleb.add_to_cart("Fish", 2000, 1)
Motaleb.add_to_cart("Mugdal", 60, 20)
Motaleb.add_to_cart("Chanachur", 50, 30)
# Motaleb.checkout(2269)
Motaleb.checkout(2269)
Motaleb.remove_cart("Mugdal")
print()
Motaleb.update_cart('Chanachur', 7)
Motaleb.checkout(2269)
"""