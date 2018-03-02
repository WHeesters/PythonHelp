import sys

print(sys.version)
print("================================================")
print("LOCAL, ENCLOSING, GLOBAl, BUILT-IN")
print("================================================")
print("---------------------")
print("GLOBAL AND LOCAL")
print("---------------------")

glob_x = "global x"
glob_loc_z = "global z"
gl = "global gl"

print("Outside test(): ")
print("Global gl variable called before test(): " + gl)


def test(arg_z):
    loc_y = "local y"  # Local variables cannot be accessed outside of their function
    glob_loc_z = "local z"
    global gl  # Sets the global variable to be used within a function
    gl = "new global gl"  # Changes the global variable instead of the local variable
    print("")
    print("Within test():")
    print("Local variable in test(): " + loc_y)
    print("Global variable called in test(): " + glob_x)
    print("glob_loc_z variable called in test(): " + glob_loc_z)
    print("Global gl variable called in test(): " + gl)
    print("Argument variable passed to test(): " + arg_z)


test("local_z")  # Passing an argument to be used inside a function

print("")
print("Outside test(): ")
print("Local variables, i.e. loc_y and arg_z, cannot be accessed outside their function")
print("Global variable called outside test(): " + glob_x)
print("glob_loc_z variable called outside test(): " + glob_loc_z)
print("Global gl variable called after test(): " + gl)

print("")
print("")
print("---------------------")
print("BUILT-IN")
print("---------------------")

import builtins

print("All attributes in builtins: ")
print(dir(builtins))  # Returns a list of all built-in attributes

print("")
print("")
print("---------------------")
print("ENCLOSING")
print("---------------------")

x = "global x"

def outer():
    x = "outer x"
    z = "outer z"
    print("x variable in outer(): " + x)
    print("z variable in outer(): " + z)

    def inner():
        x = "inner x"
        nonlocal z  # Affects local variable in enclosing function
        z = "inner z"
        print("x variable in inner(): " + x)
        print("z variable in inner(): " + z)

    inner()
    print("x variable in outer() after running inner(): " + x)
    print("z variable in outer() after running inner(): " + z)


outer()
print("x variable outside any function: " + x)