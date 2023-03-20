# Indexing
""" 
s = "abc"
len(s) = evaluates to 3
s[0] = evaluates to "a"
s[1] = evaluates to "b"
s[3] = trying to index out of bounds, KeyError

# strings can slice using [start:stop:step]

s = "abcdefgh"
s[::-1] = evaluates to "hgfedcba"
s[3:6] = evaluates to "def"
s[-1] = evaluates to "h"

# string are immutable - cannot be modified

s = "hello"
s[0] = "y"  - gives an error
s = "y" + s[1:len(s)] - is allowed but gives new object  s = "yello" """

# strings and loop

""" s = "abcdefgh"

for index in range(len(s)):
    if s[index] == "i" or s[index] == "u":
        print("there is an i or u")

for char in s:
    if char == "i" or char == "u":
        print("There is an i or u") """

an_letters = "aefhilmnorsxAEFHILMNORSX"

word = input("I will cheer for you! Enter a word: ")
times = int(input("Enthusiasm level (1-10): "))
i = 0

while i < len(word):
    char = word[i]
    if char in an_letters:
        print("Give me an", char, "!", char)
    else:
        print("Give me a", char, "!", char)
    i = i + 1
print("What does thar spell?")
for i in range(times):
    print(word, "!!!")