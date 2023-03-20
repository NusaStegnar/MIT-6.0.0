""" range(start,stop,step)

 default values are start = 0 and step = 1 and is optional
 loop until value is stop - 1  """

my_sum = 0
""" for i in range(7, 10):
    my_sum += i
    print(my_sum) """

for i in range(5, 11, 2):
    my_sum += i
    print(my_sum)

# Generate numbers between 0 to 6
for i in range(6):
    print(i)

for i in range(-1, -11, -1):
    print(i)

for i in range(0, 7 + 3, 2):
    print(i)

for i in range(0, 10)[5]:
    print(i)

for i in range(10)[3:8]:
    print(i)

for i in range(2, 15)[4:11]:
    print(i)

for i in range(12, 25)[3:9]:
    print(i)

for i in range(5).start, range(5).stop, range(5).step:
    print(i)

# print first 10 numbers
# stop = 10
for i in range(10):
    print(i, end=" ") 
# end=" " print v isti vrstici

# Numbers from 10 to 15
# start = 10
# stop = 16
for i in range(10, 16):
    print(i, end=" ")

# Numbers from 10 to 15
# start = 10
# stop = 50
# step = 5
for i in range(10, 50, 5):
    print(i, end=" ")