# List Methods

countries = ['Greece', 'USA', 'UK', 'Canada']
# Append a new item to the list
countries.append('Italy')
print(countries)

# Insert a new item at a specific index
countries.insert(1, 'France')
print(countries)

# Swap the items at index 0 and 1
countries[0], countries[1] = countries[1], countries[0]
print(countries)

# Sort the list
countries.sort()
print(countries)

# Reverse the list
countries.reverse()
print(countries)
