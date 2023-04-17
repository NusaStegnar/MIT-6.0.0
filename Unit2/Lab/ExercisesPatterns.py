num = 0
while num < 10:
    num += 1
    print(num)

# pattern number 

row = 6


for i in range(row + 1):
    for j in range(i):
        print(i, end="")
    print("")

""" 
1
22
333
4444
55555
666666 
"""

# Pyramid pattern of numbers

rows = 5

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print("")

""" 
1
12
123
1234
12345 
"""

# Inverted pyramid pattern of numbers

rows = 5
b = 0

for i in range(rows, 0, - 1):
    b += 1
    for j in range(1, i + 1):
        print(b, end="")
    print("\r")

""" 
11111
2222
333
44
5 
"""

# Inverted Pyramid pattern with the same digit

row = 5
num = row
# reverse for loop
for i in range(row, 0, -1):
    for j in range(0, i):
        print(num, end="")
    print("")


""" 
55555
5555
555
55
5 
"""

# Another inverted half pyramid pattern with number

row = 5

for i in range(row, 0, - 1):
    for j in range(1, i + 1):
        print(j, end="")
    print("")


""" 
12345
1234
123
12
1 
"""

# Alternate numbers pattern using while loop

row = 5
i = 1

while i <= rows:
    j = 1
    while j <= i:
        print((i * 2 - 1), end="")
        j = j + 1
    i = i + 1
    print("")


""" 
1
33
555
7777
99999 
"""

# Reverse number pattern or inverted pyramid of descending numbers

row = 5
# reverse loop
for i in range(row, 0, -1):
    num = i
    for j in range(0, i):
        print(num, end="")
    print("\r")


""" 
55555
4444
333
22
1 
"""

# Reverse Pyramid of Numbers

row = 6
for i in range(1, row):
    for j in range(i, 0, -1):
        print(j, end="")
    print("")


""" 
1
21
321
4321
54321 
"""

# Another reverse number pattern

row = 5
for i in range(0, row + 1):
    for j in range(row - i, 0, -1):
        print(j, end="")
    print("")


""" 
54321
4321
321
21
1  
"""

# Print reverse number from 10 to 1

start = 1
stop = 2
current_num = stop
for row in range(2, 6):
    for col in range(start, stop):
        current_num = current_num - 1
        print(current_num, end="")
    print("")
    start = stop
    stop = stop + row
    current_num = stop



""" 
1
32
654
10987 
"""

# Same number triangle pattern

row = 6
for i in range(1, row):
    num = 1
    for j in range(row, 0, -1):
        if j > i:
            print(" ", end="")
        else:
            print(num, end="")
    print("")


""" 
     1
    11
   111
  1111
 11111 
"""

# Number triangle pattern

row = 6
for i in range(1, row):
    num = 1
    for j in range(row, 0, -1):
        if j > i:
            print(" ", end="")
        else:
            print(num, end="")
            num = num + 1
    print("")

    
 """ 1
    12
   123
  1234
 12345 
"""