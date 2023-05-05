# Consider the following sequence of expressions:
animals = { "a": ["aardvark"], "b": ["baboon"], "c": ["coati"]}

animals["d"] = ["donkey"]
animals["d"].append("dog")
animals["d"].append("dingo")

print(animals)


# First, write a procedure, called how_many, 
# which returns the sum of the number of values associated with a dictionary. 
# For example:
# print(how_many(animals))
# 6

def how_many(a_dict):
    '''
    a_dict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    result = 0
    for value in a_dict.values():
        result += len(value)
    return result

print(how_many(animals))
