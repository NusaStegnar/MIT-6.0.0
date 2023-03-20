# Example of square root

x = 25
epsilon = 0.01
num_guess = 0
low = 1.0
high = x
answer = (high + low) / 2.0

while abs(answer ** 2 - x) >= epsilon:
    print("low = " + str(low) + "high = " + str(high) + " answer = " + str(answer))
    num_guess += 1
    if answer ** 2 < x:
        low = answer
    else:
        high = answer
    answer = (high + low) / 2.0
print("Num_guess = " + str(num_guess))
print(str(answer) + " is close to square root of " + str(x))


# Example for cube root


x = 27
epsilon = 0.01
num_guess = 0
low = 1.0
high = x
answer = (high + low) / 2.0

while abs(answer ** 3 - x) >= epsilon:
    print("low = " + str(low) + "high = " + str(high) + " answer = " + str(answer))
    num_guess += 1
    if answer ** 3 < x:
        low = answer
    else:
        high = answer
    answer = (high + low) / 2.0
print("Num_guess = " + str(num_guess))
print(str(answer) + " is close to cube root of " + str(x))

# Example of negative integer

x = - 27
epsilon = 0.01
num_guess = 0
low = x
high = - 1.0
answer = (high + low) / 2.0

while abs(answer ** 3 - x) >= epsilon:
    print("low = " + str(low) + "high = " + str(high) + " answer = " + str(answer))
    num_guess += 1
    if answer ** 3 < x:
        low = answer
    else:
        high = answer
    answer = (high + low) / 2.0
print("Num_guess = " + str(num_guess))
print(str(answer) + " is close to cube root of " + str(x))