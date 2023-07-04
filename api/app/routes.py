from app import app, db
from flask import request, jsonify
from app.models import User

# Read all users
@app.route("/users", methods=["GET"])
def get_all_users():
    users = []

    for json in db.users.find():
        json["_id"] = str(json["_id"])
        users.append(User(**json).model_dump())

    return users

# Create one user
@app.route("/users", methods=["POST"])
def create_user():
    user = User(**request.json)
    insert_result = db.users.insert_one(user.model_dump())
    
    user.id = str(insert_result.inserted_id)

    return user.model_dump()

# Read individual user by ID
@app.route("/users/<id>", methods=["GET"])
def get_user(id):
    user = db.users.find_one({'_id': id})
    return jsonify(user)

# Update individual user 
@app.route('/update/<id>', methods=['PUT'])
def update_user(id):
    _id = id
    _json = request.json
    _name = json['name']
    _email = json['email']
    _bio = json['bio']

# Delete one user
@app.route('/delete/<id>', methods=['DELETE'])
def delete_user(id):
    db.users.delete_one({'id': id})
    resp = jsonify("User deleted successfully")
    resp.status_code = 200
    return resp
