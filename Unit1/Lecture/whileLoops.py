""" while <condition>:
    <expression>
    <expression>
...
 <condition> evaluates to a Boolean
 if <condition> is True, do all the steps inside the 
while code block
 check <condition> again
 repeat until <condition> is False """

""" n = input("You are in the Lost Forest. Go left or right? ")
while n == "right":
    n = input("You are in the Lost Forest. Go left or right? ")
print("You got out of the Lost Forest!") """
""" 

n = 0
while n < 5:
    print(n)
    n = n + 1

e = 2
while e < 4:
    print(e)
    e = e + 1

for n in range(5):
    print(n)

for e in range(4):
    print(e)

# Print numbers less than 5

i = 1
# run loop till i is less than 5 
while i < 5:
    print(i)
    i = i + 1

# Check how many times a given number can be divided by 3 before it is less than or equal to 10.

count = 0
num = int(input("Enter a number: "))

while num > 10:
    # divide number by 3
    num = num / 3
    # increase count
    count = count + 1
print("Total iteration required", count)


x = int(input("Enter a number:"))
y = 0

while x / 3:
    print("Total iteration required", y)
    y = y + 1
    if x >= 10:
        break

# Print even and odd numbers between 1 to the entered number.

n = int(input("Enter a number: "))
while n > 0:
    # Check even and odd
    if n % 2 == 0:
        print(n, "is an even number.")
    else:
        print(n, "is an odd number.")
    # decrease number by 1 in each iteration
    n = n - 1 """

# Reverse while loop
# Reverse a while loop to display numbers from 10 to 1

i = 10
while i >= 0:
    print(i)
    i = i - 1

# while loop to iterate string letter by letter

name = "Jessa"
i = 0
x = len(name) - 1
while i <= x:
    print(name[i])
    i = i + 1

# Iterate a List using while loop
# Use while loop to iterate over a list

numbers = [1, 2, 4, 5, 7 ]
size = len(numbers)
i = 0
while i < size:
    print(numbers[i])
    i = i + 1
