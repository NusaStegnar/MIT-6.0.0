c = [(1, 2, 3), "Week 3", 6.453, [[1, 2, 3, 4], 5], 678, [True, False]]

print(c[0])
# (1, 2, 3)
print(c[3:])
# [[[1, 2, 3, 4], 5], 678, [True, False]]
print(c[3][0][2])
# 3
print(c[3][1])
# 5
print(c[::-2])
# [[True, False], [[1, 2, 3, 4], 5], 'Week 3']
print(c[:3])
# [(1, 2, 3), 'Week 3', 6.453]
print(c[:1:-2])
# [[True, False], [[1, 2, 3, 4], 5]]

