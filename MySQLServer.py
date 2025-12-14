import mysql.connector

# Replace with your connection details
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="leunamme5002$"
)
mycursor = mydb.cursor()


# Create error to handle db already exist
class DatabaseAlreadyExist(Exception):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f'{self.name} has already been created'

mycursor.execute("SHOW DATABASES")

db = 'alx_book_store'

# Extract database names from tuples
databases = [database[0] for database in mycursor.fetchall()]

if db in databases:
    raise DatabaseAlreadyExist(db)
else:
    mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print('Database created successfully!')