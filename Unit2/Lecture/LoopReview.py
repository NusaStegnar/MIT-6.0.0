answer = 0
neg_flag = Falsex = int(input("Enter an integer: "))

if x < 0:
    neg_flag = True
while answer ** 2 < x:
    answer = answer + 1
if answer ** 2 == x:
    print("Square root of", x, "is", answer)
else:
    print(x, "is not a perfect square")
    if neg_flag:
        print("Just checking ... did you mean", x, "?")
        