class Food:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price
        self.cooking_time = 15

class Burger(Food):
    def __init__(self, name, price, meat, ingredients) -> None:
        super().__init__(name, price)
        self.meat = meat
        self.ingredients = ingredients

class Pizza(Food):
    def __init__(self, name, price, size, toppings) -> None:
        super().__init__(name, price)
        self.size = size
        self.toppings = toppings

class Drinks(Food):
    def __init__(self, name, price, isCold = True) -> None:
        super().__init__(name, price)
        self.isCold = isCold

class Menu:
    def __init__(self) -> None:
        self.pizzas = []
        self.burgers = []
        self.drinks = []

    def add_menu_items(self, item_type, item:object):
        if item_type == 'pizza':
            self.pizzas.append(item)
        elif item_type == 'burger':
            self.burgers.append(item)
        elif item_type == 'drinks':
            self.drinks.append(item)

    def remove_pizza(self, pizza):
        if pizza in self.pizzas:
            self.pizzas.remove(pizza)

        
    def remove_item(self, item_type, item):
        if item_type == 'pizza' and item in self.pizzas:
            self.pizzas.remove(item)
        elif item_type == 'burger' and item in self.burgers:
            self.burgers.remove(item)
        elif item_type == 'drinks' and item in self.drinks:
            self.drinks.remove(item)
        else:
            print("Invalid item")
    
    def show_menu(self):
        print("Pizza\n------")
        for pizza in self.pizzas:
            print(f"{pizza.name}: ৳{pizza.price}")
        
        print("\nBurger\n-------")
        for burger in self.burgers:
            print(f"{burger.name}: ৳{burger.price}")
        
        print("\nDrinks\n--------")
        for drink in self.drinks:
            print(f"{drink.name}: ৳{drink.price}")

