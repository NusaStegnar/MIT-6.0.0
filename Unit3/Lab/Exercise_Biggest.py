# Consider the following sequence of expressions:
animals = { "a": ["aardvark"], "b": ["baboon"], "c": ["coati"]}

animals["d"] = ["donkey"]
animals["d"].append("dog")
animals["d"].append("dingo")

# write a procedure, called biggest, 
# which returns the key corresponding to the entry with the largest number of values associated with it. 
# If there is more than one such entry, return any one of the matching keys.

# Example usage:
# biggest(animals)
# "d"

def biggest(a_dict):
    '''
    a_dict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    result = None
    biggest_value = 0
    for key in a_dict.keys():
        if len(a_dict[key]) >= biggest_value:
            result = key
            biggest_value = len(a_dict[key])
    return result

print(biggest(animals))
