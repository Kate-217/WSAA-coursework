import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rootroot" 
)

mycursor = connection.cursor()

# create a database
mycursor.execute("CREATE database wsaa")

mycursor.close()
connection.close()