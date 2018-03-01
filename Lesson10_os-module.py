import sys

print(sys.version)
print("================================================")
print("THE OS MODULE")
print("================================================")
import os

print("All attributes and methods from the os module: ")
print(dir(os))  # Gets all attributes and methods from a module

print("")
print("The current working dir is: " + os.getcwd())  # Gets current working dir

os.chdir("../PythonHelp/files/")  # Changes current working dir

print("The current working dir is now: " + os.getcwd())
print("The files and folders in the current dir are: ")
print(os.listdir())  # Lists all files and folders in the current working dir

os.mkdir("Test")  # Makes a dir in the current working dir
os.makedirs("Test1/SubDir")  # Makes a dir with sub-dirs

print("")
print("The files and folders in the current dir after adding one dir and one dir with sub-dir are: ")
print(os.listdir())

os.rmdir("Test")  # Removes a dir in the current working dir
os.removedirs("Test1/SubDir")  # Removes a dir with its sub-dir

print("")
print("The files and folders in the current dir after removing one dir and one dir with sub-dir are: ")
print(os.listdir())

print("")
os.rename("test.txt", "demo.txt")  # Renames a file or folder in the current working dir
print("The test.txt file has been renamed to demo.txt: ")
print(os.listdir())
os.rename("demo.txt", "test.txt")
print("The demo.txt file has been changed back to test.txt: ")
print(os.listdir())

print("")
print("The os.stat for test.txt is: ")
print(os.stat("test.txt"))  # Gets the stats for a file or folder
print("")
print("The size of test.txt is: ")
print(os.stat("test.txt").st_size)  # Gets the size for a file or folder
print("The last modified time of test.txt is: ")
print(os.stat("test.txt").st_mtime)  # Gets the last modified time for a file or folder

from datetime import datetime

timestamp = os.stat("test.txt").st_mtime

print("The last modified time of test.txt in readable form is: ")
print(datetime.fromtimestamp(timestamp).strftime(
    "%Y-%m-%d %H:%M:%S"))  # Converts a given timestamp to human readable form .strftime is for formatting

print("")
print("")
print("The entire dir tree: ")
for dirpath, dirnames, filenames in os.walk(os.getcwd()):  # Gets the entire dir tree from the current working dir
    print("Current Path:", dirpath)
    print("Dirs:", dirnames)
    print("Files:", filenames)
    print("")

print("")
print("The environment variable 'USERPROFILE' contains: ")
print(os.environ.get("USERPROFILE"))  # Gets a given environment variable

file_path = os.path.join(os.environ.get("USERPROFILE"), "test.txt")  # Joins two paths together
print("Joined path: ")
print(file_path)

print("")
print("The basename of '/tmp/test.txt' is: ")
print(os.path.basename("/tmp/test.txt"))  # Gets the basename of a path
print("The dirname of '/tmp/test.txt' is: ")
print(os.path.dirname("/tmp/test.txt"))  # Gets the dirname of a path
print("The split names of '/tmp/test.txt' are: ")
print(os.path.split("/tmp/test.txt"))  # Splits a path into its base- and dirname
print("'/tmp/test.txt exists:' " + str(os.path.exists("/tmp/test.txt")))  # Checks if a path exists
print("The split extension of '/tmp/test.txt' is:")
print(os.path.splitext("/tmp/test.txt"))  # Splits the extension from the filename
