# Assume the two files below are in the same folder. 
# You run inventory.py. What happens?

# batteries.py

aa = "AA"
aaa = "AAA"
c = "C"
d = "D"

# FILE: inventory.py

aa = "aa"
triple_A = "aaa"
print(aa)

# prints aa

# Assume the two files below are in the same folder. 
# You run inventory.py. What happens?

# FILE: batteries.py
aa = "AA"
aaa = "AAA"
c = "C"
d = "D" 

# FILE: inventory.py
aa = "aa"
tripleA = "aaa"
# print(batteries.aa)

# There is an error

# Assume the two files below are in the same folder. 
# You run inventory.py. What happens?

# FILE: batteries.py

aa = "AA"
aaa = "AAA"
c = "C"
d = "D" 

# FILE: inventory.py

# import batteries
aa = "aa"
tripleA = "aaa"
# print(batteries.aa)

# prints AA

# Assume the two files below are in the same folder. 
# You run inventory.py. What happens?

# FILE: batteries.py

aa = "AA"
aaa = "AAA"
c = "C"
d = "D" 

# FILE: inventory.py

# from batteries import *
aa = "aa"
print(aa, aaa, c, d)

# aa AAA C D

