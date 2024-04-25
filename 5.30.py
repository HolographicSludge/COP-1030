# imports module for RegEx search
# i'm already familiar with regex syntax from being an avid notepad++ enjoyer, so this is just the easiest way i could think of to check for the 2nd & 3rd password rules. sorry if it makes some of the functions less readable.
import re

def main() :
	valid = False
	while valid == False :
	
		# gets new password from user input
		password = inputPW()

		# print failure message if password doesn't follow all of these rules:
			# at least 8 chars long
			# includes uppercase & lowercase
			# includes a number
			# symbols/special chars are OPTIONAL
		if len(password) < 8 :
			print("Your password must be at least 8 characters long. Please try again.")
		elif not(findUpper(password) and findLower(password)) :
			print("Your password must contain both uppercase and lowercase letters. Please try again.")
		elif findNum(password) == False :
			print("Your password must contain a number. Please try again.")
		else :
			valid = True
	
	# prints success message when password is successfully validated (when program exits the above while loop)
	print(f"Success! :)\nYour new password is \"{password}\"\n")

	return

# gets & confirms a password from user input
# returns string
def inputPW() :
	# asks user to input & confirm password
	input1 = str(input("\nEnter a new password: "))
	input2 = str(input("Confirm new password: "))
	# asks user to try again if the 2 inputs don't match
	if input1 != input2 :
		print("ERROR: These passwords do not match. Please try again.")
		input1 = inputPW()
	# returns the confirmed password
	return input1

# checks if param string contains an uppercase letter
# returns boolean
def findUpper(string) :
	upper = re.search("[A-Z]", string)
	if upper == None :
		return False
	else :
		return True

# checks if param string contains a lowercase letter
# returns boolean
def findLower(string) :
	lower = re.search("[a-z]", string)
	if lower == None :
		return False
	else :
		return True

# checks if param string contains a number
# returns boolean
def findNum(string) :
	num = re.search("\d", string)
	if num == None :
		return False
	else :
		return True

main()
