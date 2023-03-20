# Use range() to generate a sequence of numbers starting from 9 to 100 divisible by 3.

for i in range(9, 100):
    if i % 3 == 0:
        print(i)

for i in range(9, 100, 3):
    print(i)

# Use for loop with range() function to print the odd numbers between 1 and 10.

for i in range(1, 10, 2):
    print(" Current value of i is:", i )

# Print the following number pattern using range() and a loop.
1 
2 2 
3 3 3 



for i in range(4):
    for j in range(i):
        print(i, end=" ")
    print() # new line after each row to show pattern correctly

n = "*"
for i in range(8):
    for j in range(i):
        print(n, end=" ")
    print() 


# loop in a reverse iteration or backward iteration to display a range of numbers from 5 to 0.

# reverse range using negative step
# start = 5
# stop = -1
# step = -1

for i in range(5, -1, -1):
    print(i)
    
#  reverse range starting from 20 to 10

for i in reversed(range(10, 21)):
    print(i)

# reverse range starting from 20 to 10 with step 2

for i in reversed(range(10, 21, 2)):
    print(i)

# Negative range from -1 to -10
# print the range of numbers from negative to positive.

for i in range(-1, -11, -1):
    print(i)

# Negative reverse range from -10 to -1
# print the negative reverse range() using a positive step integer.

for i in range(-10, 0, 1):
    print(i) 

# Combination of negative and positive numbers

start = 2
stop = - 5
step = - 1

for i in range(2, - 5, - 1):
    print(i)

