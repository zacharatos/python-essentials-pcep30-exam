# List Iteration

# Iterating over a list using a for loop
ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]
total_of_ages = 0
for age in ages:
    total_of_ages += age

average = total_of_ages / len(ages)

print(total_of_ages)
print(average)

# Iterating over a list using a while loop
ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]
total_of_ages = 0
index = 0
while index < len(ages):
    total_of_ages += ages[index]
    index += 1

average = total_of_ages / len(ages)
print(total_of_ages)
print(average)
