a = 10
def f(x):
    return x + a
a = 3
f(1)
# output = 4

x = 12
def g(x):
    x = x + 1
    def g(y):
        return x + y
    return g(6)
g(x)
# output = 19