""" Assume s is a string of lower case characters. 
Write a program that prints the number of times the string 'bob' occurs in s. 
For example, if s = 'azcbobobegghakl', then your program should print
Number of times bob occurs is: 2 """

""" s = "azcbobobegghakl"
count = 0
char = 0

while True:
    char = s.find("bob", char)
    if char >= 0:
        count += 1
        char += 1
    else:
        break
print("Number of times bob occurs is: " + str(count))  """



""" s = "azcbobobegghakl"
count = 0
phrase = "bob"

for i in range(len(s) - len(phrase) + 1):
    if s[i:i+len(phrase)] == phrase:
         count += 1
print("Number of times bob occurs is: " + str(count))  """


""" for char in s:
    while True:
        if char == phrase[0]:
            char += str(1)
        if len(str(char)) != len(phrase):
            char += str(1)
        if char == phrase[ :]:
            count += 1
print("Number of times bob occurs is: " + str(count)) """

# My own example

# Input
""" s = "molllllllllllllllllllllllllllllllllaranizaveslokanaslovelovekanaradavelovelovimoloka"
phrase = "lov"

def variant1():
    # Internal
    count = 0
    for index in range(len(s)):
        if phrase == s[index:index + len(phrase)]:
            count += 1
    print("Number of times love occure is: " + str(count))

variant1()


for char in s[::len(phrase)]:
    print(char) """


s = "azcbobobegghakl"
x = "bob"
i = 0

for char in range(len(s)):
    if x == s[char: char + len(x)]:
        i = i + 1         
print(i)

s = 'azcbobobegghakl'
bob_count = 0 

for i in range(len(s)):
    if s[i:i+3] == "bob":
        bob_count += 1

print("Number of times bob ocurrs is:", bob_count)