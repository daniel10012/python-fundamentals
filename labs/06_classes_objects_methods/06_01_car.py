'''
Write a class to model a car. The class should:

1. Set the attributes model, year, and max_speed in the __init__() method.
2. Have a method that increases the max_speed of the car by 5 when called.
3. Have a method that prints the details of the car.

Create at least two different objects of this Car class and demonstrate
changing the objects attributes.

'''

class Car:

  def __init__(self, model, year, max_speed):
    self.model = model
    self.year = year
    self.max_speed = max_speed

  def __str__(self):
      return (f"this is a {self.model} produced in {self.year} with a max speed of {self.max_speed} kmh")

  def boost(self):
      self.max_speed += 5

my_car1 = Car("toyota", 1986, 200)

print(my_car1)

print(my_car1.max_speed)

my_car1.boost()

print(my_car1.max_speed)

my_car2 = Car("ferrari", 2000, 300)

print(my_car2)

my_car2.boost()

print(my_car2.max_speed)

