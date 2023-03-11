""" PRINT
 used to output stuff to console
 keyword is print

x = 1
print(x)

x_str = str(x)

print("My favorite number is", x, ". ", "x =", x)
print("My favorite number is " + x_str + ". " + "x = " + x_str)
print("My favourite number is " + str(x) + ". " + "x = " + str(x))

#input

 prints whatever is within the quotes
 user types in something and hits enter
 returns entered sequence
 can bind that value to a variable so can reference

text = input("Type anything... ")
print(text)
 input returns a string so must cast if working with numbers

num = int(input("Type a number... "))
print(5*num) """

box = input("write smething special: ")
print(box)
print(5*box)
print(type(box))

number = int(input("Write the number of your choice: "))
print(number)
print("The number of my choise is: " + str(number))
print("My favourite nuber is " + str(number) + ", but I do not know why.")