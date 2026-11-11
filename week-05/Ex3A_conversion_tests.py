# Christopher Springer
# 11/11/2026
# Exercise 3A Lab1

# Description:  This script tests various numeric 
#               conversion techniques
# Author: Sam Q. Newprogrammer

a = "   101.1"
b = '55'
c = "403 Stevens" 
d = 'Number 5   '

# conversion for a - "   101.1"
# a_int = int(a) ValueError: invalid literal for int() with base 10: '   101.1'
a_float = float(a)
a_int_float = int(float(a))
a_sliced = str(a[3:]) # has to be casted as a float first then to an int or as a string
a_stripped = a.strip()

print(
    a_float, type(a_float),
    a_int_float, type(a_int_float),
    a_sliced, type(a_sliced),
    a_stripped, type(a_stripped)
    )

# conversion for b - '55'
b_int = int(b) 
b_float = float(b)
b_sliced = int(b[0:])

print(
    b_int, type(b_int),
    b_float, type(b_float),
    b_sliced, type(b_sliced)
    )

# conversion for c - "403 Stevens" 
# c_int = int(c) ValueError: invalid literal for int() with base 10: '403 Stevens'
# c_float = float(c) ValueError: could not convert string to float: '403 Stevens'
c_sliced = int(c[0:3])
print(c_sliced, type(c_sliced))

# conversion for d - 'Number 5   '
# d_int = int(d) ValueError: invalid literal for int() with base 10: 'Number 5   '
# d_float = float(d) ValueError: could not convert string to float: 'Number 5   '
d_sliced = int(d[7:8])
d_stripped = d.strip()

print(
    d_sliced, type(d_sliced),
    d_stripped, type(d_stripped)
    )