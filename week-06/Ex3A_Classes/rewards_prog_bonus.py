# Christopher Springer
# 11/18/2026
# Exercise 3A Lab 2

# Create class
class RewardsProgram:
    '''Create a Rewards Program''' # docstring

    # Constructor Method
    def __init__(self, cust_name, phone, email):
        self.cust_name = cust_name
        self.phone = phone
        self.email = email

    # Methods
    def profile(self):
        print(f'Name: {self.cust_name}')
        print(f'Phone: {self.phone}')
        print(f'Email: {self.email}')

    def thank_you(self):
        print(f'Thank you, {self.cust_name}, for visiting our restaurant!')

    def add_to_cust_list(self):
        customer = (self.cust_name, self.phone, self.email)
        cust_list.append(customer)

cust_list = []

cust1 = RewardsProgram('Ruby Bridges', '555-0129', 'sample1@email.com')
cust2 = RewardsProgram('Sam Tucker', '123-4567', 'sample2@email.com')
cust3 = RewardsProgram('Jane Doe', '347-2940', 'sample3@email.com')

cust1.profile()
cust1.thank_you()
cust1.add_to_cust_list()
print()
cust2.profile()
cust2.thank_you()
cust2.add_to_cust_list()
print()
cust3.profile()
cust3.thank_you()
cust3.add_to_cust_list()
print()
print(cust_list)