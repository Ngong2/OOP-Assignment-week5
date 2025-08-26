# Base class
class Vehicle:
    def move(self):
        # This will be overridden by subclasses
        pass

# Derived classes with polymorphism
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

class Bicycle(Vehicle):
    def move(self):
        print("Pedaling 🚴")

# Using polymorphism
vehicles = [Car(), Plane(), Boat(), Bicycle()]

for v in vehicles:
    v.move()   # Same method, different output!
