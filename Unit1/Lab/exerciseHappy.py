# Write a piece of Python code that prints out the string 'hello world' 
# if the value of an integer variable, happy, is strictly greater than 2.

""" happy = 3

if happy > 2:
    print("hello world")

num = 0
while num <=5:
    print(num)
    num+=1
print("outside of loop")
print(num)

num = 5
if num>2:
    print(num)
    num-=1
print(num)    

num_of_loops = 0
num_of_apples = 2

while num_of_loops<10:
    num_of_apples *=2
    num_of_apples += num_of_loops
    num_of_loops -=1
print("Number of apples: " + str(num_of_apples)) """

""" num = 10

while num > 3:
    num -= 1
    print(num)

num = 8

while num < 10:
    num += 1
    print(num) """

num = 10

while True:
    if num < 7:
        print("breaking out of loop")
        break
    print(num)
    num -= 1
print("outside of loop")

