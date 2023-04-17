# General approximation algorithm to find roots of a polynomial in one variable

#Want to find r such that p(r) = 0
# For example, to find the square root of 24, find the root of 
# p(x) = x2 – 24
# Newton showed that if g is an approximation to the root, then
# g – p(g)/p’(g)
# is a better approximation; where p’ is derivative of p

# Simple case: cx2 + k
# First derivative: 2cx
# So if polynomial is x2 + k, then derivative is 2x
# Newton-Raphson says given a guess g for root, a better guess is
# g – (g2 –k)/2g

epsilon = 0.01  # how close we are to an answer
y = 54.0
guess = y / 2.0
num_Guesses = 0

while abs(guess * guess - y) >= epsilon:  # abs je absolutna vrednost
    num_Guesses += 1
    guess = guess - (((guess ** 2) - y) / (2 * guess))
print("num_Guesses = " + str(num_Guesses))
print("Square root of " + str(y) + " is about " + str(guess))
