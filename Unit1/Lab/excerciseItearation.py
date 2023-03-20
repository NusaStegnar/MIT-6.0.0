x = 5
answer = 0
iterationsLeft = x

while iterationsLeft != 0:
    answer = answer + x
    iterationsLeft = iterationsLeft - 1
print(str(x) + "x" + str(x) + "=" + str(answer))


num = 5
if num > 2:
    print(num)
    num -= 1
print(num)

num = 10
for num in range(5):
    print(num)
print(num)

divisior = 2
for num in range(0,10,2):
    print(num/divisior)


for variable in range(20):
    if variable % 4 == 0:
        print(variable)
    if variable % 16 == 0:
        print("Foo!")

for letter in "hola":
    print(letter)

count = 0
for letter in "Snow!":
    print("Letter #" + str(count) + "is" + str(letter))
    count += 1
    break
print(count)

my_Str = "6.00x"
for char in my_Str:
    print(char)
print("Done")

greeting = "Hello!"
count = 0

for letter in greeting:
    count += 1
    if count % 2 == 0:
        print(letter)
    print(letter)
print("Done")


school = "Massachusetts Institute of Technology"
numVowels = 0
numCons = 0

for char in school:
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        numVowels += 1
    elif char == "o" or char == "M":
        print(char)
    else:
        numCons -= 1

print("numVowels is: " + str(numVowels))
print("numCons is: " + str(numCons)) 