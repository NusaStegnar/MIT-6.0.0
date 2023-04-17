# Calling Functions

def f(x):    # defining a function called f   (x = formal parameter)
    x = x + 1
    print("In f(x): x = ", x)
    return x
x = 3  # binding x with 3
z = f(x)  #call f with a value of x in bind that to z    (x = actual parameter)

# No return function

def is_even(i):
    """ 
    Input: i, a positive int, does not return anything
    """
    i % 2 == 0    # without a return statement


# Python returns the value NONE, if no return given
# represents the absence of value


# Functions as arguments

def func_a():  # has no parameters
    print("inside func_a")
def func_b(y): # has one parameter y
    print("Inside func_b")
    return y
def func_c(z): # has one parameters z
    print("Inside func-C")
    return z()

print(func_a())         # cal func_a, take no parameters
print(5 + func_b(2))    # call func_b, take one parameter, in this case 2
print(func_c(func_a))   # call func_c, takes one parameter, that is another function

# Example

def even_odd(n):
    # check if num is even or odd
    if n % 2 == 0:
        print("Even number")
    else:
        print("Odd number")
# calling function by its name
even_odd(19)
# Output is Odd number

