# Function
#   - Function is a block of code which only runs when it is called.
# Functions can return some value with the return keyword, or they
# can return no value and instead just do some action in their body

# Functions have their own scope and can't access variables from other scopes, only from global scope.
# Also, variables defined inside a function's scope can't be accessed from outside the function.

# If you want a variable which is defined inside a function to be accessible from outside the function,
# you can use the global keyword and the name of the variable.

# Creating a Function
def input_number():
    return int(input("Enter a number: "))


# Using a Function
input1 = input_number()
input2 = input_number()
print(input1, input2)


# We can pass values into a function as parameters.
# These values can be numbers, but also lists, dictionaries, strings, etc.
def user_number_plus_offsets(offset1, offset2):
    return int(input("Enter a number: ")) + offset1 + offset2


# The position of the number we pass as input in the function matters.
print(user_number_plus_offsets(1, 2))

# If we want the position of the number we pass as input in the function not to matter,
# we can use keyword arguments.
print(user_number_plus_offsets(offset2=2, offset1=1))


# Functions also can have default values for parameters.
def user_number_plus_offsets_with_default_values(offset1=-1, offset2=-2):
    return int(input("Enter a number: ")) + offset1 + offset2


print(user_number_plus_offsets_with_default_values())
print(user_number_plus_offsets_with_default_values(1, 2))
