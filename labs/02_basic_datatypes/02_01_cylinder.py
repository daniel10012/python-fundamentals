import math

radius = 3.14
height = 5
pi = math.pi

volume = pi * radius**2 * height
surface = ((2*pi*radius) * height) + ((pi*radius**2)*2)

v = round(volume,2)
s = round(surface,2)

print ("Volume is:", v)
print ("Surface is:", s)


'''
Write the necessary code calculate the volume and surface area
of a cylinder with a radius of 3.14 and a height of 5. Print out the result.


'''