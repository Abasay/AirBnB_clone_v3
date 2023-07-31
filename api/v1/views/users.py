#!/usr/bin/python3
"""Creating a new view for User objects"""

from api.v1.views import app_views
from flask import jsonify, request, abort, make_response
from models import storage
from models.user import User
import json


@app_views.route('/users', strict_slashes=False, methods=['GET'])
def handle_users():
    """return users in json"""
    if request.method == 'GET':
        users = []
        for user in storage.all('User').values():
            users.append(user.to_dict())
        return jsonify(users)


@app_views.route('/users/<user_id>', strict_slashes=False, methods=['GET'])
def fetch_single_user(user_id):
    '''fetch single user'''
    user = storage.get('User', user_id)
    if not user:
        abort(404)
    return jsonify(user.to_dict())


@app_views.route('/users', strict_slashes=False, methods=['POST'])
def post_user():
    """function to post user"""
    if not request.get_json():
        return jsonify({"error": "Not a JSON"}), 400
    user = request.get_json()
    if not user['email']:
        return jsonify({"error": "Missing email"}), 400
    if not user['password']:
        return jsonify({"error": "Missing password"}), 400
    newInstance = User(user)
    newInstance.email = user["email"]
    newInstance.password = user["password"]
    newInstance.first_name = user["first_name"]
    newInstance.last_name = user["last_name"]
    storage.new(newInstance)
    storage.save()
    return jsonify(newInstance.to_dict()), 201


@app_views.route('/users/<user_id>', strict_slashes=False, methods=['PUT'])
def put_user(user_id):
    """Function that update user"""
    if not request.get_json():
        return jsonify({"error": "Not a JSON"}), 400
    obj = storage.get("User", user_id)
    if not obj:
        abort(404)
    requestObj = request.get_json()
    obj.password = requestObj["password"]
    if requestObj["first_name"]:
        obj.first_name = requestObj["first_name"]
    if requestObj["last_name"]:
        obj.last_name = requestObj["last_name"]
    obj.save()
    return jsonify(obj.to_dict()), 200


@app_views.route('/users/<user_id>',
                 strict_slashes=False, methods=['DELETE'])
def delete_user(user_id):
    """Function that delete user"""
    obj = storage.get("user", user_id)
    if not obj:
        abort(404)
    storage.delete(obj)
    storage.save()
    return jsonify({}), 200
