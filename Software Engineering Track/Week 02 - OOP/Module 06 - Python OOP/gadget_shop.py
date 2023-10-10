# Creating a common/parent/base/super class
class Device:
    def __init__(self, brand, price, color, ram, rom, origin) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.ram = ram
        self.rom = rom
        self.origin = origin

    def run(self) -> str:
        return f"Running laptop {self.brand}"

class Laptop:
    def coding(self, language="python") -> str:
        return f"Learning {language} and doing projects"

# Phone class is inheriting the 'Device' class
class Phone(Device):
    def __init__(self, brand, price, color, ram, rom, origin, dual_sim: bool) -> None:
        self.dual_sim = dual_sim
        super().__init__(brand, price, color, ram, rom, origin)
        
        # experiment: create a dictionary and store values into it
        self.phone_details = {}
        self.phone_details[str(self.brand)] = brand
        

    def phone_call(self, number, text):
        return f"Sending SMS to: {number}\nMessage: {text}"

    def __repr__(self):
        return f"Phone: {self.dual_sim}"

class Camera:
    def __init__(self, pixel) -> None:
        self.pixel = pixel

    def change_lens(self):
        pass

# inheritance
my_phone = Phone("Realme", 15000, 'Black', 6, 32, 'China', True)
print(my_phone)