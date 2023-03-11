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
