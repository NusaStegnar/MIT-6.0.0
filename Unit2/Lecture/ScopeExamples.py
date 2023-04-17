# inside a function, can access a variable defined outside
# inside a function, cannot modify a variable defined outside

def f(y):
    x = 1           # x is re-defined in scope of f
    x += 1
    print(x)        

x = 5
f(x)                # different x object
print(x)            # this x is printed from global/main scope


def g(y):
    print(x)        # take x from outside g
    print(x + 1)

x = 5               # x inside g is picked up from scope that called function g
g(x)
print(x)            # this x is printed from global/main scope


def h(y):
    x = x + 1       # unboundLocalError: local variable "x" referenced before assignment

x = 5
h(x)
print(x)            # this x is printed from global/main scope


def g(x):
    def h():
        x = "abc"
    x = x + 1
    print("In g(x): x = ", x)
    h()
    return x

x = 3
z = g(x)
