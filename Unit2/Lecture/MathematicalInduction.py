# Mathematical Induction
# To prove a statement indexed on integers is true for all values of n:
# Prove it is true when n is smallest value (e.g. n = 0 or n = 1)
# Then prove that if it is true for an arbitrary value of n, 
# one can show that it must be true for n+1

# EXAMPLE OF INDUCTION
# 0 + 1 + 2 + 3 + ...+ n = (n(n+1))/2
# PROOF
# If n = 0,
# then left hand side(LHS) is 0 and right hand side(RHS) is 0*1/2=0 --> so this is True

# Assume true for some k, then need to show that
# 0 + 1 + 2 + … + k + (k+1) = ((k+1)(k+2))/2
# LHS is k(k+1)/2 + (k+1) by assumption that property holds for problem of size k
# This becomes, by algebra, ((k+1)(k+2))/2
# Hence expression holds for all n >= 0

# RELEVANCE TO CODE?
def mult(a, b):
    if b == 1:
        return a
    else:
        return a + mult(a, b - 1)
# Base case, we can show that mult must return correct answer
# For recursive case, we can assume that 
# mult correctly returns an answer for problems of size smaller than b, 
# then by the addition step, 
# it must also return a correct answer for problem of size b
# Thus by induction, code correctly returns answer