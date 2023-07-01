from app import app, db
from flask import request, jsonify
from app.models import User


@app.route("/users", methods=["GET"])
def get_all_users():
    users = []

    for json in db.users.find():
        users.append(User(**json).to_json())

    return jsonify(users)


@app.route("/users", methods=["POST"])
def create_user():
    user = User(**request.json)
    db.users.insert_one(user)

    return user.to_json()
