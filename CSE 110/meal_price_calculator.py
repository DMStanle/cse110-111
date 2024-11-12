#For my addition to the reqyuired code, I added a gratuity option for the user to adda tip to their bill. This can be found in lines 13, 15, and 21.
child_meal = float(input("What is the price of a child's meal?: "))
adult_meal = float(input("What is the price of an adult's meal?: "))
num_of_children = int(input("How many children are there?:"))
num_of_adult = int(input("How many adults are there?: "))
print()
sub_total = num_of_children * child_meal + num_of_adult * adult_meal
print((f"Subtotal is: ${sub_total}"))
print()
tax_rate = float(input("What is the sales tax rate?: "))
tax_rate = sub_total * tax_rate /100
print((f"Tax rate is: ${tax_rate}"))
tip = float(input("How much would you like to tip: "))

total = sub_total + tax_rate + tip
print((f"Total is: ${total}"))
payment_amount_in_cash = float(input("Payment in cash: "))



change = payment_amount_in_cash - sub_total - tax_rate - tip




print((f"Change is: ${change}"))
