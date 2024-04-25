import random

def GetFromRandIntList():
	
	# creates a list with 100 randomly chosen integers between 1 and 100
	randInts = []
	for i in range(100):
		randInts.append(random.randint(1, 100))

	# prompts the user to enter an index of the array and gets the corresponding element value
	index = int(input("Please enter an index value (0–99): "))
	try:
		elementValue = randInts[index]

	# if the specified index is out of bounds, displays the message "Out of Bounds."
	except IndexError:
		print("Out of Bounds.")
	
	# i debated adding another except branch for other error types for some extra brownie points, but i think in the real world the default error handler would be better for "miscellaneous" errors b/c it gives debug info that's actually useful lol
	### except:
	###     print("ERROR")
	
	# if the specified index is in-bounds, displays the corresponding element value
	else:
		print("Element value:", elementValue)
	
	return

def main():
	GetFromRandIntList()
	return

main()