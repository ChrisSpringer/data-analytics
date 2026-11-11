# Christopher Springer
# 11/11/2026
# Exercise 3B Lab 3

# Dictionary with contact info
contact_info = {
    #"name": "Chris Springer",
    "address": "86 Broad Street",
    "city": "Brooklyn",
    "state": "New York",
    "ZIP": 10004
}

# Displays the contact info in mailing format
print(#f'{contact_info["name"]}\n
    f'{contact_info["address"]}\n\
{contact_info["city"]}, {contact_info["state"]} {contact_info["ZIP"]}'
      )

# Creates new dictionary for full name
full_name = {
    "first name": "Chris",
    "last name": "Springer"
}

# Updates the dictionary to add honorific title
full_name.update({"honorific": "Mr."})

# Adds full name dictionary to contact info dictionary
contact_info.update(full_name)

# Displays updated contact info
print(f'{contact_info["honorific"]}{contact_info["first name"]} \
{contact_info["last name"]} \n{contact_info["address"]}\n\
{contact_info["city"]}, {contact_info["state"]} {contact_info["ZIP"]}'
      )