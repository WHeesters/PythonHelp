import sys

print(sys.version)
print("================================================")
print("FILE OBJECTS")
print("================================================")
print("---------------------")
print("NOT RECOMMENDED")
print("---------------------")
# The not recommended method
notRecommendedWay = open("files/test.txt",
                         "r")  # Opens the file at the given path with the given mode r=read w=write r+=read/write

print(notRecommendedWay.name)  # Prints the name of the file
print(notRecommendedWay.mode)  # Prints the mode with which the file is opened

notRecommendedWay.close()  # Closes the file!

print("---------------------")
print("RECOMMENDED")
print("---------------------")
# The recommended method
print("~~~~~~~~")
print("READ")
print("~~~~~~~~")
with open("files/test.txt", "r") as f:  # Opens a file using a context manager
    f_contents = f.read()  # Reads the contents of a file
    print("Below are the contents of test.txt: ")
    print(f_contents, end="")

print("")
with open("files/test.txt", "r") as f:
    f_contentLines = f.readlines()  # Reads the contents of a file and puts the lines in a list
    print("Below are the contents of test.txt in a list: ")
    print(f_contentLines, end="")

print("")
with open("files/test.txt", "r") as f:
    f_contentLine = f.readline()  # Reads a line in a file
    print("")
    print("Below are the contents of line 1 in test.txt: ")
    print(f_contentLine, end="")  # Prints a line and ends it with a empty string (removes the newline)

    f_contentLine = f.readline()  # Reads the next line in a file
    print("Below are the contents of line 2 in test.txt: ")
    print(f_contentLine, end="")

    f.seek(0)  # Resets the read position to the given position

    f_contentLine = f.readline()
    print("Below are the contents of line 1 in test.txt: ")
    print(f_contentLine, end="")

print("")
with open("files/test.txt", "r") as f:
    print("Iterated over every line in the test.txt file gives: ")
    for line in f:  # Iterate over every line in a file
        print(line, end="")

print("")
print("")
with open("files/test.txt", "r") as f:
    f_contents = f.read(100)  # Reads the file up to given char amount
    print("Below are the contents of test.txt up to the 100th char: ")
    print("")
    print(f_contents, end="")

    f_contents = f.read(100)  # Reads the file a given char amount further
    print("")
    print("")
    print("Below are the contents of test.txt up to the 200th char from the 100th char: ")
    print(f_contents, end="")

print("")
print("")
with open("files/test.txt", "r") as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)  # Reads the file up to given char amount
    print("The location in the test.txt file at this point is: " + str(f.tell()))  # Gets the current location of the f.read() method
    print("Below are the contents of test.txt up to the the given char amount: ")
    print("")
    while len(f_contents) > 0:
        print(f_contents, end="*")  # Adds an * after every time it loops
        f_contents = f.read(size_to_read)  # Sets f_contents to the next chunk

print("")
print("")
print("~~~~~~~~")
print("WRITE")
print("~~~~~~~~")
# with open("files/test2.txt", "a") as f:  # Opens a writable file and appends to it instead of overriding
with open("files/test2.txt", "w") as f:  # Creates a writable file if it doesn't exist, otherwise overrides it
    f.write("Test")

print("")
print("")
print("~~~~~~~~")
print("READ/WRITE")
print("~~~~~~~~")
with open("files/test.txt", "r") as rf:
    with open("files/test_copy.txt", "w") as wf:
        for line in rf:
            wf.write(line)  # Writes every line from a read-only file into a write-file

with open("files/img.jpg", "rb") as rf:  # The added b opens a file in binary mode
    with open("files/img_copy.jpg", "wb") as wf:
        for line in rf:
            wf.write(line)

with open("files/img.jpg", "rb") as rf:
    with open("files/img_copy_chunk.jpg", "wb") as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:  # Copies an image/file in chunks
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)

print("")
print("")
print("File is closed: " + str(f.closed))  # Checks if a file is closed
