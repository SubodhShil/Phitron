# Composition in Python refers to "has a" relationship

# Example 01
class Engine:
    def __init__(self) -> None:
        pass

    def start(self):
        return "Engine Started"

class Driver:
    def __init__(self) -> None:
        pass

class Car:
    def __init__(self) -> None:
        self.engine = Engine()
        self.driver = Driver()

    def start(self):
        self.engine.start()


# Example 02
class CPU:
    def __init__(self, core) -> None:
        self.core = core
    def __str__(self) -> str:
        return f'{self.core}'
        
class RAM:
    def __init__(self, size) -> None:
        self.size = size
    def __str__(self) -> str:
        return f'{self.size}'

class HDD:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
    def __str__(self) -> str:
        return f"{self.capacity}"

class Laptop:
    def __init__(self, core_count, ram_size, hdd_capacity):
        self.cpu = CPU(core_count)
        self.ram = RAM(ram_size)
        self.hdd = HDD(hdd_capacity)

    def __str__(self):
        return f"Your Macbook configuration\n--------------------------------\nCPU = {self.cpu} Cores\nRAM = {self.ram} GB\nHDD = {self.hdd} GB"
    
Macbook = Laptop(8, 16, 512)
print(Macbook)