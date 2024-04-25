# imports an averaging function (faster than calculating manually)
from statistics import fmean

# prompts the user for 2 integers
print("Please input 2 numbers as integers.")
num1 = int(input("1st number: "))
num2 = int(input("2nd number: "))

# calculates & prints the following stats:
# sum, difference, product, avg, distance, max, min
print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
print("Average/Mean:", fmean([num1, num2]))
print("Distance:", abs(num1 - num2))
print("Maximum:", max(num1, num2))
print("Minimum:", min(num1, num2))