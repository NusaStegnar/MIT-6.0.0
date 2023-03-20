# if - elif - else

number = 6
if number > 5:
    #Calculate square
    print(number * number)
print("Next lines of code")


password = input("Enter password: ")

if password is "nseFFjwjucf":
    print("Correct password")
else:
    print("Incorrect password")


def user_check(choice):
    
    if choice == 1:
        print("Admin")
    elif choice == 2:
        print("Editor")
    elif choice == 3:
        print("Guest")
    else:
        print("Wrong entry")

user_check(1)
user_check(2)
user_check(3)
user_check(4)


# Find a greater number between two numbers

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 >= num2:
    if num1 == num2:
        print(num1, "and", num2, "are equal")
    else:
        print(num1, "is greater than", num2)
else:
    print(num1, "is smaller than", num2)


# Single statement suites

number = 59
if number > 0: print("Positive")
else: print("Negative")

x= 1
while x <= 5: print(x, end=""); x = x+1

# for and while loop

for i in range(1, 11):
    print(i)


num = 10
sum = 0
i = 1
while i <= num:
    sum = sum + i
    i = i + 1
print("Sum of first ten number is:", sum)

# break, continue, pass

for num in range(10):
    if num > 5:
        print("Stop processing.")
        break
    print(num)    


for num in range(3,8):
    if num == 5:
        continue
    else:
        print(num)


months = ["January", "June", "March", "April"]
for mon in months:
    pass
print(months)