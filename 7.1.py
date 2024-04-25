def main():
	writeStringToTxt("hello.txt", "Hello, World!")
	message = readStringFromTxt("hello.txt")
	print(message)
	return


# writes a specified message to a specified text file
def writeStringToTxt(file, string):
	
	# open the file
	outputFile = open(file, "w")

	# write string to the file
	outputFile.write(string + "\n")

	# close file & return
	outputFile.close()
	return


# reads a specified text file and returns the read data as a string
def readStringFromTxt(file):
	
	# open the file
	inputFile = open(file, "r")

	# read the file, store read data in string
	string = inputFile.readline()

	# close file & return
	inputFile.close()
	return string


main()