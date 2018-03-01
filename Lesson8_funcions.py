import sys

print(sys.version)
print("================================================")
print("FUNCTIONS")
print("================================================")


def blank_func():
    pass  # To be able to leave a function blank


print("Blank function returns: " + str(blank_func()))


def hello_func():
    print("This is the output of hello_func()")


hello_func()  # Call a function


def return_func():
    return "This is the output of return_func()"


return_func()  # Won't print anything

print(return_func())  # Will print the output
print(return_func().upper() + " in uppercase")  # Because you know the return type, you can call additional functions


def arg_func(arg):  # A function with an argument
    return f"{arg} Function."  # f notation to use parameters inside a string instead of using the .format() function


print(arg_func("Argument"))  # Call a function with a parameter


def args_func(arg, arg2="Argument 2"):  # A function with multiple arguments, name has a default value of 'Argument 2'
    return f"{arg}, {arg2}."


print("The output of args_func('Argument'): " + args_func("Argument"))  # Prints the arg function with a default second parameter because we didn't provide one
print("The output of args_func('Argument', 'CJ'): " + args_func("Argument", "CJ"))


def cj_info(*args,
            **kwargs):  # *args and **kwargs are used to receive an arbitrary number of arguments and key-word arguments
    print("The arguments: " + str(args))
    print("The key-word arguments: " + str(kwargs))


print("")
print("The output of cj_info('Uzi','Baseball bat',name='CJ',age=22): ")
cj_info("Uzi", "Baseball bat", name="CJ", age=22)

weapons = ["Uzi", "Baseball bat", "Silenced pistol"]
info = {"name": "CJ", "age": 22, "occupation": "na"}

print("")
print("The output of cj_info(weapons, info): ")
cj_info(weapons, info)  # Passes all arguments as *args

print("")
print("The output of cj_info(*weapons, **info): ")
cj_info(*weapons, **info)

print("")
print("")
print("================================================")
print("STANDARD PYTHON LIBRARY CODE")
print("================================================")
#################################################
# This is the start of the standard library code#
#################################################
# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """Return True for leap years, False for non-leap years."""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of days in that month in that year."""

    if not 1 <= month <= 12:
        return "Invalid Month"

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]


#################################################
## This is the end of the standard library code##
#################################################


print("The output of is_leap(2018): " + str(is_leap(2018)))
print("The output of is_leap(2020): " + str(is_leap(2020)))
print("The output of days_in_month(2018, 2): " + str(days_in_month(2018, 2)))
print("The output of days_in_month(2020, 2): " + str(days_in_month(2020, 2)))
