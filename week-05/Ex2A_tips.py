# Christopher Springer
# 11/10/2026

# Define known values
food_cost = 79.25
tax = 6.54
tip = 12.00

# Calculate the unknown
total_due = food_cost + tax + tip

# Display the results
# print("The total due is " + str(total_due)) 
# str() function casts the given value as a string. Here it is used for concatenation
# The total due is 97.79

print("Food cost is " + str(food_cost) + " and tax is " + str(tax)) # Food cost is 79.25 and tax is 6.54
# print("Tip is " + str(tip))                                       # Tip is 12.0
print("Tip is " + format(tip, ".2f"))                               # Tip is 12.00
print("Total due is " + str(total_due))                             # Total due is 97.79