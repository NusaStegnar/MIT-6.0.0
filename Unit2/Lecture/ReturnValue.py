# Return statement is used to return value from the function
# The return value is nothing but a outcome of function.
# The return statement ends the function execution.
# For a function, it is not mandatory to return a value.
# If a return statement is used without any expression, then the None is returned.
# The return statement should be inside of the function block.

def is_even(list1):
    even_num = []
    for n in list1:
        if n % 2 == 0:
            even_num.append(n)
    # return a list
    return even_num
# pass list to the function
even_num = is_even(2, 3, 5, 78, 14, 16, 59, 80)
print("Even numbers are: ", even_num)