def compareStringsChars():
	
	# prompts user to enter 2 strings, stores them as sets of characters
	print("\nEnter 2 strings of text to compare.")
	str1 = set(input("String #1: "))
	str2 = set(input("String #2: "))

	# determines which letters don’t occur in either string
	notUsedLetters = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"}
	for char in (str1 | str2):
		notUsedLetters.discard(char.lower())

	# prints the comparison results
	print("\nCharacters that are in both strings:", str1 & str2)
	print("Characters that are only in string #1:", str1 - str2)
	print("Characters that are only in string #2:", str2 - str1)
	print("Letters that are not in either string:", notUsedLetters)
	
	print()
	return

compareStringsChars()