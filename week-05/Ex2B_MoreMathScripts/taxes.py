# Christopher Springer
# 11/10/2026

# Federal taxes are 23% of your salary
federal_taxes = 0.23

# Have user input their salary
salary = int(input("How much is your salary? "))

# Calculate the amount withheld for taxes
withheld = salary * federal_taxes

# Display results accounting for any stray decimals using round()
print(f"{round(withheld, 2)} is withheld for taxes")