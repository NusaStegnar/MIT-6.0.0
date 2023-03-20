""" break STATEMENT
 immediately exits whatever loop it is in
 skips remaining expressions in code block
 exits only innermost loop

while <condition_1>:
    while <condition_2>:
        <expression_a>
        break
        <expression_b>
    <expression_c> """

my_sum = 0
for i in range(5, 11, 2):
    my_sum += i
    if my_sum == 5:
        break 
print(my_sum)


# Break while loop

name = "Jesaa29 Roy"
size = len(name)
i = 0
# iterate loop till the last character
while i < size:
    # break loop if current character is space
    if name[i].isspace():
        break
    # print current character
    print(name[i])
    i = i + 1


# Break nested loop

# To terminate the nested loop, use a break statement inside the inner loop.
# In the following example, we have two loops, the outer loop, and the inner loop.
# The outer for loop iterates the first 10 numbers using the range() function
# the internal loop prints the multiplication table of each number.
# But if the current number of both the outer loop and the inner loop is greater than 5
# then terminate the inner loop using the break statement.

for i in range(1, 11):
    print("Multiplication table of" , i)
    for j in range(1, 11):
        # condition to break inner loop
        if i > 5 and j > 5:
            break
        print(i * j, end=" ")
    print(" ")


# Break outer loop

# To terminate the outside loop, use a break statement inside the outer loop.
# we have two loops, the outer loop and the inner loop
# The outer for loop iterates the first 10 numbers
# the internal loop prints the multiplication table of each number.
# But if the current number of the outer loop is greater than 5
# then terminate the outer loop using the break statement.

for i in range(1, 11):
    # condition to break outer loop
    if i > 5:
        break
    print("Multiplication table of", i)
    for j in range(1, 11):
        print(i * j, end=" ")
    print(" ")
