# Read in the first number from `integers.txt`
# and perform a calculation with it.
# Make sure to catch at least two possible Exceptions (`IOError` and `ValueError`)
# with specific `except` statements, and continue to do the calculation
# only if neither of them applies.

from pathlib import Path

file_path = Path("/Users/jakebestland/Documents/codingnomads/python-301-main/05_exceptions/integers.txt")

try:
    # file_name = 'integers.txt'

    # with open(file_name, "r") as int_file:
    #     numbers = int_file.read()
    with file_path.open() as int_file:
        numbers = int_file.read()
        # num_list = [int(n) for n in numbers]
        num_list = [int(n) for n in numbers.split()]
    print(num_list)


except IOError:
    print("Cannot read in this file. This is an invalid filename or location.  Add a path to the file in order to correctly read it in.")

except ValueError:
    print("This is not a valid integer. split the text to get rid of '/n' contained in the string.")

else:
    print(f"{num_list[0] * 2}")
