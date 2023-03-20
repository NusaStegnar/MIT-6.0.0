""" # Write a program to print the following number pattern using a loop

1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5

print("Number Pattern")  

# decide the row count.
row = 5
# start: 1
# stop: row + 1 (range never include stop number in result)
# step: 1
# run loop 5 times

for i in range(1, row + 1, 1):
    # run inner loop i + 1 times
    for j in range(1, i + 1):
        print(j, end=" ")
        # empty line after each row
    print(" ")

row = 10

for i in range(1, row + 1,):
    for j in range(1, j + 2):
        print(" * ", end= " ")
    print(" * ") """

# Calculate the sum of all numbers from 1 to a given number

""" x = int(input("Enter a number: "))
m = 0

for i in range(1, x+1):
    m = m + i
print(m)

# Write a program to print multiplication table of a given number

 
for i in range(4, 41):
    if i % 4 == 0:
        print(i)
    else:
        pass

n = 4

for i in range(1, 41):
    z = i * n
    print(z) """
    
# Display numbers from a list using loop
# Write a program to display only those numbers from a list that satisfy the following conditions
# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the next number
# If the number is greater than 500, then stop the loop

numbers = [12, 75, 150, 180, 145, 525, 50]

for i in numbers:
    if i > 500:
        break
    if i > 150:
        continue
    if i % 5 == 0:
        print(i) 


# Count the total number of digits in a number

count = 0
num = 75869

while num != 0:
    num = num // 10
    count += 1
print("Total digits are: ", count)


# Print the following pattern (RAZLAGA RAZLIKE)

5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1

n = 5
k = 5

for i in range(0,n+1):
    for j in range(k-1,0,-1):
        print(j,end=" ")
    print()


n = 5
k = 5
for i in range(0,n+1):
    for j in range(k-i,0,-1):
        print(j,end=' ')
    print()

# Display numbers from -10 to -1 using for loop

for i in range(-10, 0, 1):
    print(i)


# Use else block to display a message “Done” after successful execution of for loop

for i in range(5):
    print(i)
else:
    print("Done")

# Write a program to display all prime numbers within a range

# range
start = 25
stop = 50

print("Prime numbers between", start, "and", stop, "are:")

for i in range(25, 51, 1):
    # all prime numbers are greater than 1
    # if number is less than or equal to 1, it is not prime
    if i > 1:
        for j in range(2, i):
            # check for factors
            if i % j == 0:
                # not a prime so break inner loop
                #look for next number
                break
        else:
            print(i)

# Calculate the cube of all numbers from 1 to a given number 6
# Write a program to rint the cube of all numbers from 1 to a given number

input_number = 6


for i in range(1, 7): 
    x = i ** 3
    print("Current Number is: ", i, "and the cube is", x)


# Print the following pattern
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
# Write a program to print the following start pattern using the for loop

n = "*"
row = 5

for i in range(0, row):
    for j in range(0, i + 1):
        print(n, end=" ")
    print("/r")     
for i in range(row, 0, -1):
        for j in range(0, i - 1):
            print(n, end=" ")
        print("/r")

