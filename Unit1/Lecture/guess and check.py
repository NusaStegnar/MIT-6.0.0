""" One way to use this idea of generating guesses in order to find a cube root of x is to first try 0**3, then 
1**3, then 2**3, and so on 
 Can stop when reach k such that k**3 > x
 Only a finite number of cases to try """

x = int(input("Enter an integer: "))
ans = 0

while ans ** 3 < x:
    ans = ans + 1
if ans ** 3 != x:
    print(str(x) + " is not a perfect cube")
else:
    print("Cube root of " + str(x) + " is " + str(ans))


x = int(input("Enter an integer: "))
ans = 0
while ans ** 3 < abs(x):
    ans = ans + 1
if ans ** 3 != abs(x):
    print(str(x) + " is not a perfect cube")
else:
    if x < 0:
        ans = - ans
    print("Cube root of " + str(x) + " is " + str(ans))

cube = 8
for guess in range(cube+1):
    if guess ** 3 == cube:
        print("Cube root of ", cube, " is ", guess)

cube = 8
for guess in range(abs(cube)+1):
    if guess ** 3 >= abs(cube):
        break
    if guess ** 3 != abs(cube):
        print(cube, "is not a perfect cube")
    else:
        if cube < 0:
            guess = -guess
    print("Cube root of " + str(cube) + " is " + str(guess))
