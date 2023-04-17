# how to check if a string of characters is a palindrome, i.e., 
# reads the same forwards and backwards
# “Able was I, ere I saw Elba” – attributed to Napoleon
# “Are we not drawn onward, we few, drawn onward to new era?” – attributed to Anne Michaels

# SOLVING RECURSIVELY?
# First, convert the string to just characters, 
# by stripping out punctuation, 
# and converting upper case to lower case
# Then
# Base case: a string of length 0 or 1 is a palindrome
# Recursive case:
# If first character matches last character, then is a palindrome 
# if middle section is a palindrome

# EXAMPLE
# ‘Able was I, ere I saw Elba’ --> ‘ablewasiereisawleba’
# isPalindrome(‘ablewasiereisawleba’) 
# is same as 
# ‘a’ == ‘a’ and 
# isPalindrome(‘blewasiereisawleb’)
def isPalindrome(s):
    def to_chars(s):
        s = s.lower()
        ans = " "
        for char in s:
            if char in "ablewasiereisawleba":
                ans = ans + char
        return ans
    
    def is_pal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and is_pal(s[1: -1])
    return is_pal(to_chars(s))
