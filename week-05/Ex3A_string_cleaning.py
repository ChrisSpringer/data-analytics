# Christopher Springer
# 11/11/2026
# Exercise 3A Lab2

name_1 = "PRIYA SHARMA" 
name_2 = "bob NGUYEN" 
name_3 = "LaTonya Williams" 
salary_1 = "$82,500" 
salary_2 = "$74,000" 

# Convert each name to lower case and print
name_1 = name_1.lower()
name_2 = name_2.lower()
name_3 = name_3.lower()
print(f'{name_1}\n{name_2}\n{name_3}')

# Convert each name to title case and print
name_1 = name_1.title()
name_2 = name_2.title()
name_3 = name_3.title()
print(f'{name_1}\n{name_2}\n{name_3}')

# Replace the $ in the salaries and print
print(salary_1.replace('$', ''), type(salary_1.replace('$', '')))
print(salary_2.replace('$', ''), type(salary_2.replace('$', '')))
# In order to do mathematical operations, the comma must also be replaced
# then both must be casted as ints or floats

# Replacing the $ and , to cast the salary as an int
salary_1 = salary_1.replace('$','')
salary_1 = salary_1.replace(',','')
salary_1 = int(salary_1)
print(salary_1, type(salary_1))