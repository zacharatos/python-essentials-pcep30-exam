# Nested Lists

# Nested lists are lists that contain other lists as elements.

# 2D Lists (two-dimensional lists or Matrix)
classroom = [
    ['Sally', 'Jane', 'Bob'],
    ['Billy', 'Kyle', 'Joe'],
    ['Sam', 'Sue', 'Tim']
]

# To get the person sitting in the middle
# Second row, which means index 1
# Second column, which means index 1
print(classroom[1][1])  # Kyle

# 3D Lists (three-dimensional lists or Cube)
school = [
    [
        ['Sally', 'Jane', 'Bob'],
        ['Billy', 'Kyle', 'Joe'],
        ['Sam', 'Sue', 'Tim']
    ],
    [
        ['Max', 'Edgar', 'Tom'],
        ['Josh', 'Pete', 'Jim'],
        ['Layla', 'Beth', 'Jill']
    ],
]

# To get the person which is in the second floor
# sitting in the middle of the last row in the classroom
# Second floor, which means index 1
# Last row, which means index 2
# Second column, which means index 1
print(school[1][2][1])  # Beth
