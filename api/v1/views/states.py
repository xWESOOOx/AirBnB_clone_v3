#!/usr/bin/python3
"""
Create a new view for State objects - handles all default RESTful API actions.
"""

# Import necessary modules
from flask import abort, jsonify, request
from models.state import State
from api.v1.views import app_views
from models import storage

# Route for retrieving all State objects
@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_all_states():
    """
    Retrieves the list of all State objects.
    """
    # Get all State objects from the storage
    states = storage.all(State).values()
    # Convert objects to dictionaries and jsonify the list
    state_list = [state.to_dict() for state in states]
    return jsonify(state_list)

# Route for retrieving a specific State object by ID
@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def get_state(state_id):
    """
    Retrieves a State object.
    """
    # Get the State object with the given ID from the storage
    state = storage.get(State, state_id)
    if state:
        # Return the State object in JSON format
        return jsonify(state.to_dict())
    else:
        # Return 404 error if the State object is not found
        abort(404)

# Route for deleting a specific State object by ID
@app_views.route('/states/<state_id>', methods=['DELETE'])
def delete_state(state_id):
    """
    Deletes a State object.
    """
    # Get the State object with the given ID from the storage
    state = storage.get(State, state_id)
    if state:
        # Delete the State object from the storage and save changes
        storage.delete(state)
        storage.save()
        # Return an empty JSON with 200 status code
        return jsonify({}), 200
    else:
        # Return 404 error if the State object is not found
        abort(404)

# Route for creating a new State object
@app_views.route('/states', methods=['POST'], strict_slashes=False)
def create_state():
    """
    Creates a State object.

