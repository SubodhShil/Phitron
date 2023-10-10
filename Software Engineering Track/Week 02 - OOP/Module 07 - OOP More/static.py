class Shopping:
    cart = []  # class attribute or static attribute
    origin = 'Japan'

    def __init__(self, name, location) -> None:
        self.name = name            # instance attribute
        self.location = location    # instance attribute

    @classmethod                    # decorator specifies a class method
    def serverError(self):
        print("404")

    # 'purchase' is a static class method
    @classmethod
    def purchase(self, item: str, price: float, amount: float):
        self.item = item
        self.price = price
        self.amount = amount

        if self.amount > self.price:
            remaining = self.amount - self.price
            print(f"Item: {self.item}\nRemaining money: {remaining} taka")
            self.serverError()
        else:
            print(f"Pay {self.price}")
            self.serverError()

    # staic method can be used without instance or object
    @staticmethod                  # decorator specifies a class method
    def offer(giftCard: bool):
        if giftCard:
            giftCardValue = int(input())
            print(f'You can buy anything worth {giftCardValue} taka')
        else:
            print('Sorry, offer is only granted to gift card holder')
            # Can't access any class attributes like variables from a static method
            # self.serverError()


Shopping.purchase('Condensed milk', 100, 500)
Shopping.offer(False)
