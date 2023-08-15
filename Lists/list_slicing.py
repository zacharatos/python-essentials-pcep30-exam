# List Slicing

# List slicing is a way to get a subset of elements from a list. It is done by specifying the index of the first
# element to be included and the index of the first element to be excluded.
# The syntax is as follows:
# list[start:end]
# The start index is inclusive and the end index is exclusive.

# Important: Using slicing we create a new list.
# That is the way to create a copy from a list without modifying the original list.

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

# The first two letters
first_two_letters = letters[0:2]
print(first_two_letters)

# All the letters except the first two
all_except_first_two_letters = letters[2:]
print(all_except_first_two_letters)

# All the letters until letter at index 3
all_letters_until_index_3 = letters[:3]
print(all_letters_until_index_3)

# All the letters except the last two
all_except_last_two_letters = letters[:-2]
print(all_except_last_two_letters)
