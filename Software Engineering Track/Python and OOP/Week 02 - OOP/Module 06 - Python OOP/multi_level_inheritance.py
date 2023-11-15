class Vehicle:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self) -> str:
        return f"{self.name}\n{self.price}"

    def move(self):
        pass


class Bus(Vehicle):
    def __init__(self, name, price, seat):
        self.seat = seat
        super().__init__(name, price)

    def __repr__(self) -> str:
        return super().__repr__()


class Truck(Vehicle):
    def __init__(self, name, price, weight):
        self.weight = weight
        super().__init__(name, price)


class PickUpTruc(Truck):
    def __init__(self, name, price, weight):
        super().__init__(name, price, weight)


class ACBus(Bus):

    def __init__(self, name, price, seat, temperature):
        self.temeperature = temperature
        super().__init__(name, price, seat)

    def __repr__(self) -> str:
        return super().__repr__()


green_line = ACBus('Green Line', 5000000, 50, 16)
print(green_line)
