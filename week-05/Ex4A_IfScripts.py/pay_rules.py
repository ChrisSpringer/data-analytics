# Christopher Springer
# 11/12/2026

# Gather info from the user
pay_rate = float(input('Enter your pay rate: '))
hours_worked = int(input('Enter hours worked: '))

# Create variables to find out overtime hours and rate if applicable
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    overtime_rate = pay_rate * 1.5
    gross_pay = (hours_worked - overtime_hours) * pay_rate
    gross_pay = gross_pay + (overtime_hours * overtime_rate)
else:
    gross_pay = hours_worked * pay_rate

print(f'Your gross pay is ${gross_pay:.2f}')