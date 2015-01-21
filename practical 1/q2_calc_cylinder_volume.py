__author__ = 'dhs'
from math import pi

radius = float(input("Tell me the radius of your cylinder"))
length = float(input("Tell me the length of your cylinder"))

print("So the radius is", radius)
print("And the length is", length)
print("The area of your cylinder is", radius*radius*pi)
print("The volume of your cylinder is", radius*radius*pi*length)