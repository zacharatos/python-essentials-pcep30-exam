# Errors and Exceptions

# You can use try and except to handle errors from application

try:
    user_input = int(input("Enter a number: "))
    result = 10 / user_input
    print(result)
except ZeroDivisionError:
    print("You can't divide by zero")
except ValueError:
    print("You must enter a number")
# Python doesn't have a general exception handler and needs
# to catch each exception which can be in the app separately
# except:
#    print("Something went wrong")

# Hierarchical Exceptions
# You can use the hierarchy of exceptions to catch multiple exceptions
try:
    user_input = int(input("Enter a number: "))
    result = 10 / user_input
    print(result)
except ArithmeticError:
    # You can use the parent exception to catch all the child exceptions,
    # like ZeroDivisionError and others
    print("You can't divide by zero")
except ValueError:
    print("You must enter a number")

# Order matters in exception handling branches so if you want to catch
# some exceptions in the same level you can do by using ():
try:
    user_input = int(input("Enter a number: "))
    result = 10 / user_input
    print(result)
except (ZeroDivisionError, ValueError):
    print("Same level exceptions")
except ValueError:
    print("You must enter a number")

# You can use assert to validate your data and raise an exception
# if something wrong
try:
    user_input = int(input("Enter a number: "))
    assert user_input != 0
    result = 10 / user_input
    print(result)
except AssertionError:
    print("Error in validation of data")
