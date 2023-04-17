# FUNCTIONS
# write reusable piece/chunks of code, called functions
# functions are not run in a program until they are “called” or “invoked” in a program

# function characteristics:
    # has a name
    # has parameters (0 or more)
    # has a docstring (optional but recommended)
    # has a body

def is_even(i): # def = keyword, is_even = name, i = parameters or arguments
    """ 
    Input: i, a positive int returns True 
    if i is even, otherwise False 
    """ # specification, docstring; you can access them by using is_even.__doc__
   
    print("Hi")             # print and return are body; print evaluate some expressions
    return i % 2 == 0       # return is keyword that tells to stop commputing, 
                            # (i%2==0) is expresssion to evaluate and return

is_even(3) # later in the code, you call the function using it name and values for parameters
print(is_even.__doc__)

# Function without any parameters

def message():
    print("Welcome to PYnative")

# call function using its name

message()


# Function with two parameters

def course_func(name, course_name):
    print("Hello", name, ". Welcome to PYnative!")
    print("Your cours name is: ", course_name)

# call function
course_func("John", "Python") 


# Function with parameters and return value

def calculator(a, b):
    add = a + b
    return add
# call function
# take return value in variable
res = calculator(20, 5)

print("Addition: ", res)


