# Christopher Springer
# 11/18/2026
# Exercise 3B Lab 1 

# Create Restaurant class
class Restaurant:
    '''Updated Restuarant information''' # docstring

    # Constructor method
    def __init__(self, rest_name, food_type, number_served = 0, customer_ratings = []):
        self.rest_name = rest_name
        self.food_type = food_type
        self.number_served = number_served
        self.customer_ratings = customer_ratings.copy()

    # Methods
    def describe_rest(self):
        print(f'{self.rest_name} serves {self.food_type}.')

    def rest_open(self):
        print(f'{self.rest_name} is open.')

    def add_num_served(self):
        self.number_served += int(input('How many customers served today? '))

    def print_num_served(self):
        print(f'{self.rest_name} has served {self.number_served} customers.')

    def customer_rating(self):
        while True:
            try:
                rating = int(input('How would you rate your experience today on a scale of 1-5 (5 being excellent)? '))
                if rating >= 1 and rating <= 5:
                    break
                print('Enter a number between 1-5.')
            except ValueError:
                print('You did not enter a valid rating.')
        self.customer_ratings.append(rating)
        self.average = sum(self.customer_ratings) / len(self.customer_ratings)
        print(f'Your rating was {rating}. The average rating for this restaurant is {self.average:.2f}')
            
# Create 3 Restaurant instances 
mcnaldos = Restaurant('McNaldos', 'burgers')
applebapples = Restaurant("Applebapple's", 'entrees')
donkin_donnts = Restaurant("Donkin' Donnts", 'donuts')

# Display results from each method
mcnaldos.print_num_served()
mcnaldos.add_num_served()
mcnaldos.add_num_served()
mcnaldos.print_num_served()
mcnaldos.customer_rating()
mcnaldos.customer_rating()
mcnaldos.customer_rating()
print()
applebapples.print_num_served()
applebapples.add_num_served()
applebapples.add_num_served()
applebapples.print_num_served()
applebapples.customer_rating()
applebapples.customer_rating()
applebapples.customer_rating()
print()
donkin_donnts.print_num_served()
donkin_donnts.add_num_served()
donkin_donnts.add_num_served()
donkin_donnts.print_num_served()
donkin_donnts.customer_rating()
donkin_donnts.customer_rating()
donkin_donnts.customer_rating()