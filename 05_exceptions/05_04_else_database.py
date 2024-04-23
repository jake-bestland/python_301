# Write a script that demonstrates a try/except/else statement.
# For example, you can revisit the course module about database interactions
# and include a try/except/else statement based on what to do whether or not
# the database connection can be established.

import sqlalchemy

try:
    engine = sqlalchemy.create_engine('mysql+pymysql://root:password@localhost/desk_file_count')
    connection = engine.connect()
    metadata = sqlalchemy.MetaData()

except ModuleNotFoundError:
    print("You need to install PyMySQL in order to connect to the database.")

except RuntimeError:
    print("You did not gain access to the database.  Please enter the correct password.")

else:
    print("You are now connected to the database.")