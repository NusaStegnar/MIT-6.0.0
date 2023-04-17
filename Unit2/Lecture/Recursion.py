# Recursion means a defined function can call itself.
# Example:
# tri_recursion() is a function that we have defined to call itself ("recurse"). 
# We use the k variable as the data, which decrements (-1) every time we recurse. 
# The recursion ends when the condition is not greater than 0 (i.e. when it is 0).

def tri_recursion(k):
    if (k > 0):
        result = k + tri_recursion(k - 1)
    else:
        result = 0
    return result
print("\n\nRecursion Example Results")
tri_recursion(6)  


# “multiply a * b” is equivalent to “add a to itself b times”
# capture state by an iteration number (i) starts at b
# i <-- i-1 and stop when 0
# a current value of computation (result)
# result <-- result + a

# ITERATIVE SOLUTION
def mult_iter(a, b):
    result = 0
    while b > 0:       # iteration
        result += a    # current value of computation
        b -= 1         # a running sum
    return result      # current value of iteration variable

# RECURSIVE SOLUTION
def mult(a, b):
    if b == 1:         # base case (keep reducing problem until reach a simple case that can be solved directly)
        return a       # when b=1, a*b=a
    else:              # recursive step (think how to reduce problem to a simpler/smaller version of same problem)
        return a + mult(a, b - 1)
    

# FACTORIAL
# n! = n*(n-1)*(n-2)*(n-3)*...* 1
# what n do we know the factorial of?
# n = 1    -->  if n == 1:, return 1   ---> BASE CASE
# how to reduce problem? Rewrite in terms of something simpler to reach base case
# n*(n-1)! -->  else:, return n*factorial(n-1) ----> RECURSIVE STEP
    

