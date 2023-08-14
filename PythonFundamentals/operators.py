# Arithmetic operators
# + - * / % ** //

# Operators Priority
# 1. Parentheses
# 2. Exponentiation
# 3. Multiplication, Division, Floor division, Modulus
# 4. Addition, Subtraction

# ** Exponentiation
print(2 ** 3)

# * Multiplication
print(2 * 3)
print(2. * 3.)

# / Division
# Returns always a float
print(10 / 5)
print(10. / 5.)

# // Floor division
# Returns float or integer depending on the operands
# Also, rounds the result down to the nearest whole number
print(10 // 5)
print(10. // 5.)

# % Modulus
# Returns the remainder of the division
print(10 % 5)
print(10 % 3)

# + Addition
print(2 + 3)

# - Subtraction
print(2 - 3)

# Comparison operators
# == != > < >= <=

# == Equal
# Checks if the values of two operands are equal or not
print(2 == 3)

# != Not equal
# Checks if the values of two operands are equal or not
print(2 != 3)

# > Greater than
# >= Greater than or equal to
# Checks if the value of the left operand is greater than the value of the right operand
print(2 > 3)
print(2 >= 3)

# < Less than
# <= Less than or equal to
# Checks if the value of the left operand is less than the value of the right operand
print(2 < 3)
print(2 <= 3)

# Logical operators
# and or not

# and Logical AND
# If both the operands are true then condition becomes true
print(True and True)

# or Logical OR
# If any of the two operands are non-zero then condition becomes true
print(True or False)

# not Logical NOT
# Used to reverse the logical state of its operand
print(not True)

# Bitwise operators
# & | ^ ~ << >>

# & Bitwise AND (conjunction)
x = 10  # 1010
y = 4  # 0100
print(bin(x))
print(bin(y))
print(10 & 4)  # 0000

# | Bitwise OR (disjunction)
print(10 | 4)  # 1110

# ^ Bitwise XOR (exclusive disjunction)
print(10 ^ 4)  # 1110

# ~ Bitwise NOT (negation)
print(~10)  # -11

# Bit Shifting

# << Bitwise left shift
# Shifts the bits of the number to the left and fills 0 on voids left as a result
print(10 << 2)  # 101000

# >> Bitwise right shift
# Shifts the bits of the number to the right and fills 0 on voids left as a result
print(10 >> 2)  # 10
