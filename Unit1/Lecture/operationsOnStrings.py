OPERATIONS ON STRINGS

 "ab"+ "cd"  concatenation
 3 * "eric"  successive concatenation
 len("eric")  the length
 "eric"[1]  indexing
 "eric"[1:3]  slicing

#successive concatenation
3 * "eric"
print(3*"eric")

print(10*"mama")

#the length
len("eric")
print(len("eric"))
len("hi there you boy") = lenght of a string including spaces

#indexing
"eric"[1] = "r" (it stars counting with 0)
"eric"[0]
"my name is Maya"[8]

my_name = "peter"
my_name[3]
my_name[5] = error; string index out of range
my_name[-1]


#slicing

"eric"[1:3] = gives first and second, but not third
"eric"[0:3] is the same as "eric"[:3] = gives from biggining to including second, but not third
"eric"[1:] = gives from first (not zero) to last
"eric"[:] = gives all string

#excersises

"mahatmagandhi"[3:7]
"drugsonbord"[3:6]
"mamamiawhereareyou"[4:9]
"helloworldandby"[3:10:3]

s = "Python is fun!"
s[1:5]
s[:5]
s[1:]
s[:]
s[1:12:2]
s[1:12:3]
s[::2]