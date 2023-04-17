low = 0
high = 100
uinput = ''

print("Please think of your secret number between 0 and 100!")

while uinput != "c":
    ans = (high + low)//2
    
    print("Is it ", ans, "?")
    uinput = input("Enter h if the guess is too high. Enter l if the guess is to low. Enter c if I guess corecctly: ")

    if uinput == "h":
        high = ans
    elif uinput == "l":
        low = ans
    elif uinput == "c":
        print("Game over. Your secret number was: ", ans)
    else:
        print("Sorry, I did not understand your input.")


#Complexty
#test = [1, 2, 345, 5, 55, 66, 78, 66]
#O(n)
#sort O(log(n))
#test = [1, 2, 5, 55, 66, 66, 78, 345]
#bisection O(log(n))
# => O(2*log(n))
