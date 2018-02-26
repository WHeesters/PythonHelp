import sys

print(sys.version)
print("================================================")
print("FOR LOOPS")
print("================================================")

nums = [1,2,3,4,5]

print("Every number in 'nums':")
for num in nums:
    print(num) # Prints each value of a list


print("")
print("If num 3 is found the loop ends:")
for num in nums:
    if num == 3:
        print('Found num 3')
        break # break breaks out of the loop when ran
    print(num) # If condition isn't met, this code will run


print("")
print("Num 3 will be skipped:")
for num in nums:
    if num == 3:
        print('Found num 3')
        continue # continues the loop after running
    print(num)

print("")
print("Loop within a loop:")
for num in nums:
    for letter in 'abc':
        print(num, letter)


print("")
print("Loop 10 times starting at 1:")
for i in range(1, 11): # Sets where to start the loop and the amount of times to loop
    print(i)


print("")
print("")
print("================================================")
print("WHILE LOOPS")
print("================================================")
x = 0

print("While x < 10 print x:")
while x < 10:
    print(x)
    x += 1 # Increment to make sure the loop ends


x = 0
print("")
print("While x < 10 print x but break at x = 5:")
while x < 10:
    if x == 5:
        break
    print(x)
    x += 1 # Increment to make sure the loop ends