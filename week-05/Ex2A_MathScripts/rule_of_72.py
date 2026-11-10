# Christopher Springer
# 11/10/2026

interest_rate = float(input("What is your interest rate "))
savings = int(input('What is your current account savings? '))
doubled_savings = savings * 2       #finding the doubled savings
years = 72 / (interest_rate * 100)  # rule of 72

print('Your current savings is ' + str(savings))
print(f'At a {interest_rate:.0%} interest rate, \
your savings account will be worth {doubled_savings:.2f} in {years:.1f} years.')


# The possible pitfalls that arise when using input() are the mismatching data types
# input returns a string, so I have to convert the input into the corresponding data type for the code to work
# Also, user input is problematic, since a user may not enter the correct type (eg a string for a numeric value)