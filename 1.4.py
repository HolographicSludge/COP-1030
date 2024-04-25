# constants
BAL_INIT = 1000   # initial balance
IR = 1.05   # interest rate

# calculates the balance after the given number of years
balYr1 = BAL_INIT * IR
balYr2 = balYr1 * IR
balYr3 = balYr2 * IR

# prints each balance
print(f"Initial balance:\t${BAL_INIT:,.2f}")
print(f"Balance after 1 year:\t${balYr1:,.2f}")
print(f"Balance after 2 years:\t${balYr2:,.2f}")
print(f"Balance after 3 years:\t${balYr3:,.2f}")