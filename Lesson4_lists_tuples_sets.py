import sys

print(sys.version)
print("================================================")
print("LISTS")
print("================================================")
courses = ["History", "Math", "Physics", "CompSci"]
courses_2 = ["Education", "English"]
nums = [1, 2, 4, 5, 7, 3, 0, 9]
different_list = list("123456789")  # Creates a list by splitting after every character
course_str = ", ".join(courses)  # Joins items from a list to a string
new_courses = course_str.split(", ")  # Splits a string into a list based on a given string
sorted_courses = sorted(courses)  # Sorts a list without altering the original list by creating a new list

courses.append("Art")  # Adds an item to the end of a list
courses.insert(2, "PE")  # Adds an item to a given index
courses.extend(courses_2)  # Adds the contents of another list to the end of a list

courses.remove("Math")  # Removes an item from a list
courses.pop()  # Removes the last item from a list

courses.reverse()  # Reverses the order of a list
courses.sort()  # Sorts a list in a alphabetical order
nums.sort()  # Sorts a list of numbers ascending
nums.sort(reverse=True)  # Sorts a list descending

print("Courses: " + str(courses))
print("Numbers: " + str(nums))
print("Different way of making a list: " + str(different_list))
print("Sorted courses: " + str(sorted_courses))
print("Joined courses: " + course_str)
print("Split list: " + str(new_courses))

print("")  # Prints an empty line
print("Index of 'CompSci': " + str(courses.index("CompSci")))  # Prints the index of a value

print("")
print("Minimum in numbers: " + str(min(nums)))  # Prints the minimum number of a list
print("Maximum in numbers: " + str(max(nums)))  # Prints the maximum number of a list
print("Sum of numbers: " + str(sum(nums)))  # Prints the sum of a list

print("")
print("Art" in courses)  # Prints a boolean based on value in a list

print("")
# Prints each item in a list individually
print("Individual items: ")
for course in courses:
    print(course)

print("")
# Prints each item in a list individually with it's index starting at x
print("Individual items with index starting at 1: ")
for index, course in enumerate(courses, start=1):
    print(index, course)

print("")
print("")
print("================================================")
print("TUPLES")
print("================================================")
# Tuples are basically the same as lists, the biggest difference is that tuples are immutable

tuple_1 = ("History", "Math", "Physics", "CompSci")
tuple_2 = tuple_1
different_tuple = tuple("123456789")  # Creates a tuple by splitting after every character
stupid_tuple = "This", "is", "a", "stupid", "way", "to", "create", "a", "tuple"  # creates a tuple somehow

print("Tuple 1: " + str(tuple_1))
print("Tuple 2: " + str(tuple_2))
print("Different way of making a tuple: " + str(different_tuple))
print("Stupid way of making a tuple: " + str(stupid_tuple))

print("")
print("")
print("================================================")
print("SETS")
print("================================================")
# Sets are unordered lists

courses_set_duplicate = {"History", "Math", "Physics", "CompSci", "Math"}
courses_set = {"History", "Math", "Physics", "CompSci"}
courses_set_2 = {"History", "English", "PE", "CompSci"}
different_set = set("123456789")  # Creates a set by splitting after every character
frozen_set = frozenset("123456789")  # Creates an immutable set

intersection = courses_set.intersection(courses_set_2)  # The overlap between sets
difference = courses_set.difference(courses_set_2)  # The difference between sets
union = courses_set.union(courses_set_2)  # The combination of sets

member = "Math" in courses_set  # Sets are optimized to look for members

print("Courses set with duplicate: " + str(courses_set_duplicate))  # The duplicate 'Math' will only be printed once
print("Different way of making a set: " + str(different_set))
print(member)

print("")
print("Overlap between set 1 and 2: " + str(intersection))
print("Difference between set 1 and 2: " + str(difference))
print("Combination of set 1 and 2: " + str(union))
