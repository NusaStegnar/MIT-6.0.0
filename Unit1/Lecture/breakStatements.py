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