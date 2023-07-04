from app import app, db
from flask import request, jsonify
from app.models import User


@app.route("/users", methods=["GET"])
def get_all_users():
    users = []

    for json in db.users.find():
        json["_id"] = str(json["_id"])
        users.append(User(**json).model_dump())

    return users


@app.route("/users", methods=["POST"])
def create_user():
    user = User(**request.json)
    insert_result = db.users.insert_one(user.model_dump())

    user.id = str(insert_result.inserted_id)

    return user.model_dump()
