# Dictionary

# Create a dictionary
my_dict = {
    'user1': 'username1',
    'user2': 'username2'
}

# Print the dictionary
print(my_dict["user1"])

# Iterate over a dictionary
for key in my_dict.keys():
    print(my_dict[key])

# Modify an element of a dictionary
my_dict["user1"] = "new_username1"
print(my_dict["user1"])

# Add an element to a dictionary
my_dict["user3"] = "username3"
my_dict.update({"user4": "username4"})
print(my_dict)

# Delete an element from a dictionary
del my_dict["user2"]

# Remove all elements of a dictionary
my_dict.clear()
print(my_dict)
