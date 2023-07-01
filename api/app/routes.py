from app import app, db
from flask import request, jsonify


@app.route("/users", methods=["GET"])
def get_all_users():
    users = []

    for user in db.users.find():
        user["_id"] = str(user["_id"])
        users.append(user)

    return jsonify(users)


@app.route("/users", methods=["POST"])
def create_user():
    user = {
        "email": request.json["email"],
        "name": request.json["name"],
        "bio": request.json["bio"],
    }

    db.users.insert_one(user)
    return {"message": "user created"}
