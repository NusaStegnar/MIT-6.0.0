# Convert the following into code that uses a while loop.

""" prints 2
prints 4
prints 6
prints 8
prints 10
prints Goodbye! """

""" i = 0
for i in range(2,11,2):
    print(i)
print("Goodbye")

num = 2
while num <= 10:
    print(num)
    num += 2
print("Goodbye") """

# Convert the following into code that uses a while loop.

""" prints Hello!
prints 10
prints 8
prints 6
prints 4
prints 2 """

""" print("Hello!")
num = 10
while num <= 10:
    if num < 2:
        break
    print(num)
    num -= 2 """

# Write a while loop that sums the values 1 through end, inclusive. End is a variable that we define for you. 
# So, for example, if we define end to be 6, your code should print out the result:
# 21 which is 1 + 2 + 3 + 4 + 5 + 6.
# For problems such as these, do not include input statements or define variables we will provide for you. 
# Our automating testing will provide values so write your code in the following box assuming these variables 
# are already defined.

total = 0
current = 1

while current <= 6:
    total += current
    current += 1
print(total)