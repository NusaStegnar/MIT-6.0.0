# Write an iterative function iterPower(base, exp) 
# that calculates the exponential baseExp by simply using successive multiplication. 
# For example, iterPower(base, exp) should compute baseExp by multiplying base times itself exp times. 
# Function should take in two values - 
# base can be a float or an integer; 
# exp will be an integer >= 0. It should return one numerical value. 
# Your code must be iterative - use of the ** operator is not allowed.
def iterPower(base, exp):
    """ 
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    """
    result = 1
    while exp > 0:
        result * base
        exp -= 1
    return result



