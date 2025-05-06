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
    return render_template("index.html", results=swimDAO.get_all())

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

    return jsonify(swimDAO.create(swimmer))


# find by ID 
@app.route("/results/<int:id>", methods=['GET'])
def find_swimmer(id):
    swimmer = swimDAO.find_by_id(id)
    if swimmer:
        return jsonify(swimmer)
    else:
        return jsonify({"message": "Swimmer is not found"})


# find by age
@app.route("/results/age/<int:age_group>", methods=['GET'])
def find_by_age(age_group):
    #print("age group:",age_group)
    swimmers = swimDAO.find_by_age_group(age_group)
    #print("found:", swimmers)
    if swimmers:
        return jsonify(swimmers)
    else:
        return jsonify({"message": "Swimmers are not found"})

# curl http://127.0.0.1:5000/results/age/12
    
# only girls
@app.route("/results/girls", methods=['GET'])
def get_girls():
    swimmers = swimDAO.find_girls()
    if swimmers:
        return jsonify(swimmers)
    else:
        return jsonify({"message": "No female swimmers found"})

# curl http://127.0.0.1:5000/results/girls


# only boys
@app.route("/results/boys", methods=['GET'])
def get_boys():
    swimmers = swimDAO.find_boys()
    if swimmers:
        return jsonify(swimmers)
    else:
        return jsonify({"message": "No  swimmers found"})

# curl http://127.0.0.1:5000/results/boys

# update
@app.route("/results/<int:id>", methods=['PUT'])
def update_result(id):
    jsonstring = request.json
    swimmer = swimDAO.find_by_id(id)
    
    if not swimmer:
        return jsonify({"message": "Swimmer is not found"})

    swimmer = {}
    new_data = ["first_name", "last_name", "sex", "age_group", "event", "date", "time"]
    for i in new_data:
        if i in jsonstring:
            swimmer[i] = jsonstring[i]

    return jsonify(swimDAO.update(id, swimmer))

# delete
@app.route("/results/<int:id>", methods=['DELETE'])
def delete_record(id):
    swimmer = swimDAO.find_by_id(id)
    
    if not swimmer:
        return jsonify({"message": "Swimmer is not found"})
    return jsonify(swimDAO.delete(id))

# curl -X DELETE http://127.0.0.1:5000/results/1




if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
