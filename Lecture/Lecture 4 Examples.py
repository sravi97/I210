import math
radius = int(input("Please enter a radius: "))
height = int(input("Please enter a height: "))
area = (2 * math.pi * radius * height) + (2 * math.pi * radius * radius)
print ("The surface area is: " + str(area))
