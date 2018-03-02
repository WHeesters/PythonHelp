import sys

print(sys.version)
print("================================================")
print("SORTING LISTS, TUPLES AND OBJECTS")
print("================================================")
print("---------------------")
print("LISTS")
print("---------------------")

num_li = [9, 2, 3, 6, 5, 4, 1, 7, 8]
s_num_li = sorted(num_li)
s_num_li_sort = num_li.sort()  # Returns none

print("Original list Variable: ", num_li)
print("Sorted list Variable: ", s_num_li)

num_li.sort()  # Only works on lists
print("Original list Variable with sort method: ", num_li)
print("Sorted list Variable with sort method: ", s_num_li_sort)

s_num_li_rev = sorted(num_li, reverse=True)
num_li.sort(reverse=True)
print("Original list Variable with sort method descending: ", num_li)
print("Sorted list Variable descending: ", s_num_li_rev)

n_num_li = [-6, -4, 1, -5, 2, 3]
s_n_num_li = sorted(n_num_li)
s_n_num_li_abs = sorted(n_num_li, key=abs)  # Sorts on absolute values

print("")
print("Original negative list Variable: ", n_num_li)
print("Sorted negative list Variable: ", s_n_num_li)
print("Sorted negative list Variable absolute value: ", s_n_num_li_abs)

print("")
print("")
print("---------------------")
print("TUPLES")
print("---------------------")

num_tup = (9, 2, 3, 6, 5, 4, 1, 7, 8)
s_num_tup = sorted(num_tup)  # Returns a sorted list
print("Original tuple Variable: ", num_tup)
print("Sorted tuple Variable: ", s_num_tup)

print("")
print("")
print("---------------------")
print("DICTIONARIES")
print("---------------------")

di = {"name": "CJ", "age": 28, "license": "B", "phone": "555-WE-TIP"}
s_di = sorted(di)  # Just sorts the keys

print("Original dict Variable: ", di)
print("Sorted dict Variable: ", s_di)

print("")
print("")
print("---------------------")
print("OBJECTS")
print("---------------------")


class Character():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):  # Defines a representation for return value
        return f"({self.name}, {self.age}, ${self.salary})"


c1 = Character('CJ', 28, 240000)
c2 = Character('Rider', 26, 70000)
c3 = Character('Big Smoke', 31, 150000)

characters = [c1, c2, c3]


def c_sort(cha):  # Defines our own sort key
    return cha.name


def c_sort_s(cha):
    return cha.salary


s_characters = sorted(characters, key=c_sort)  # Sorts based on our own key
s_characters_s = sorted(characters, key=c_sort_s, reverse=True)
s_characters_a = sorted(characters, key=lambda c: c.age)  # Sorts based on lambda function

from operator import attrgetter

s_characters_a_a = sorted(characters, key=attrgetter("age"))  # Sorts based on attrgetter class


print("Unsorted characters: ")
print(characters)
print("Sorted characters based on name: ")
print(s_characters)
print("Sorted characters descending based on salary: ")
print(s_characters_s)
print("Sorted characters based on age using lambda: ")
print(s_characters_a)
print("Sorted characters based on age using attrgetter: ")
print(s_characters_a_a)
