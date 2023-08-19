# Tuples
# Are immutable
# Are faster than lists
# Are used to protect data

# Create a tuple
aTuple = (1, 2, 3, 4, 5)
another_tuple = 1, 2, 3, 4, 5
print(aTuple)
print(another_tuple)

# Read data from a tuple
print(aTuple[0])
print(aTuple[1:3])
for item in aTuple:
    print(item)

# Create a tuple with one element
aTuple = (1,)
print(aTuple)
