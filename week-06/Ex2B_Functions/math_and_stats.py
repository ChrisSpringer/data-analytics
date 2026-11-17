# Christopher Springer
# 11/16/2026
# Exercise 2B Lab 3

import random
import math
import statistics

vals_1_100 = range(1,100)
vals_sample = random.sample(vals_1_100, 75)
vals_choices = random.choices(vals_1_100, k = 200)
radius = random.randint(3,10)
pi = math.pi

print('_Experimenting with a subset of integer 1-100:')
print(f'Sum of 75 sample values from 1 to 100: {math.fsum(vals_sample)}')
print(f'Average of 75 sample values: {statistics.mean(vals_sample):.2f}')
print(f'Median of 75 sample values: {statistics.median(vals_sample)}\n')

print('_Experimenting with a superset of 200 values, integers 1-100:')
print(f'Average of 200 values: {statistics.mean(vals_choices):.2f}')
print(f'Median of 200 values: {statistics.median(vals_choices)}')
print(f'Mode of 200 values: {statistics.mode(vals_choices)}')
print(f'Standard Deviation 200 values: {statistics.stdev(vals_choices):.2f}')
print(f'Variance of 200 values: {statistics.variance(vals_choices):.2f}\n')

area = pi * math.pow(radius,2)

print('_Modeling a random circle:')
print(f'Radius = {radius}, area = {math.ceil(area)}')
print(f'Radius = {radius}, area = {math.floor(area)}')
