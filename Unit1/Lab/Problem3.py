""" Assume s is a string of lower case characters. Write a program that prints the longest substring 
of s in which the letters occur in alphabetical order. 
For example, if s = 'azcbobobegghakl', then your program should print
Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. 
For example, if s = 'abcbcd', then your program should print
Longest substring in alphabetical order is: abc """


s = "azcbobobegghakl"

current = long = last = ""
# init current, longest, and last char empty

for char in s:
    # loop over entire string
    if last > char:
        # is this end of alphabetic substring?
        if len(current) > len(long):
            # if longer than longest
            long = current
            # replace longest with current
            current = ""
            # reset current string
            current += char
            # always add letter to current string
            last = char
            # save last char to check alpha-sequence
if len(current) > len(long):
            # need to check remaining string
            long = current
            # and replace longest if its longer
print("Longest substring in alphabetical order is: ", long)
             




        




            

        
