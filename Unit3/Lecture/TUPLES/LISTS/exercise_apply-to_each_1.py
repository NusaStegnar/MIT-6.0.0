def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

test_list = [1, -4, 8, -9]

def timesFive(a):
    return a * 5

applyToEach(test_list, timesFive)
print(test_list)
# [5, -20, 40, -45]

test_list = [1, -4, 8, -9]

def absolute(a):
    return abs(a)

applyToEach(test_list, absolute)
print(test_list)
# [1, 4, 8, 9]


test_list = [1, -4, 8, -9]

def calculate(a):
    return a + 1

applyToEach(test_list, calculate)
print(test_list)
# [2, -3, 9, -8]


test_list = [1, -4, 8, -9]

def multiple_with_each_other(a):
    return a * a

applyToEach(test_list, multiple_with_each_other)
print(test_list)
# [1, 16, 64, 81]