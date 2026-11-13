# Christopher Springer
# 11/12/2026

x = 100
y = 20

# Question 1(a)
if (x / y) == 5:
    print("x divided by y is 5")
    x = 1
else:
    print("are the variables set up correctly?")

# 1(b)
if (x * y) == y:
    print("now x times y is y")
    x = 10
else:
    print(f"Whoops x equals {x}")

# 1(c)
if x < y:
    print('x is less than y')
    x *= 2
else:
    print('uh oh, x is not less than y')

# 1(d)
if x > y:
    print('how is x greater than y??')
else:
    print("x is NOT greater than y")

print(f"The final value of x is {x} and the final value of y is {y}")