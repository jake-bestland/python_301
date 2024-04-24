# Write a custom exception  that inherits from `Exception()`
# Open and read in the content of the book `.txt` files in the `books/` folder
# like you did in the previous exercise.
# Raise your `PrinceException()` if the first 100 characters of a book
# contain the string "Prince".


from pathlib import Path
class PrinceException(Exception): pass

war_peace_path = Path("//Users/jakebestland/Documents/codingnomads/python-301-main/05_exceptions/books/war_and_peace.txt")
pride_prej_path = Path("/Users/jakebestland/Documents/codingnomads/python-301-main/05_exceptions/books/pride_and_prejudice.txt")
crime_pun_path = Path("/Users/jakebestland/Documents/codingnomads/python-301-main/05_exceptions/books/crime_and_punishment.txt")

try:
        with war_peace_path.open() as war_file:
                wp = war_file.read()
except IOError:
       print("Unable to read in this file. It may be an invalid filename or location.")
       
try:
        with crime_pun_path.open() as crime_file:
                cp = crime_file.read()
except IOError:
       print("Unable to read in this file. It may be an invalid filename or location.")

       
try:
        with pride_prej_path.open() as pride_file:
                pp = pride_file.read()
except IOError:
       print("Unable to read in this file. It may be an invalid filename or location.")

       

try:  
    if "Prince" in wp[0:100]:
        raise PrinceException

except PrinceException:
      print("There is a Prince in the first 100 characters!")