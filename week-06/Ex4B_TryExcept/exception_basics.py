# Christopher Springer
# 11/19/2026
# Exercise 4B Lab 1 Working with exceptions

try:
    rating = int(input('Enter a number: '))
except ValueError:
    print("You did not enter the right input for this variable's datatype")
else:
    print(rating)
finally:
    print("Let's try another one")

try:
    print(rate)
    rate = 0.5
except NameError:
    print("You called a variable before defining it")
else:
    print(rate)
finally:
    print("Let's try another one")

try:
    double = "hello" + 2
except TypeError:
    print("The value has to be the correct datatype")
else:
    print(double)
finally:
    print("Let's try another one")

# Syntax error cannot be caught since it is found before the code executes
try:
    print ("Hello")
except SyntaxError:
    print("The syntax is off somewhere")
else:
    print("No error detected")
finally:
    print("Let's try another one")