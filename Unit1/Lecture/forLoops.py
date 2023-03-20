""" CONTROL FLOW: for LOOPS

for <variable> in range(<some_num>):
    <expression>
    <expression> 
...
 each time through the loop, <variable> takes a value
 first time, <variable> starts at the smallest value
 next time, <variable> gets the prev value + 1
 etc. """

for n in range(12):
    print(n)

for x in range(10):
    print(x)

sum = 0
for n in range(2, 22, 2):
    sum = sum + n
print(sum)

# Calculate the square of each number of list

numbers = [1, 2, 3, 4, 5]
# iterate over ech element in list num
for i in numbers:
    # ** exponent operation
    square = i ** 2
    print("Square of: ", i, "is", square)


# Calculate the average of list of numbers

numbers = [10, 20, 30, 40, 50]
# definite iteration
# run loop 5 times because list contains 5 items
sum = 0
for i in numbers:
    sum = sum + i
    list_size = len(numbers)
    average = sum/list_size
print(average)


# Print all even and odd numbers

for i in range(0, 21):
    if i % 2 == 0:
        print("Even number: ", i)
    else:
        print("Odd number:", i)

# Use for loop to generate a list of numbers from 9 to 50 divisible by 2.

for i in range(9, 51):
    if i % 2 == 0:
        print(i)


# Break the loop if number is greater than 15

numbers = [1, 4, 7, 8, 15, 20, 35, 45, 55]
for i in numbers:
    if i > 15:
        #break the loop
        break
    else:
        print(i)

# Count the total number of "m" in a giving string

name = "mariya mennen"
count = 0
for char in name:
    if char != "m":
        continue
    else:
        count = count + 1
print("Total number of m is: ", count)


# pass statements

num = [1, 4, 5, 3, 7, 8]
for i in num:
    #calculate multiplication in future if required
    pass 

# Else block in for loop

for i in range(1, 6):
    print(i)
else:
    print("Done")

# Both break and else statement

count = 0
for i in range(1, 6):
    count = count + 1
    if i > 2:
        break
    else:
        print(i)
else:  
    print("Done")
