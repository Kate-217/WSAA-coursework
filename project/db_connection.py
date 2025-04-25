import mysql.connector

# connection to db
def get_connection():
    try:
        connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="rootroot",
        database="swimmers")
        return connection
    except mysql.connector.Error as e:
        print(f"Connection Error: {e}")
        
