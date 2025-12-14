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

db = 'alx_book_store'

try:
    mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print('Database created successfully!')
except mysql.connector.Error as err:
    # Error code 1007 means database already exists
    if err.errno == 1007:
        raise DatabaseAlreadyExist(db)
    else:
        raise




