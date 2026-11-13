# Christopher Springer
# 11/12/2026
# Conditional statements Lab 2: greeting based on hour

time = int(input('Enter the hour (0-23): '))

if time < 10:
    print("Good morning!")
elif time < 17:
    print("Good day!")
elif time <= 23:
    print('Good evening!')

if time == 23 or time <= 4:
    print('What are you doing up so late??')