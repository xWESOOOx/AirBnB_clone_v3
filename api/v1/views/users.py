#!/usr/bin/python3
'''
Create a new view for User objects - handles all default RESTful API actions
'''

# Import necessary modules
from flask import abort, jsonify, request
# Import the User model
from models.user import User
from api.v1.views import app_views
from models import storage


# Route for retrieving all User objects
@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_all_users():
    '''
    retrieves the list of all User objects
    '''
    # Get all User objects from the storage and convert them to dictionaries
    users = storage.all(User).values()
    return jsonify([user.to_dict() for user in users])


# Route for retrieving a specific User object by ID
@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    '''
    Retrieves a User object
    '''
    # Get the User object with the given ID from the storage
    user = storage.get(User, user_id)
    if user:
        # Return the User object in JSON format
        return jsonify(user.to_dict())
    else:
        # Return 404 error if the User object is not found
        abort(404)


# Route for deleting a specific User object by ID
@app_views.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    '''
    Deletes a User object
    '''
    # Get the User object with the given ID from the storage
    user = storage.get(User, user_id)
    if user:
        # Delete the User object from the storage and save changes
        storage.delete(user)
        storage.save()
        # Return an empty JSON with 200 status code
        return jsonify({}), 200

