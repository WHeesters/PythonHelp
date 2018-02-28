import sys

print(sys.version)
print("================================================")
print("MULTIPLE FILE PARSING AND RENAMING")
print("================================================")

import os

os.chdir('../PythonHelp/files/videos')  # Change dir to correct one

print("Current dir: ")
print(os.getcwd())

print("")
print("All files in dir:")
for f in os.listdir():
    print(f)

print("")
print("")
for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)  # Splits the filename on the extension
    f_title, f_course, f_num = f_name.split('-')  # Gets just the filename split on the -

    f_title = f_title.strip()  # Strips any whitespace
    f_course = f_course.strip()
    f_num = f_num.strip()[1:].zfill(2)  # Gets anything from the second character on and adds a 0 on the beginning

    new_names = f'{f_num}_{f_title}{f_ext}'  # Formats the new names
    os.rename(f, new_names)  # Renames all file

