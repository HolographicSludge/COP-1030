
def storeGolfRecords():
	
	# open txt file to write records in
	file = open("golf.txt", "a")
	try:
		
		# gets records from user input
		playerNames = []
		playerScores = []
		print("Please input each player's name and golf score. When finished, press enter (input a blank line) to save the data.")
		nextField = input("Player #1 Name: ")
		# continues getting records until sentinal (blank input) is hit
		while nextField != "":
			playerNames.append(nextField)
			nextField = int(input("%s's Score: " %( playerNames[ len(playerNames)-1 ] ) ))
			playerScores.append(nextField)
			nextField = input("Player #%d Name: " %(len(playerNames)+1))

		# writes the list of records to the txt file
		print("Saving...")
		for i in range(len(playerNames)):
			file.write("%s: %d\n" %(playerNames[i], playerScores[i]))
		print("Data saved successfully.")
	
	# close file & return
	finally:
		file.close()
	return


def printGolfRecords():
	
	# open txt file containing records
	file = open("golf.txt", "r")
	try:
		
		# stores each line of the txt file in a list
		records = []
		nextRecord = file.readline()
		while nextRecord != "":
			records.append(nextRecord.rstrip())
			nextRecord = file.readline()

		# prints the list of records
		print("Golf Records")
		print("-"*14)
		for x in records:
			print(x)

	# close file & return
	finally:
		file.close()
	return


# debug: input function in console to run it
# i decided to comment this out instead of deleting it just in case you wanna use it for testing my code
'''
print()
command = input()
while command != "exit":
	print()
	eval(command)
	print()
	command = input()
print()
'''