# The factorial of a positive integer n is the result multiplying all the integers less than or equal to n. 
# The factorial of 3 is 3 * 2 * 1 (by convention, the factorial of 0 is 1) 
# Factorial is denoted as n! in mathematics.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial (n - 1)
factorial(3)
