# Conditional Statements

# if statement
age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult")

# if-else statement
age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult")
else:
    print("You are a child")

# if-elif-else statement
age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult")
elif age >= 13:
    print("You are a teenager")
else:
    print("You are a child")

# Nested if statement
age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult")
    if age >= 65:
        print("You are a senior")
