class MacBook:
    model = "Air M1"

    def __init__(self, model):
        self.model = model
        print(f"The MacBook {self.model} is equipied with 8GB RAM")

buy1 = MacBook("Pro M2")


class Phone:
    manufactured = "Taiwan"

    def __init__(self, owner, brand, price, origin):
        self.manufactured = origin
        self.owner = owner
        self.brand = brand
        self.price = price

    def checkDetails(self):
        print(f"Phone manufactured in {self.manufactured}\nOwner name {self.owner}\nBrand name {self.brand}\nPrice {self.price}")

buyer = Phone("Jack", "Apple", "15000", "India")
buyer.checkDetails()