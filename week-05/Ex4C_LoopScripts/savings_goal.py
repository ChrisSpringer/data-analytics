# Christopher Springer
# 11/12/2026
# Loops Lab 2

bank_balance = 0
savings_goal = 1000
weekly_savings_amount = 120

while bank_balance < savings_goal:
    bank_balance += weekly_savings_amount
    if bank_balance >= savings_goal * .75:
        bank_balance -= 25
        print(f'So close! After treating myself, my balance is up to ${bank_balance}')
    elif bank_balance > savings_goal / 2:
        print(f'Almost There! This week my balance increased to ${bank_balance}')
    else:
        print(f'This week my balance increased to ${bank_balance}')

print(f'Goal met! My current balance is ${bank_balance}')