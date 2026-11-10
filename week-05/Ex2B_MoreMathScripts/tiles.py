# Christopher Springer
# 11/10/2026

import math

# Assign the length and width from user input
length = int(input("What is the length of the room? "))
width = int(input("What is the width of the room? "))

# Calculate the area
area = length * width

# Calculate the boxes count by dividing area by 12, 
# using ceiling to account for remainding tiles
initial_boxes = math.ceil(area / 12)

# Calculate how many tiles are included in this batch of boxes
initial_tiles = initial_boxes * 12

# remainder
tile_remainder = initial_tiles - area 

# find out how many tiles are in the 10% increase and 
# the amount of boxes needed to account for them
# also subracted the initial remainder since we already had extra
ten_percent_increase = math.ceil(initial_tiles * 0.1)
extra_boxes = math.ceil((ten_percent_increase - tile_remainder) / 12)

# Calculate total amount of boxes necessary and how many tiles that is
total_boxes = initial_boxes + extra_boxes
total_tiles = total_boxes * 12

# Display results
print(f"The area of the room is {area} square feet")
print(f"To cover this space, you will need {initial_boxes} boxes, which is {initial_tiles} tiles")
print(f"{tile_remainder} tile(s) left over")
print(f"For the 10% increase (about {ten_percent_increase} more tiles), \
you will need {total_boxes} boxes, which is a total of {total_tiles} tiles")