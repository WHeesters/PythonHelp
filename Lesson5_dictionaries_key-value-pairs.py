import sys

print(sys.version)
print("================================================")
print("DICTIONARIES")
print("================================================")
# Dictionaries allows us to work with key-value pairs and consist of JSON

student = {1: 3, 'name': 'John', 'age': 25, 'address': 'LA', 'courses': ['Math', 'CompSci']}
student['phone'] = '555-WE-TIP'  # Add a key-value pair to a dict
student['name'] = 'Will'  # Updates a value at a specific key

student.update({'name': 'CJ', 'age': 28, 'license': 'B'})  # Updates and/or adds key-value pairs

del student['license']  # Deletes a key-value pair
popped = student.pop('address')  # Deletes a key-value pair and stores it in a variable

print("Dictionary: " + str(student))  # Prints the entire dict
print("Value at key 'name': " + str(student['name']))  # Prints the value at a specified key
print("Value at key 'courses': " + str(student['courses']))  # This can also be a key for a list
print("Value at key '1': " + str(student[1]))  # A key can also be an int

print("")
phone = student.get('phone')  # Gets the value at a specified key
address = student.get('address')  # Gets the velaue at a non-existant key
DoB = student.get('DoB', 'Not Found')  # Gets the velaue at a non-existant key and returns the second paramater

print("Value at specified key: " + str(phone))
print("Value at non-existant key (address): " + str(address))
print("Value at non-existant key (DoB): " + str(DoB))

print("")
print("Popped key-value pair: " + str(popped))

print("")
print("Length of student dict: " + str(len(student)))  # Prints the length of a dict
print("All keys in student: " + str(student.keys()))  # Prints the keys in a dict
print("All values in student: " + str(student.values()))  # Prints the values in a dict
print("All key-value pairs in student: " + str(student.items()))  # Prints the key-value pairs in a dict

print("")
# Prints each key in a dict individually
print("Looping through student keys:")
for key in student:
    print(key)

print("")
# Prints each key-value pair in a dict individually
print("Looping through student key-value pairs:")
for key, value in student.items():
    print(key, value)
