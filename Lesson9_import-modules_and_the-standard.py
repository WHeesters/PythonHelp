import sys

print(sys.version)
print("================================================")
print("CUSTOM MODULES")
print("================================================")
from modules import l9_module as l9  # Use the as keyword to give a name to a imported module
# import modules.my_module as l9                # Another possibility
# from modules.my_module import *               # To import all from a module
from modules.l9_module import find_index, test  # To import a single function/variable etc.

weapons = ["Uzi", "M9", "Baseball bat", "Sniper", "Sawn-off shotgun", "Silenced pistol"]

index = l9.find_index(weapons, "M9")
print("The index of mm.find_index(weapons, 'M9') is " + str(index))  # This uses the entire module import

index_func = find_index(weapons, "Sawn-off shotgun")
print("The index of find_index(weapons, 'Sawn-off shotgun') is " + str(index_func))  # This uses only the imported function

print("")
print("")
print("================================================")
print("STANDARD LIBRARY")
print("================================================")
print("import sys")
import sys

print("The paths python checks to find imports: ")
print(sys.path)

print("")
print("import random")
import random

random_weapon = random.choice(weapons)

print("The random weapons is: " + random_weapon)

print("")
print("import math")
import math

rads = math.radians(90)
sin = math.sin(rads)

print("90 degrees converted to radians is: " + str(rads))
print("The sign of 90 degrees is: " + str(sin))

print("")
print("import datetime and calendar")
import datetime
import calendar

today = datetime.date.today()

print("Today is " + str(today))
print("2020 is a leapyear: " + str(calendar.isleap(2020)))

print("")
print("import os")
import os

print("Current working directory is : " + os.getcwd())
