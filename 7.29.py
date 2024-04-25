
def enterSales(fileName = "sales.txt"):
## Warning: Stupidly absurd amounts of over-engineering ahead! why tf am i like this
# note-to-self: delet this definitely funny (/s) comment b4 submit
	try:
		# open file
		file = open(fileName, 'a')

		# print instructions for user
		print("Please enter the required data for each sale, one sale at a time.")
		print("When you are finished, enter a blank line to exit.\n")

		# get sales data from user input & write it to file
		name = input("Client name: ")
		while name != "":
			service = input("Service provided: ")
			# make sure value inputted for revenue is a number
			# sorry for the slight spaghetti here, recursion was the only way I could find to implement a "retry" feature while including the try-except and I was too stubborn to just not include in lol
			def retry():
				temp = input("Revenue earned: ")
				try:
					temp = float(temp)
				except ValueError:
					print("ERROR: Revenue earned must be a numerical value. Please retry.")
					temp = retry()
					return temp
				else:
					return temp
			revenue = retry()
			# write inputs to file
			file.write(f"{name}; {service}; {revenue}\n")
			# start getting next set of data
			name = input("\nClient name: ")
	
	# if IOError is raised, warn user of potential invalid/corrupted data
	except IOError as EXCEPTION:
		ERROR_MSG = EXCEPTION.__str__()
		print("\nERROR: A file-related exception has occurred.")
		print(f"Details: {ERROR_MSG}\n")
		print(f"Please open the output file ({fileName}) in another program to ensure the data & syntax are valid before retrying.")

	# if no exceptions raised, print success msg
	else:
		print("\nData saved successfully!")

	# close file & return
	finally:
		try:
			file.close()
		# this part just makes sure python doesn't freak out if the file failed to open lol
		except UnboundLocalError:
			pass
	return


def displayRevenuePerService(fileName = "sales.txt"):

	# get data from the file
	data = getSalesData(fileName)

	# create an new dict to keep track of the revenue totals
	revenuePerService = dict()

	# for each sale: if the service category hasn't been added to the dict yet, add it; then add the revenue of the sale to the dict entry
	for sale in data:
		revenuePerService.setdefault(sale["service"], 0)
		revenuePerService[sale["service"]] += sale["revenue"]
	
	# replace each revenue value in the dict with a string containing the value in money formatting
	for service in revenuePerService:
		revenuePerService[service] = moneyFormat(revenuePerService[service])

	# print the data
	printTable("Service", list(revenuePerService.keys()), "Revenue", list(revenuePerService.values()))


## copies all of the sales data from the file to a list of dicts, where each dict contains the client name, service category, & revenue earned of one sale
def getSalesData(fileName = "sales.txt"):
	try:
		# open file
		file = open(fileName, 'r')

		# copy everything in file to a list
		lines = []
		nextLine = file.readline()
		while nextLine!="" and nextLine!='\n' :
			lines.append(nextLine.strip())
			nextLine = file.readline()
	
	# if IOError is raised, warn user
	except IOError as EXCEPTION:
		ERROR_MSG = EXCEPTION.__str__()
		print("\nERROR: A file-related exception has occurred.")
		print(f"Details: {ERROR_MSG}")

	# close file
	finally:
		try:
			file.close()
		# this part just makes sure python doesn't freak out if the file failed to open lol
		except UnboundLocalError:
			pass
	
	# extract the individual pieces of data from each line
	# stored in a list of dicts (each dict is the data from 1 line)
	salesData = []
	for line in lines:
		data = line.split("; ")
		salesData.append({"name": data[0], "service": data[1], "revenue": float(data[2])})
	
	# return list of sales' data
	return salesData



# these last 2 functions were copy/pasted from a collection i have of funcs that i made for previous assignments that could also be useful for others, so if any part of them seems useless/redundant that's probably why
# (copy/pasted instead of import b/c i figured you wouldn't want to have to deal with grading 2 different files lol)


## Prints data as a table/t-chart with 2 columns & a header row.
# @param h1 : String containing header for the left column.
# @param col1 : List containing data to be printed in the left column.
# @param h2 : String containing header for the right column.
# @param col2 : List containing data to be printed in the right column.
#
def printTable(h1, col1, h2, col2):

	# prints header row
	header = str(h1) + "\t\t" + str(h2)
	print(header)

	# if the columns are of different lengths, appends empty strings to the shorter one until they're the same length
	rowCount = max(len(col1), len(col2))
	while len(col1) < rowCount:
		col1.append("")
	while len(col2) < rowCount:
		col2.append("")
	
	# prints data rows
	for i in range(rowCount):
		nextRow = str(col1[i]) + "\t\t" + str(col2[i])
		print(nextRow)
	
	return


## Formats a raw numerical value as an amount of money; Intended for use in print statements.
# @param n : Float or int value to apply formatting to.
# @param currency : (optional) String specifying which currency symbol to use; defaults to '$'.
# @return : String containing formatted value.
#
def moneyFormat(n, currency='$'):
	
	# raises exception if data type of arg n is not numeric
	# note to future self: data type of currency arg doesn't matter; it's intended to be a string, and all data types I currently know of convert to a string just fine (except lists, but if I ever try to use an entire list as currency then honestly at that point i deserve to spend 5 hours debugging lol)
	if (type(n) != int) and (type(n) != float):
		raise TypeError("Argument n in moneyFormat must be numeric (float or int).")

	# applies formatting
	amount = float(n)   # only relevant if n arg is an int
	money = str(currency) + f"{amount:,.2f}"
	
	# returns formatted value
	return money



def testprgm():
	import time
	print(); enterSales()
	time.sleep(2)
	print("\n"); displayRevenuePerService(); print()
testprgm()