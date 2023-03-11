""" compute the right hand side  VALUE
 store it (aka bind it) in the left hand side  VARIABLE
 left hand side will be replaced with new value
 = is called assignment

x = 2
x = x*x
y = x+1 """

swap variables 
– is this ok?

x = 1
y = 2
y = x
x = y
print(x)
print(y)


swap variables 
– this is ok!

x = 1
y = 2
temp = y
y = x
x = temp
print(x)
print(y)


# Examples swaping

a = 1
b = 4
c = 3
d = 2

temp = b
b = c
c = temp
print(c)
print(b)

