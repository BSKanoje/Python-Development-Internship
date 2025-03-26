# A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# Ask user for quantity
# Suppose, one unit will cost 100.
# Judge and print total cost for user.

quantity = int(input("Enter the quantity: "))
cost = 100
total_cost = quantity * cost
if total_cost > 1000:
    total_cost = total_cost - (total_cost * 0.1)
print("Total cost is: ", total_cost)
