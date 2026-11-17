# Christopher Springer
# 11/17/2026
# Exercise 2C Lab 2

def display_mailing_label(name, address, city, state, zip):
    print(f'{name}\n{address}\n{city}, {state} {zip}\n')

def add_numbers(*numbers):
    result = 0
    print(numbers[0], end = ' ')
    for i in range(len(numbers)):
        result += numbers[i]
        if(i + 1 < len(numbers)):
            print(f'+ {numbers[i+1]}', end = ' ')   
    print(f'= {result}\n')

def display_receipt(total_due, amount_paid):
    print(f'Total due: ${total_due:.2f}')
    print(f'Amount paid: ${amount_paid:.2f}')
    if amount_paid < total_due:
        remaining_balance = total_due - amount_paid
        print(f'Remaining Balance: ${remaining_balance:.2f}\n')
    else:
        change_due = amount_paid - total_due
        print(f'Change Due: ${change_due:.2f}\n')

display_mailing_label('Chris Springer','101 Nice Street', 'Brooklyn',
                      'New York', 10001)
display_mailing_label('John Doe','257 Broadway Avenue', 'Beverly Hills',
                      'California', 90210)

add_numbers(2)
add_numbers(39, 76)
add_numbers(121, 54, 338, 5)

display_receipt(75, 100)
display_receipt(54, 54)
display_receipt(385, 300)