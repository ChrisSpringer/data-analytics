# Christopher Springer
# 11/11/2026
# Exercise 3B Lab 2

candy = ('Starburst', 'Skittles', 'Jolly Rancher')
flavors = ('Kiwi Strawberry', 'Lemon-Lime', 'Mango')

# Nested for loop to populate the tuple with all combinations
candy_combo = set()
for i in range(0, len(candy)):
    for x in range(0, len(flavors)):
        candy_combo.add(flavors[x] + ' ' + candy[i])

# displays the tuple with each combintion
print(f"Today's candy options include: {candy_combo}")

# printing this multiple times, I noticed the set changes order every times
# items are rarely in the same position upon repeated running of the code