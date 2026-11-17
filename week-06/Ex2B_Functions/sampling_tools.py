# Christopher Springer
# 11/16/2026
# Exercise 2B Lab 1

import random

# Generate list
products = ['Laptop', 'Monitor', 'Keyboard', 'Mouse', 'Webcam', 
'Headset', 'Docking Station', 'USB Hub', 'Desk Lamp', 'Surge Protector'] 

# Product of the day - return one randomly selected item
print(random.choice(products))

# Three random products chosen for usability survey, avoiding duplicates
print(random.sample(products, k = 3))

# Display list in a randomized order
random.shuffle(products) # printing this returns NONE
print(products)

# Generate a transaction count between 50 and 300
transaction_count = random.randint(50,300)
print(transaction_count)