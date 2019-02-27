'''
- Write a script with three classes that model everyday objects.
- Each class should have an __init__ method that sets attributes
    to a default value if values are not passed.
- Create at least two objects of each class using the __init__ method.
- Each object should have at least three attributes.
- Each class should have at least two class attributes.
- Create a print method in each class that prints out the attributes
    in a nicely formatted string.
- Include a __str__ method in each class.
- Overload the + operator in one of the classes
    so that it adds two attributes of that class.
- Once the objects are created, change some of the attribute values.

Be creative. Have some fun. :)
Using objects you can model anything you want.
Cars, animals, poker games, sports teams, trees, beers, people etc...


'''

class Animal:

    def __init__(self, name , mamal = True, speed = 30, num_legs = 4):
        self.name = name
        self.mamal = mamal
        self.speed = speed
        self.num_legs = num_legs

    def __str__(self):
        if self.mamal == True:
            return(f"{self.name} is a mamal , goes at speed of {self.speed} kmh and has {self.num_legs} legs")
        else:
            return(f"{self.name} is not a mamal , goes at speed of {self.speed} kmh and has {self.num_legs} legs")

    def __add__(self, other_animal):
        return (Animal(name=self.name+other_animal.name, num_legs=self.num_legs+other_animal.num_legs))

    def printing(self):
        print("nice animal")


# my_animal1 = Animal("Roger")
#
# my_animal2 = Animal("Bob", False, 20, 6)
#
# mixed_animal = my_animal1 + my_animal2
#
# mixed_animal.speed = 150
#
# print(mixed_animal)





