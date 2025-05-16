import mysql.connector
from db_config import db_config

connection = mysql.connector.connect(
    host = db_config["host"],
    user = db_config["user"],
    password = db_config["password"]
)

mycursor = connection.cursor()

# create a database
# https://dev.mysql.com/doc/refman/8.4/en/drop-database.html
mycursor.execute("DROP DATABASE IF EXISTS swimmers")
mycursor.execute("CREATE DATABASE swimmers")


# disconnect in order to connect to just created database
mycursor.close()
connection.close()

# reconnection to swimmers 
connection = mysql.connector.connect(
    host = db_config["host"],
    user = db_config["user"],
    password = db_config["password"],        
    database="swimmers"
)

mycursor = connection.cursor()

# create a table
sql = """
CREATE TABLE results(
    id INT AUTO_INCREMENT PRIMARY KEY, 
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    sex ENUM('M', 'F'),
    age_group INT,
    event VARCHAR(50),
    date DATE,
    time VARCHAR(10)
    )"""
mycursor.execute(sql)

# create test data
sql = """
INSERT INTO results (first_name, last_name, sex, age_group, event, date, time)
VALUES (%s, %s, %s, %s, %s, %s, %s)
"""
values = ("Kate", "Smith", "F", 12, "50 Freestyle", "2025-02-01", "00:35:36")

mycursor.execute(sql,values)
connection.commit()
mycursor.close()
connection.close()



