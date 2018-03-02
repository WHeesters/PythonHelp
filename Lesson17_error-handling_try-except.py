import sys

print(sys.version)
print("================================================")
print("ERROR HANDLING WITH TRY/EXCEPT")
print("================================================")

try:
    f = open("files/text.txt")  # Wrong
except Exception:
    print("File doesn't exist")

# Throws exception based on anything in try block
try:
    f = open("files/test.txt")
    var = bad_var
except Exception:
    print("File doesn't exist")

# Throws exception based on type of error
try:
    f = open("files/test.txt")
    var = bad_var
except FileNotFoundError:
    print("File doesn't exist")
except NameError:
    print("Name error")
except Exception as e:  # Prints error itself, not self-defined string
    print(e)

# If exception isn't thrown, run the else block
try:
    f = open("files/test.txt")
except FileNotFoundError:
    print("File doesn't exist")
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()

# The finally block always runs
try:
    f = open("files/test.txt")
except FileNotFoundError:
    print("File doesn't exist")
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print("Executing Finally...")

try:
    f = open("files/text.txt")  # Wrong
except FileNotFoundError:
    print("File doesn't exist")
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print("Executing Finally...")

