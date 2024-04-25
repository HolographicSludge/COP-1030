def CountLetter(letter, string) :

	# counts amount of specified letter
	lower = string.count(letter.lower())   #count lowercase
	upper = string.count(letter.upper())   #count uppercase
	
	# returns total amount of specified letter
	return lower+upper

def CountVowels(string) :

	# counts amount of each vowel in string
	a = CountLetter("a", string)   #count A/a
	e = CountLetter("e", string)   #count E/e
	i = CountLetter("i", string)   #count I/i
	o = CountLetter("o", string)   #count O/o
	u = CountLetter("u", string)   #count U/u

	# returns total amount of vowels
	return a+e+i+o+u

def main() :

	# gets string from user input
	string = str(input("Please enter a string: "))

	# prints the amount of vowels the string contains
	vowels = CountVowels(string)
	print(f"The string you entered contains {vowels} vowels.")

	return

main()