animals = {"a": "aardvark", "b": "baboon", "c": "coati"}
animals["d"] = "donkey"

# print(animals)
# {'a': 'aardvark', 'b': 'baboon', 'c': 'coati', 'd': 'donkey'}

# print(animals["c"])
# coati

# print(animals["donkey"])
# error

# print(len(animals))
# 4

animals["a"] = "anteater"
#print(animals["a"])
# anteater

# print(len(animals["a"]))
# 8

# print("baboon" in animals)
# False

# print("donkey" in animals.values())
# True

# print("b" in animals)
# True

# print(animals.keys())
# dict_keys(['a', 'b', 'c', 'd'])

del animals["b"]
# print(len(animals))
# 3

print(animals.values())
# dict_values(['anteater', 'coati', 'donkey'])