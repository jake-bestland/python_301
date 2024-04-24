# In this exercise, you will practice both File I/O as well as using Exceptions
# in a real-world scenario.
#
# This folder contains another folder called `books/` that contains three text files
# of books from Project Gutenberg:
# 1. war_and_peace.txt
# 2. pride_and_prejudice.txt
# 3. crime_and_punishment.txt
#
# 1) Open `war_and_peace.txt`, read the whole file content and store it in a variable
# 2) Open `crime_and_punishment.txt` and overwrite the whole content with an empty string
# 3) Loop over all three files and print out only the first character each. Your program
#    should NEVER terminate with a Traceback.
#     a) Which exception can you expect to encounter? Why?
#     b) How do you catch it to avoid the program from terminating with a traceback?


from pathlib import Path

war_peace_path = Path("//Users/jakebestland/Documents/codingnomads/python-301-main/05_exceptions/books/war_and_peace.txt")
pride_prej_path = Path("/Users/jakebestland/Documents/codingnomads/python-301-main/05_exceptions/books/pride_and_prejudice.txt")
crime_pun_path = Path("/Users/jakebestland/Documents/codingnomads/python-301-main/05_exceptions/books/crime_and_punishment.txt")

file_list = []
try:
        with war_peace_path.open() as war_file:
                wp = war_file.read()
                file_list.append(wp)
except IOError:
       print("Unable to read in this file. It may be an invalid filename or location.")

try:
        with crime_pun_path.open() as crime_file:
                cp = crime_file.read()
                cp = ""
                file_list.append(cp)
except IOError:
       print("Unable to read in this file. It may be an invalid filename or location.")

try:
        with pride_prej_path.open() as pride_file:
                pp = pride_file.read()
                file_list.append(pp)
except IOError:
       print("Unable to read in this file. It may be an invalid filename or location.")

try:
    for file in file_list:
        print(file[0])

except IndexError:
      print("This is an empty file and doesn't have any characters")
