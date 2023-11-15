class Shop:
    cartList = [] # class attribute

    def __init__(self, buyer):
        self.buyer = buyer

    def add_to_cart(self, item):
        self.cartList.append(item)


customer1 = Shop("Rockey")
customer1.add_to_cart("Bat")
print(customer1.cartList)

customer2 = Shop("Jesmin")
customer2.add_to_cart("Cosmetics")
print(customer2.cartList)

# ----------------- #
class Course:

    def __init__(self, name):
        self.courseTaken = [] # instance attribute
        self.totalPurchaseCost = 0
        self.name = name
    
    def purchase(self, courseName, cost):
        self.courseTaken.append(courseName)
        self.totalPurchaseCost += int(cost)
        print(f"{self.name} just purchased {courseName} course")
        
    def totalCost(self):
        return self.totalPurchaseCost


student1 = Course("Subodh")
student1.purchase("Dart and Flutter", 100)
student1.purchase("System Design", 200)
student1.purchase("DevOps and Backend", 500)
print(f"{student1.name} = {student1.courseTaken}")
print(student1.totalCost())

student2 = Course("Pulkit")
student2.purchase("Communication", 350)
student2.purchase("MERN stack", 400)
print(f"{student2.name} = {student2.courseTaken}")
print(student2.totalCost())