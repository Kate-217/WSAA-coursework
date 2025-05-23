from flask import Flask, request, jsonify, render_template, abort

# import function to co connect to MySQL DB
from db_connection import get_connection

# import Data Access Object class swimmers
from swimmers_skeleton import swimDAO


app = Flask(__name__)


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

# curl http://127.0.0.1:5000/results


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
# curl -X POST http://127.0.0.1:5000/results -H "Content-Type: application/json" -d '{"first_name":"Anna","last_name":"Smith","sex":"F","age_group":12,"event":"100m Freestyle","date":"2025-05-20","time":"00:01:23"}'



# find by ID 
@app.route("/results/<int:id>", methods=['GET'])
def find_swimmer(id):
    swimmer = swimDAO.find_by_id(id)
    if swimmer:
        return jsonify(swimmer)
    else:
        return jsonify({"message": "Swimmer is not found"})

# curl http://127.0.0.1:5000/results/1



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
    existing_swimmer = swimDAO.find_by_id(id)
    
    if not existing_swimmer:
        return jsonify({"message": "Swimmer is not found"})

    updated_swimmer = {}
    new_data = ["first_name", "last_name", "sex", "age_group", "event", "date", "time"]
    for i in new_data:
        if i in jsonstring:
            updated_swimmer[i] = jsonstring[i]

    return jsonify(swimDAO.update(id, updated_swimmer))

# curl -X PUT http://127.0.0.1:5000/results/1 -H "Content-Type: application/json" -d '{"first_name": "Sofia", "last_name": "PPPPPP", "sex": "F", "age_group": 13, "event": "200m IM", "date": "2025-05-25", "time": "00:02:05"}'



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
    
