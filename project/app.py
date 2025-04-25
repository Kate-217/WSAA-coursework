from flask import Flask, render_template
from db_connection import get_connection

app = Flask(__name__)


# https://planetscale.com/learn/courses/mysql-for-python-developers/using-mysql-with-python/using-cursors
# set the dictionary=True option to have the cursor return results
# as a list of dictionaries instead of the default tuple of tuples.

@app.route("/")
def home():
    sql = "SELECT * FROM results"
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql)
    sql_results = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template("index.html", results=sql_results)

if __name__ == "__main__":
    app.run(debug=True)
