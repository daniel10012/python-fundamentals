'''
Create two classes that model a rectangle and a circle. The rectangle class should
be constructed by length and width while the circle class should be constructed by
radius.

Write methods in the appropriate class so that you can calculate the area (of the rectangle and circle),
perimeter (of the rectangle) and circumference of the circle.

'''



class Rectangle:

    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width

    def __str__(self):
        return f"this is a rectangle with a lenght of {self.lenght} and a width of {self.width}"

    def area(self):
        return self.width * self.lenght

    def perimeter(self):
        return (self.lenght + self.width)*2

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius**2 * 3.14

    def circumference(self):
        return 2*3.14*self.radius

my_rectangle = Rectangle(3,7)
my_circle = Circle(3)

print(my_rectangle.area())
print(my_circle.area())
print(my_circle.circumference())
print(my_rectangle.perimeter())