def getStateCapital():

	# dict containing the names of U.S. states & their capital cities
	stateCapitals = {"Alabama": "Montgomery", "Alaska": "Juneau", "Arizona": "Phoenix", "Arkansas": "Little Rock", "California": "Sacramento", "Colorado": "Denver", "Connecticut": "Hartford", "Delaware": "Dover", "Florida": "Tallahassee", "Georgia": "Atlanta", "Hawaii": "Honolulu", "Idaho": "Boise", "Illinois": "Springfield", "Indiana": "Indianapolis", "Iowa": "Des Moines", "Kansas": "Topeka", "Kentucky": "Frankfort", "Louisiana": "Baton Rouge", "Maine": "Augusta", "Maryland": "Annapolis", "Massachusetts": "Boston", "Michigan": "Lansing", "Minnesota": "Saint Paul", "Mississippi": "Jackson", "Missouri": "Jefferson City", "Montana": "Helena", "Nebraska": "Lincoln", "Nevada": "Carson City", "New Hampshire": "Concord", "New Jersey": "Trenton", "New Mexico": "Santa Fe", "New York": "Albany", "North Carolina": "Raleigh", "North Dakota": "Bismarck", "Ohio": "Columbus", "Oklahoma": "Oklahoma City", "Oregon": "Salem", "Pennsylvania": "Harrisburg", "Rhode Island": "Providence", "South Carolina": "Columbia", "South Dakota": "Pierre", "Tennessee": "Nashville", "Texas": "Austin", "Utah": "Salt Lake City", "Vermont": "Montpelier", "Virginia": "Richmond", "Washington": "Olympia", "West Virginia": "Charleston", "Wisconsin": "Madison", "Wyoming": "Cheyenne"}

	# print instructions for user
	print("\nEnter the full name (not abrv.) of a U.S. state to get the name of its capital city, or enter \"quit\" to exit.\n")

	# prompts user to input name of a state
	state = input("State name: ").title()
	# ↑ used .title() so that all case variants can be valid inputs (e.g. to get the capital of Ohio the user could enter "Ohio", "ohio", "OHIO", etc.)

	# prints the corresponding capital, then prompts again; repeat until sentinel "quit" is entered
	while state!="Quit":
		# if input isn't a valid state name, print error msg
		if stateCapitals.get(state) == None:
			print(f"ERROR: \"{state}\" is not a U.S. state.")
		# prints the corresponding capital IF user enters a valid state name
		else:
			capital = stateCapitals[state]
			print(f"The capital city of {state} is {capital}.")
		# prompts user to input next state name
		state = input("\nState name: ").title()
		# ↑ used .title() so that all case variants can be valid inputs (e.g. "ohio", "OHIO", "oHIO", etc. are all interpretted as "Ohio")
	
	# exit func. when sentinel "quit" is entered
	print()
	return

getStateCapital()