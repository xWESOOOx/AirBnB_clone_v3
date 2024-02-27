#!/usr/bin/python3
'''
Create a new view for Review objects - handles all default RESTful API
'''

# Import necessary modules
from flask import abort, jsonify, request
from models.place import Place
from models.review import Review
from models.user import User
from api.v1.views import app_views
from models import storage


# Route for retrieving all Review objects of a Place
@app_views.route('/places/<place_id>/reviews', methods=['GET'],
                 strict_slashes=False)
def get_reviews_by_place(place_id):
    '''
    Retrieves the list of all Review objects of a Place
    '''
    # Get the Place object with the given ID from the storage
    place = storage.get(Place, place_id)
    if not place:
        # Return 404 error if the Place object is not found
        abort(404)

    # Get all Review objects of the Place and convert them to dictionaries
    reviews = [review.to_dict() for review in place.reviews]
    return jsonify(reviews)


# Route for retrieving a specific Review object by ID
@app_views.route('/reviews/<review_id>', methods=['GET'],
                 strict_slashes=False)
def get_review(review_id):
    '''
    Retrieves a Review object
    '''
    # Get the Review object with the given ID from the storage
    review = storage.get(Review, review_id)
    if review:
        # Return the Review object in JSON format
        return jsonify(review.to_dict())
    else:
        # Return 404 error if the Review object is not found

