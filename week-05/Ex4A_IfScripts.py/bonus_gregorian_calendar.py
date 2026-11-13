# Christopher Springer
# 11/12/2026
# leap year

year = int(input('Enter the year: '))

if (year % 4 == 0) & (year % 100 != 0):
    print(f"{year} is a leap year.")
elif year % 400 == 0:
    print(f'{year} is a leap year.')
else:
    print(f'{year} is NOT a leap year.')