'''
Build on the previous exercise.

Create subclasses of two of the existing classes. Create a subclass of
one of those so that the hierarchy is at least three levels.

Build these classes out like we did in the previous exercise.

If you cannot think of a way to build on your previous exercise,
you can start from scratch here.

We encourage you to be creative and try to think of an example of
your own for this exercise but if you are stuck, some ideas include:

- A Vehicle superclass, with Truck and Motorcycle subclasses.
- A Restaurant superclass, with Gourmet and FastFood subclasses.

'''

from freeform import Animal

class Mamal(Animal):

    def __init__(self, name, speed, num_legs, cute = True):
        super().__init__(name, speed, num_legs)
        self.cute = cute

class Ovipar(Animal):

    def __init__(self,name,  speed = 30, eggs = 0 ):
        self.name = name
        self.speed = speed
        self.eggs = eggs

    def layeggs(self):
        self.eggs += 2



class Human(Mamal):
    pass



my_ovipar = Ovipar("Jean", 10, 0)

my_ovipar.layeggs()


my_mamal = Mamal("robert", 50, 3, True)

print(my_mamal)


