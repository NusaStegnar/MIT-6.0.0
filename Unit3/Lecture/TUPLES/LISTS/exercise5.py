def apply_each_to(L, x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result

def square(a):
    return a * a

def halve(a):
    return a / 2

def inc(a):
    return a + 1


apply_each_to([inc, square, halve, abs], -3)
# [-2, 9, -1.5, 3]
apply_each_to([inc, square, halve, abs], 3.0)
# [4.0, 9.0, 1.5, 3.0]
apply_each_to([inc, max, int], -3)
# error