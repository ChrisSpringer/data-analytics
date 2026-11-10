# Christopher Springer
# 11/10/2026

import math

# Find the number of people on the tour
tourists = int(input("How many people are going on this tour? "))

# Calculate the number of vans needed and how much they would cost altogether
vans_needed = math.ceil(tourists / 15)
vans_cost = round(vans_needed * 250, 2)

# Calculate the amount each person needs to pay
cost_per_person = round(vans_cost / tourists, 2)

# FInd out how much money was actually collected
total_collected = round(cost_per_person * tourists, 2)

# Display results according to questions
print(f"For a total of {tourists} people, we will need {vans_needed} vans")
print(f"This will be a total of ${vans_cost}")
print(f"Split evenly, each person will be charged ${cost_per_person}")
print(f"We collected ${total_collected}")

# My script said to charge each person $19.74
# Multiplied out, I collected $750.12
# Thw vans were $750
# There is leftover money due to the rounding up for the tourists cost per person.