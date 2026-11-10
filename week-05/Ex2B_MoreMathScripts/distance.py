# Christopher Springer
# 11/10/2026

import math

# getting the coordinates for both points
x1 = int(input("What is the x coordinate of the first point? "))
y1 = int(input("What is the y coordinate of the first point? "))
x2 = int(input("What is the x coordinate of the second point? "))
y2 = int(input("What is the y coordinate of the second point? "))

# Calculate the distance using math.sqrt() and math.pow()
distance = math.sqrt(math.pow((x2 - x1),2) + math.pow((y2 - y1),2))

# Display results accounting for any trailing decimals
print(f"The distance between ({x1}, {y1}) and ({x2}, {y2}) is {round(distance, 2)}")