# Christopher Springer
# 11/12/2026
# Conditional statements Lab 4: min/max of three number

a = eval(input('Enter first number: '))
b = eval(input('Enter second number: '))
c = eval(input('Enter third number: '))

# Check if a is the min or max
if a > b and a > c:
    max = a
if a < b and a < c:
    min = a

# Check if b is the min or max
if b > a and b > c:
    max = b
if b < a and b < c:
    min = b

# Check if c is the min or max
if c > b and c > a:
    max = c
if c < b and c < a:
    min = c

# Display results
print(f'The min is {min} and the max is {max}.')