import mysql.connector

# connection to db
def get_connection():
    connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rootroot",
    database="swimmers")
    return connection
