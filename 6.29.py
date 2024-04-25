#takes in 2 lists, returns an appended list
def appendList(a, b):
	
	#creates new list of 2 passed in lists
	newList = a + b
	return newList

def main():
	
	#creates 2 lists
	names = ["Susan", "Beverly", "Michael"]
	values = [1, 2, 3, 4, 5]
	
	#calls appendList
	newList = appendList(names, values)
	
	#prints newList
	print(newList)

main()