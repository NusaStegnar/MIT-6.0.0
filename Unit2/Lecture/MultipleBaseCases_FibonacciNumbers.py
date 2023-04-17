# Fibonacci numbers
# Leonardo of Pisa (aka Fibonacci) modeled the following challenge
# Newborn pair of rabbits (one female, one male) are put in a pen
# Rabbits mate at age of one month
# Rabbits have a one month gestation period
# Assume rabbits never die, 
# and female always produces one new pair (one male, one female) every month from its second month on.
# How many female rabbits are there at the end of one year?

# FIBONACCI
# After one month (call it 0) – 1 female
# After second month – still 1 female (now pregnant)
# After third month – two females, one pregnant, one not
# In general, females(n) = females(n-1) + females(n-2)
# Every female alive at month n-2 will produce one female in month n;
# These can be added those alive in month n-1 to get total alive in month n

# Base cases: females(0) = 1, Females(1) = 1
# Recursive step: Females(n) = Females(n - 1) + Females(n - 2)
def fib(x):
    """ 
    assume x an int >= 0
    returns Fibonacci of x
    """
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)