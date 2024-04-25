#initialize constants & vars
TOTAL_TICKETS_TO_SELL = 20
MAX_TICKETS_PER_BUYER = 4
ticketsRemaining = TOTAL_TICKETS_TO_SELL
ticketsBought = []
ticketsRequested = 0

# repeat until all tickets have been sold:
while ticketsRemaining > 0 :

	# prompt the user for the desired number of tickets
	ticketsRequested = int(input(f"\nEnter the number of tickets to purchase (max. {MAX_TICKETS_PER_BUYER} tickets per buyer): "))

	# input validation
	if ticketsRequested < 1 :
		print("ERROR: Number of tickets requested must be positive.")
	elif ticketsRequested > MAX_TICKETS_PER_BUYER :
		print(f"ERROR: You may only purchase a maximum of {MAX_TICKETS_PER_BUYER} tickets.")
	elif ticketsRequested > ticketsRemaining :
		print(f"Sorry, we currently only have {ticketsRemaining} tickets available. :(")
	
	# if purchase succeeds, adds it to the purchases list & outputs success msg
	else :
		ticketsBought.append(ticketsRequested)
		print("Purchase successful! :)")
		ticketsRemaining -= ticketsRequested
		print("Tickets remaining:", ticketsRemaining)

# after ALL tickets have been sold, displays the total number of buyers
print("\nALL TICKETS SOLD!")
print("Number of buyers:", len(ticketsBought))
print()