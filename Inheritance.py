# Define a parent class called "Vehicle"
class Vehicle:
    def __init__(self, wheels:int):
        self.wheels = wheels

    def move(self):
        print("The vehicle is moving.")

# Define a child class called "Bicycle" that inherits from Vehicle
class Bicycle(Vehicle):
    def __init__(self, wheels: int, gear: int):
        super().__init__(wheels)  # Call the parent class's __init__ method
        self.gear = gear

    def pedal(self):
        print("Pedaling the bicycle.")

# Create an object of the Bicycle class
my_bike = Bicycle(2, "Mountain")

# Access and print the attributes of the object
print(my_bike.wheels)  
print(my_bike.gear)    

# Call the method on the object
my_bike.move()  
my_bike.pedal()  
