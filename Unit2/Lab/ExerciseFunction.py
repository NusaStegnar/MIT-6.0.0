# Exercise1: Create a function in Python

# Write a program to create a function that takes two arguments, name and age, and print their value.

def sun(name, age):
    print("Name,", name, ", age", age)

sun("Nusa", "40")

# Exercise2: Create a function with variable length of arguments

# Write a program to create function func1() to accept a variable length of arguments and print their value.

def func1(*args):
    for i in args:
        print(i)

func1(20, 40, 60)
func1(80, 100)

# Exercise3: Return multiple values from a function

# Write a program to create function calculation() such that it can accept two variables and calculate addition and subtraction. 
# Also, it must return both addition and subtraction in a single return call.

def calculation(a, b):
    x = a + b
    y = a - b
    return x, y

res = calculation(40, 10)
print(res)

# Exercise4: Create a function with a default argument

# Write a program to create a function show_employee() using the following conditions.
# It should accept the employee’s name and salary and display both.
# If the salary is missing in the function call then assign default value 9000 to salary

def show_employee(name, salary = 9000):
    print("Name: ", name,", Salary: ", salary)

show_employee("Ben", 12000)
show_employee("Jessa")

# Exercise5: Create an inner function to calculate the addition in the following way

# Create an outer function that will accept two parameters, a and b
# Create an inner function inside an outer function that will calculate the addition of a and b
# At last, an outer function will add 5 into addition and return it

def outer_function(a, b):

    def inner_function(a, b):
        x = a + b
        return x
    # call inner function from outer function
    add = inner_function(a, b)
    # add 5 to the result
    y = 5 + add
    return y
    
result = outer_function(5, 10)
print(result)
