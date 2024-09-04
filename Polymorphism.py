# Define a class called "Shape"
class Shape:
    def area(self):
        pass  # Abstract method, to be implemented by child classes

# Define a child class called "Circle" that inherits from Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

# Define a child class called "Rectangle" that inherits from Shape
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Create objects of the Circle and Rectangle classes
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Call the area method on each object
print(circle.area())  
print(rectangle.area())  
