import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)


def calculate_area(shape):
    return shape.area()


# Create instances of Rectangle and Circle
rectangle = Rectangle(10, 5)
circle = Circle(7)

# Calculate and print the areas of the shapes
print(f"The area of the Rectangle is: {calculate_area(rectangle)}")
print(f"The area of the Circle is: {calculate_area(circle)}")

