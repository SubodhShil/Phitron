from abc import ABC, abstractmethod
from datetime import datetime

class User(ABC):
    def __init__(self, name, email, number, nid) -> None:
        self.name = name
        self.email = email
        self.__nid = nid
        self.__id = id
        self.number = number
        self.wallet = 0

    @abstractmethod
    def display_profile(self):
        raise NotImplementedError

class Rider(User):
    def __init__(self, name, email, number, nid, current_location, initial_amount) -> None:
        self.current_ride = None
        self.wallet = initial_amount
        self.current_location = current_location
        super().__init__(name, email, number, nid)

    def display_profile(self):
        print(f"Rider Name: {self.name}\nRider Number: {self.number}")

    def load_cash(self, amount):
        if amount > 0:
            self.wallet += amount
    
    def update_location(self, current_location):
        self.current_location = current_location

    def request_ride(self, destination, current_location = None):
        if not self.current_ride:
            ride_request = Ride_Request(self, destination)
            ride_matcher = Ride_Matching()
            self.current_ride = ride_matcher.find_drivers(ride_request)

class Driver(User):
    def __init__(self, name, email, number, nid, current_location) -> None:
        self.current_location = current_location
        self.wallet = 0
        super().__init__(name, email, number, nid)

    # Accept ride request from the user
    def accept_ride(self, ride):
        ride.set_driver(self)

    def display_profile(self):
        print(f"Driver Name: {self.name}\nDriver Number: {self.number}")

# class demonstrates all the riding details
class Ride:
    def __init__(self, start_location, end_location) -> None:
        self.start_location = start_location
        self.end_location = end_location
        self.driver = None
        self.rider = None
        self.start_time = None
        self.end_time = None
        self.estimated_fare = None

    def set_driver(self, driver):
        self.driver = driver

    def start_drive(self):
        self.start_time = datetime.now()

    def end_ride(self, rider, payment):
        self.end_time = datetime.now()
        # self.estimated_fare += payment
        self.rider.wallet -= self.estimated_fare
        self.driver.wallet += self.estimated_fare

class Ride_Request:
    def __init__(self, rider:Rider, end_location) -> None:
        self.rider = rider
        self.end_location = end_location

class Ride_Matching:
    def __init__(self) -> None:
        self.available_drivers = []

    def find_drivers(self, ride_request:Ride_Request):
        if len(self.available_drivers) > 0:
            # TODO: find the closest driver near the rider and othe cirteria
            driver_index = 0
            driver = self.available_drivers[driver_index]
            ride = Ride(ride_request.rider.current_location, ride_request.end_location)
            driver.accept_ride(ride)
            
            return ride

class Vehicle(ABC):
    speed = {
        'car': 70,
        'bike': 70,
        'cng': 50,
    }
    
    all_vehicle_status = ['On service', 'Currently unavailable', 'On maintenance']
    
    def __init__(self, vehicle_type, vehicle_status ,license_plate, rate) -> None:
        self.vehicle_type = vehicle_type
        self.status = vehicle_status
        self.license_plate = license_plate
        self.rate = rate
        super().__init__()

    @abstractmethod
    def start_drive(self):
        raise NotImplemented

class Car(Vehicle):
    def __init__(self, vehicle_type, vehicle_status, license_plate, rate) -> None:
        super().__init__(vehicle_type, vehicle_status, license_plate, rate)

    def start_drive(self):
        self.status = self.all_vehicle_status[0]

class Bike(Vehicle):
    def __init__(self, vehicle_type, vehicle_status, license_plate, rate) -> None:
        super().__init__(vehicle_type, vehicle_status, license_plate, rate)

    def start_drive(self):
        self.status = self.all_vehicle_status[2]

class Ride_Sharing:
    def __init__(self, company_name) -> None:
        self.company_name = company_name
        self.riders = []
        self.drivers = []
        self.rides = []

    def add_rider(self, rider:Rider):
        self.riders.append(rider)
        
    def add_driver(self, driver:Driver):
        self.drivers.append(driver)

    