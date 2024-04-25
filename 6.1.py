import random

def main():
	# declarations
	values = []
	evenIndexVals = []
	evenVals = []
	valsReversed = []

	# prints a list of ten random ints
	for n in range(10):
		values.append(random.randint(1, 99))
	printList(values, "Values in list")

	# prints a list of each value at an even index
	for i in range(len(values)):
		if isEven(i):
			evenIndexVals.append(values[i])
	printList(evenIndexVals, "Values at even indexes")

	# prints a list of even elements in the original list
	for x in values:
		if isEven(x):
			evenVals.append(x)
	printList(evenVals, "Even values")

	# prints the original list but in reversed order
	valsReversed = values
	valsReversed.reverse()
	printList(valsReversed, "Values in reverse order")

	# prints the 1st & last values of the original list
	print("First value:", values[0])
	print("Last value:", values[len(values)-1])

	return

# takes in a numerical value; returns true if value is even, returns false if value is odd
def isEven(num):
	if num % 2 == 0:
		return True
	else:
		return False

# takes in a list of any type of elements and 2 optional strings
# prints the string followed by ": " (with NO LINEFEED AT THE END), followed by each element in the list with a user-defined separator b/t each element (default separator: ", ")
# this program never specifies a non-default element separator, but I added the option anyway for reusability.
def printList(list, label=None, separator=", "):
	if label!=None:
		print(label, end=": ")
	for i in range(len(list)):
		if i==len(list)-1:
			print(list[i], end="\r\n")
		else:
			print(list[i], end=separator)
	return

main()