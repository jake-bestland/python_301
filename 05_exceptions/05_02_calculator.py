# Write a script that takes in two numbers from the user and calculates the quotient.
# Use a try/except statement so that your script can handle:
#
# - if the user enters a string instead of a number
# - if the user enters a zero as the divisor
#
# Test it and make sure it does not crash when you enter incorrect values.



try:
    num1 = int(input("Please enter a number: "))
    num2 = int(input("Please enter a number to divide your first number by: "))
    answer = num1 / num2
    print(f"The result of {num1} divided by {num2} is {answer}")
except ZeroDivisionError:
    print(f"You can't divide by 0. Please enter a number > 0.")

except ValueError:
    print("You did not enter a number.  Please only use digits as your input")
        