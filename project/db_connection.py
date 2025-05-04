import mysql.connector
from db_config import db_config 

# connection to db
def get_connection():
    try:
        connection = mysql.connector.connect(
        host = db_config["host"],
        user = db_config["user"],
        password = db_config["password"],
        database = db_config["database"])
        return connection
        
    except mysql.connector.Error as e:
        print(f"Connection Error: {e}")
        
