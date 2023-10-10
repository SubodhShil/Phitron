class Company:
    def __init__(self, name, address) -> None:
        self.name = name
        self.bus = []
        self.routes = []
        self.drivers = []
        self.counter = []
        self.manager = []
        self.supervisors = []
        self.fare = []
        self.address = address


class Driver:
    def __init__(self, name, license, age) -> None:
        self.name = name
        self.license = license
        self.age = age


class Counter:
    pass


class Passengers:
    pass


class Supervisors:
    pass
