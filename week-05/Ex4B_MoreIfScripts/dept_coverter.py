# Christopher Springer
# 11/12/2026
# Conditional statements Lab 1: match department name to code

dept_num = int(input('Enter department code: '))

match dept_num:
    case 1:
        print('Marketing')
    case 5:
        print('Human Resources')
    case 10:
        print('Accounting')
    case 12:
        print('Legal')
    case 18:
        print('IT')
    case 20:
        print('Customer Relations')
    case _:
        print('No department')