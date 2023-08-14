# While Loop

# A while loop is a control flow statement that allows code to be executed repeatedly
# based on a given Boolean condition.
secret_number = 7
user_guess = int(input("Guess the secret number (0-9): "))
while user_guess != secret_number:
    user_guess = int(input("Guess the secret number (0-9): "))
else:
    print("You guessed it!")

# For Loop

# A for loop is a control flow statement that allows code to be executed repeatedly
# based on a given Boolean condition.
for i in range(10):
    print(i)

for i in range(5):
    if i == 3:
        break
    print(i)

for i in range(6):
    if i == 3:
        continue
    print(i)
    