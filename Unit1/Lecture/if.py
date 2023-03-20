""" The simplest branching statement is a conditional
◦ A test (expression that evaluates to True or False)
◦ A block of code to execute if the test is True
◦ An optional block of code to execute if the test is False """

""" x = int(input("Enter an integer: ")) """
""" if x % 2 == 0:
    print("")
    print("Even")
else:
    print("")
    print("Odd")
print("Done with conditional!") """

""" x = int(input("Enter an integer: "))
if x % 2 == 0:
    if x % 3 == 0:
        print("Divisible by 2 and 3.")
    else:
        print("Divisible by 2 and not by 3.")
elif x % 3 == 0:
    print("Divisible by 3 and not by 2.") """

""" x = 4
y = 8
z = 2

if x < y and x < z:
    print("x is least")
elif y < z:
    print("y is least")
else:
    print("z is least") 


<condition> has a value True or False
evaluate expressions in that block if <condition> is True """

x = float(input("Enter as number for x: "))
y = float(input("Enter a number for y: "))

if x == y:
    print("x and y are equal!")
    if y != 0:
        print("Therefore, x/y is ", x/y)
elif x < y:
    print("x is smaller!")
else:
    print("y is smaller!")
print("Thanks!!")