# Simple function definition, if last argument is TRUE, 
# then print lastName, firstName; 
# else firstName, lastName

def print_name(first_name, last_name, reverse):
    if reverse:
        print(last_name + ", " + first_name)
    else:
        print(first_name, last_name)

# each of this invocations is equivalent
print_name("Nusa", "Stegnar", False)
print_name("Nusa", "Stegnar", reverse = False)
print_name("Nusa", last_name = "Stegnar", reverse = False)
print_name(last_name = "Stegnar", first_name = "Nusa", reverse = False)

def print_name(first_name, last_name, reverse = False):
    if reverse:
        print(last_name + ", " + first_name)
    else:
        print(first_name, last_name)

print_name("Nusa", "Stegnar")
print_name("Nusa", "Stegnar", True)
