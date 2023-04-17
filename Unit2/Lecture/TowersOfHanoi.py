# TOWERS OF HANOI
# The story:
# 3 tall spikes
# Stack of 64 different sized discs – start on one spike
# Need to move stack to second spike (at which point universe ends)
# Can only move one disc at a time, and a larger disc can never cover up a small disc

# Think recursively!
# Solve a smaller problem
# Solve a basic problem
# Solve a smaller problem
def print_move(fr, to):
    print("Move from" + str(fr) + "to" + str(to))

def Towers(n, fr, to, spare):
    if n == 1:
        print_move(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)
print(Towers(4, "P1", "P2", "P3"))
# Move fromP1toP3
# Move fromP1toP2
# Move fromP3toP2
# Move fromP1toP3
# Move fromP2toP1
# Move fromP2toP3
# Move fromP1toP3
# Move fromP1toP2
# Move fromP3toP2
# Move fromP3toP1
# Move fromP2toP1
# Move fromP3toP2
# Move fromP1toP3
# Move fromP1toP2
# Move fromP3toP2
# None