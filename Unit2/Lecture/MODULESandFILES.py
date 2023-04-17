# MODULES

# the file circle.py contains
pi = 3.14159
def area(radius):
    return pi*(radius ** 2)
def circumference(radius):
    return 2 * pi * radius
# we can import and use this module (circle.py)

import circle
pi  = 3
print(pi)
# 3
print(circle.pi)
# 3.14159
print(circle.area(3))
# 28.27431
print(circle.circumference(3))
# 18.849539999999998

# if we don't want to refer to functions and variables by their module, 
# and the names don't collide with other bindings,
# then we can use:

from circle import *
print(pi)
# 3
print(area(3))
# 3.14159

# this has the effect of creating bindings 
# within the current scope for all objects defined within circle
# statements within a module are executed 
# only the first time a module is imported

# FILES

# need a way to save our work for later use
# every operating system has its own way of handling files; 
# Python provides an operating-system independent means to access files, 
# using a file handle

name_handle = open("kids", "w")
# creates a file named kids 
# and returns file handle which we can name and thus reference. 
# The "w" indicates that the file is to opened for writing into.

name_handle = open("kids", "w")
for i in range(2):
    name = input("Enter name: ")
    name_handle.write(name + "\n")
name_handle.close()

# The "r" indicate that the file is opened for read.

name_handle = open("kids", "r")
for line in name_handle:
    print(line)
name_handle.close()
                      