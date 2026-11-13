# Christopher Springer
# 11/12/2026
# Exercise 4D

import random

num = random.randint(1,10)

guess = int(input('Enter a guess from 1-10: '))
count = 1
if guess == num:
    print('You got it!')

list_guesses = []
list_guesses.append(guess)

while guess != num:
    if guess < num:
        print("That was not it. :( Higher! ")
    elif guess > num:
        print("That was not it. :( Lower! ")
    else:
        print('That was the number!')
    guess = int(input('Enter another guess: '))
    list_guesses.append(guess)
    count += 1

print(list_guesses)

if count < 5:
    print(f"You're awesome! You got it in {count} guesses")
else:
    print(f'You got it in {count} guesses')

