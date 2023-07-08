from app import app, db
from flask import request, jsonify
from app.models import User, Job
from bson import ObjectId
import json

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


# Route for creating a new job
# @app.route('/jobs', methods=['POST'])
# def create_job():
#     data = request.json
#     job = Job(**data)
#     jobs.append(job)
#     return jsonify(job.to_json()), 201

# Route for retrieving a job by ID
@app.route('/jobs/<string:job_id>', methods=['GET'])
def get_job(job_id):
    job = db.jobs.find.one({"_id": ObjectId(job_id)})
    if job:
        job["_id"] = str(job["_id"])
        job_model = Job(**job)
        return job_model.model_dump()
    return jsonify({'error': 'Job not found'}), 404


    # for job in db.jobs.find():
    #     if str(job["_id"]) == job_id:
    #         job["_id"] = str(job["_id"])
    #         return Job(**job).model_dump()
    return jsonify({'error': 'Job not found'}), 404

# Route for updating a job by ID
# @app.route('/jobs/<string:job_id>', methods=['PUT'])
# def update_job(job_id):
#     data = request.json
#     for job in jobs:
#         if str(job.id) == job_id:
#             for field, value in data.items():
#                 setattr(job, field, value)
#             return jsonify(job.to_json())
#     return jsonify({'error': 'Job not found'}), 404

# Route for deleting a job by ID
# @app.route('/jobs/<string:job_id>', methods=['DELETE'])
# def delete_job(job_id):
#     for job in jobs:
#         if str(job.id) == job_id:
#             jobs.remove(job)
#             return jsonify({'message': 'Job deleted'})
#     return jsonify({'error': 'Job not found'}), 404
    
