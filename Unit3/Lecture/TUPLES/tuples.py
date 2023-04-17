te = ()
t = (2, "one", 3)
print(t[0])
# 2
print(t + (5, 6))
# (2, "one", 3, 5, 6)
print(t[1:2])
# ('one',)
print(t[1:3])
# ('one', 3)

# MANIPULATING TUPLES

aTuple = ((), (), (), ())

def get_data(aTuple):
    nums = ()
    words = ()
    for t in aTuple:
        nums = nums + (t[0],)
        if t[1] not in words:
            words = words + (t[1],)
    
    min_nums = min(nums)
    max_nums = max(nums)
    unique_words = len(words)
    return (min_nums, max_nums, unique_words)

(small, large, words) = get_data(((1, "mine"),
                                  (3, "yours"),
                                  (5, "ours"),
                                  (7, "mine")))

print(small)
# 1
print(large)
# 7
print(words)
# 3


