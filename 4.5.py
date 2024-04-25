# imports an averaging function
from statistics import fmean

# reads a non-fixed amount of floats from user input
print("\nPlease input a list of numbers below. Seperate each number by pressing the \"enter\" key. Enter a blank line after the last number to mark the end of the list.")
numbers = [] # list of numbers user inputs
nextVal = float(input())
# continues asking user for more numbers until they enter a blank line (signals end of list)
while nextVal != "" :
	numbers.append(float(nextVal))
	nextVal = input()

# calculates & prints the average, min, max, & range of the inputted list of numbers
print("Average of Values:", fmean(numbers))
print("Smallest Value:", min(numbers))
print("Largest Value:", max(numbers))
print("Difference b/t Smallest & Largest:", max(numbers) - min(numbers))
print()