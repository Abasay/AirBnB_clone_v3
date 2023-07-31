#!/usr/bin/python3
"""Creating a new view for city objects"""

from api.v1.views import app_views
from flask import jsonify, request, abort, make_response
from models import storage
from models.state import State
from models.city import City
from models.place import Place
import json


@app_views.route('/cities/<city_id>', strict_slashes=False, methods=['GET'])
def handle_place(place_id):
    """return places in json"""
    if request.method == 'GET':
        place = {}
        for pl in storage.all('Place').values():
            if pl.to_dict().get('id') == place_id:
                city = ci.to_dict()
        if not city:
            abort(404)
        return jsonify(city)


@app_views.route('/cities/<city_id>/places',
                 strict_slashes=False, methods=['GET'])
def fetch_places(city_id):
    """fetch places for a state"""
    places = []
    for city in storage.all('City').values():
        if city.to_dict().get('id') == city_id:
            for place in city.places:
                places.append(place.to_dict())
    if not places:
        abort(404)
    return jsonify(places)


@app_views.route('/cities/<city_id>/places',
                 strict_slashes=False, methods=['POST'])
def post_place(city_id):
    """function to post place"""
    city = storage.get("City", city_id)
    if not state:
        abort(404)
    if not request.get_json():
        return jsonify({"error": "Not a JSON"}), 400
    place = request.get_json()
    if not place['name']:
        return jsonify({"error": "Missing name"}), 400
    if not place['user_id']:
        return jsonify({"error": "Mising user_id"}), 400
    newInstance = Place(place)
    newInstance.name = place.get("name")
    newInstance.city_id = city_id
    storage.new(newInstance)
    storage.save()
    return jsonify(newInstance.to_dict()), 201


'''
@app_views.route('/cities/<city_id>', strict_slashes=False, methods=['PUT'])
def put_city(city_id):
    """Function that update city"""
    if not request.get_json():
        return jsonify({"error": "Not a JSON"}), 400
    obj = storage.get("City", city_id)
    if not obj:
        abort(404)
    requestObj = request.get_json()
    obj.name = requestObj["name"]
    obj.save()
    return jsonify(obj.to_dict()), 200


@app_views.route('/cities/<city_id>',
                 strict_slashes=False, methods=['DELETE'])
def delete_city(city_id):
    """Function that delete state"""
    obj = storage.get("City", city_id)
    if not obj:
        abort(404)
    storage.delete(obj)
    storage.save()
    return jsonify({}), 200
'''
