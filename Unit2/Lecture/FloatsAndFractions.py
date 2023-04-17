# Decimal number:
# 302 = 3*102 + 0*101 + 2*100
# Binary number
# 10011 = 1*24 + 0*23 + 0*22 + 1*21 + 1*20
# (which in decimal is 16 + 2 + 1 = 19)

# Internally, computer represents numbers in binary

# Converting decimal integer to binary

#Consider example of

# x = 1*24 + 0*23 + 0*22 + 1*21 + 1*20 = 10011
# If we take remainder relative to 2 (x%2) of this number, that gives us the last binary bit
# If we then divide x by 2 (x//2), all the bits get shifted right
# x//2 = 1*23 + 0*22 + 0*21 + 1*20 = 1001
# Keep doing successive divisions; now remainder gets next bit, and so on
# Let’s us convert to binary form

num = 19

if num < 0:
    is_Neg = True
    num = abs(num)
else:
    is_Neg = False
    result = ""
if num == 0:
    result = "0"
while num > 0:
    result = str(num % 2) + result
    num = num // 2
if is_Neg:
    result = " - " + result
print(result)

# Fractions

# 3/8 = 0.375 = 3*10-1 + 7*10-2 + 5*10-3
# So if we multiply by a power of 2 big enough to convert into a whole number, can then convert to 
# binary, and then divide by the same power of 2
# 0.375 * (2**3) = 3 (decimal)
# Convert 3 to binary (now 11)
# Divide by 2**3 (shift right) to get 0.011 (binary)

x = float(input('Enter a decimal number between 0 and 1: '))

p = 0

while ((2 ** p) * x) % 1 != 0:
    print('Remainder = ' + str((2 ** p) * x - int((2 ** p) * x)))
    p += 1

num = int(x * (2 ** p))

result = " "
if num == 0:
    result = "0"
while num > 0:
    result = str(num % 2) + result
    num = num//2

for i in range(p - len(result)):
    result = "0" + result
    result = result[0: -p] + "." + result[-p :]
print("The binary representation of the decimal " + str(x) + " is " + str(result))