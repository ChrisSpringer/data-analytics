# Christopher Springer
# 11/17/2026
# Exercise 2D Lab 1 Lambdas & Generators

doubler = lambda n: n * 2

print(doubler(8))
print(doubler(-4))
print(doubler('banana'))

tripler = lambda n: n * 3

print(tripler(8))
print(tripler(-4))
print(tripler('banana'))

def multiplier(num):
    return lambda n: n * num

quadrupler = multiplier(4)
quintupler = multiplier(5)
sextupler = multiplier(6)
septupler = multiplier(7)
octupler = multiplier(8)
nonupler = multiplier(9)
decupler = multiplier(10)

print(quadrupler(4))
print(quintupler(4))
print(sextupler(4))
print(septupler(4))
print(octupler(4))
print(nonupler(4))
print(decupler(4))