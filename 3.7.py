# gets 3 ints from user
print("Please enter 3 integers (press enter key between each number)")
x = int(input())
y = int(input())
z = int(input())

# tells user if ints are in ascending or descending order
if x == y and y == z :
	print("Those are all the same number...")
elif x <= y and y <= z :
	print("These numbers are in ascending order.")
elif x >= y and y >= z :
	print("These numbers are in descending order.")
else :
	print("These numbers are not in order.")