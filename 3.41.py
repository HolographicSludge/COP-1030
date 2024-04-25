TIP_MULTIPLIER = 0.05 # used for systematic calculation of recommended tip (avoids needing about 30 bazillion if statements)
MIN_TIP = 0.05 # minimum recommended tip (percentage); exists mostly just to ensure customer can't tip $0

# asks the customer how much they spent on dinner
total = float(input("\nPlease enter the cost of your meal: "))
# input validation
while total <= 0 :
	print("Error: Cost must be a positive number.")
	total = float(input("Please try again: "))

# asks the customer's satisfaction rating
satisfaction = int(input("Please rate your satisfaction with our service today out of 5 stars: "))
# input validation
while satisfaction < 1 or satisfaction > 5 :
	print("Error: Satisfaction rating must be a whole number between 1 & 5.")
	satisfaction = int(input("Please try again: "))

# calculates the customer's recommended tip
tipPercent = (satisfaction - 1) * TIP_MULTIPLIER # 5 stars = 20%, 4 stars = 15%, etc.
if tipPercent < MIN_TIP : # enforces minimum recommended tip
	tipPercent = MIN_TIP
tipAmount = total * tipPercent # calculates dollar amount from percentage

# reports the customer's satisfaction rating, recommended tip amount, & recommended tip percentage
print(f"\nFor {satisfaction}-star service, your recommended tip is ${tipAmount:,.2f} ({int(tipPercent * 100)}%)\n")