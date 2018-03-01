import sys

print(sys.version)
print("================================================")
print("IF ELSE ELIF STATEMENTS")
print("================================================")

# Comparisons:
# Equal:                ==
# Not Equal:            !=
# Greater than:         >
# Less than:            <
# Greater or equal:     >=
# Less or equal:        <=
# Object Identity:      is

language = "Java"

if language == "Python":
    print("The language is Python")
elif language == "Java":
    print("The language is Java")
elif language == "JS":
    print("The language is JS")
else:
    print("No match")

print("")
user = "Admin"
logged_in = False

print("AND:")  # AND
if user == "Admin" and logged_in:
    print("Admin is logged in")
else:
    print("Bad creds")

print("OR:")  # OR
if user == "Admin" or logged_in:
    print("Admin is logged in")
else:
    print("Bad creds")

print("NOT:")  # NOT
if not logged_in:
    print("Please log in")
else:
    print("Welcome")

print("")
print("")
print("================================================")
print("'is' vs. '=='")
print("================================================")

a = [1, 2, 3]
b = [1, 2, 3]

print("a equals b: " + str(a == b))  # Returns True
print("a is b: " + str(a is b))  # Returns False

print("")
print("The id's of a and b are different:")
print("id a: " + str(id(a)))
print("id b: " + str(id(b)))

b = a  # Sets b equal to a

print("")
print("If b = a, the id is the same: ")
print("id a: " + str(id(a)))
print("id b: " + str(id(b)))
print("And now a equals b and a is b are both True:")
print("a equals b: " + str(a == b))  # Returns True
print("a is b: " + str(a is b))  # Returns False
print("")
print("The is operator is the same as saying id(a) == id(b):")
print(id(a) == id(b))

print("")
print("")
print("================================================")
print("False values")
print("================================================")

# False values:
# False
# None
# Zero of any numeric type
# Any empty sequence. i.e. "", (), []
# Any empty mapping. i.e. {}

print("Condition = False")
condition = False

if condition:
    print("Evaluated to True")
else:
    print("Evaluated to False")

print("Condition = None")
condition = None

if condition:
    print("Evaluated to True")
else:
    print("Evaluated to False")

print("Condition = 0")
condition = 0

if condition:
    print("Evaluated to True")
else:
    print("Evaluated to False")

print("Condition = 10")
condition = 10

if condition:
    print("Evaluated to True")
else:
    print("Evaluated to False")

print("Condition = ''")
condition = ""

if condition:
    print("Evaluated to True")
else:
    print("Evaluated to False")

print("Condition = {}")
condition = {}

if condition:
    print("Evaluated to True")
else:
    print("Evaluated to False")

print("Condition = 'Test'")
condition = "Test"

if condition:
    print("Evaluated to True")
else:
    print("Evaluated to False")
