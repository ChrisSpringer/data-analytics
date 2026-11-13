# Christopher Springer
# 11/12/2026
# Loops Lab 3: ranked list

favorite_foods = ['oxtail','lasagna','mac and cheese',
                  'shrimp','quesadilla','chicken']

for i, food in enumerate(reversed(favorite_foods), start = 1):
    if i == 1:
        print(f'{i}. {food} <- top pick!')
    else:
        print(f'{i}. {food}')