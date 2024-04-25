# constants:
TAX_RATE = 0.075   # =7.5%
SHIPPING_PER_BOOK = 2

# variables:
subtotal = 0   # total price of books before tax/shipping
bookAmount = 0
taxTotal = 0
shippingTotal = 0
orderPrice = 0


# user inputs the order's subtotal & number of books
print("Please enter the following details about your order —")
subtotal = float(input("Total price of the books: "))
bookAmount = int(input("Number of books ordered: "))

# calculates total tax & total shipping charge
taxTotal = round(subtotal * TAX_RATE, 2)   # using round() here to get rid of fractional cents bc it might be able to cause logic errors later
shippingTotal = SHIPPING_PER_BOOK * bookAmount

# calculates & prints final price of the order
orderPrice = subtotal + taxTotal + shippingTotal
print(f"The total order price is ${orderPrice:,.2f}.")