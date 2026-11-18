# Christopher Springer
# 11/18/2026
# Exercise 3A Lab 1 

# Create Restaurant class
class Restaurant:
    '''Restuarant information''' # docstring

    # Constructor method
    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type

    # Methods
    def describe_rest(self):
        print(f'{self.rest_name} serves {self.food_type}.')

    def rest_open(self):
        print(f'{self.rest_name} is open.')

# Create 3 Restaurant instances 
mcnaldos = Restaurant('McNaldos', 'burgers')
applebapples = Restaurant("Applebapple's", 'entrees')
donkin_donnts = Restaurant("Donkin' Donnts", 'donuts')

# Display results from each method
mcnaldos.describe_rest()
mcnaldos.rest_open()
print()
applebapples.describe_rest()
applebapples.rest_open()
print()
donkin_donnts.describe_rest()
donkin_donnts.rest_open()