# Christopher Springer
# 11/12/2026
# Conditional statements Lab 3

# Gather info from the user
pay_rate = float(input('Enter your pay rate: '))
hours_worked = int(input('Enter hours worked: '))
file_status = input('Enter filing status(single or joint): ')
total_hours = hours_worked * 52

# Create variables to find out overtime hours and rate if applicable
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    overtime_rate = pay_rate * 1.5
    gross_pay = (hours_worked - overtime_hours) * pay_rate
    gross_pay = gross_pay + (overtime_hours * overtime_rate)
else:
    gross_pay = hours_worked * pay_rate

# Calculate annual gross pay
annual_pay = gross_pay * 52

# Adjust tax rate based on filing status
if file_status == 'single':
    if annual_pay < 12000:
        tax_rate = 0.5
    elif annual_pay < 25000:
        tax_rate = 0.10
    elif annual_pay < 75000:
        tax_rate = 0.15
    else:
        tax_rate = 0.20
elif file_status == 'joint':
    if annual_pay < 12000:
        tax_rate = 0
    elif annual_pay < 25000:
        tax_rate = 0.6
    elif annual_pay < 75000:
        tax_rate = 0.11
    else:
        tax_rate = 0.20

# Calculate weekly tax withheld from WEEKLY gross pay and weekly net pay
withheld_taxes = gross_pay * tax_rate
net_pay = gross_pay - withheld_taxes

print(f'Your annual income is {annual_pay:.2f}')
print(f'You worked {hours_worked} hours this period.')
print(f'Because you earn ${pay_rate:.2f} per hour, your gross weekly pay is ${gross_pay:.2f}')
print(f'Your filing status is {file_status}')
print(f'Your {(tax_rate * 100)}% tax withholding for the week is ${withheld_taxes:.2f}')
print(f'Your net pay is ${net_pay:.2f}')