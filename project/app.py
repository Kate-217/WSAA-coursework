from flask import Flask, request, jsonify, render_template, abort

# import function to co connect to MySQL DB
from db_connection import get_connection

# import Data Access Object class swimmers
from swimmers_skeleton import swimDAO


app = Flask(__name__, static_url_path='', static_folder='static')


# https://planetscale.com/learn/courses/mysql-for-python-developers/using-mysql-with-python/using-cursors
# set the dictionary=True option to have the cursor return results
# as a list of dictionaries instead of the default tuple of tuples.

@app.route("/")
def home():
    sql = "SELECT * FROM results LIMIT 30"
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql)
    sql_results = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template("index.html", results=sql_results)

# to get all swimmers
@app.route("/results", methods=['GET'])
def get_swimmers():
    return jsonify(swimDAO.get_all())

# create a new result
@app.route("/results", methods=['POST'])
def create_result():
    jsonstring = request.json
    swimmer = {}

    new_data = ["first_name", "last_name", "sex", "age_group", "event", "date", "time"]
    for i in new_data:
        if i not in jsonstring:
            abort(400, description=f'Missing required field: {i}')
        swimmer[i] = jsonstring[i]

    return jsonify(swimDAO.create(swimmer)), 201


# find by ID 
@app.route("/results/<int:id>", methods=['GET'])
def find_swimmer(id):
    swimmer = swimDAO.find_by_id(id)
    if swimmer:
        return jsonify(swimmer)
    else:
        return jsonify({"message": "Swimmer is not found"})






if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
