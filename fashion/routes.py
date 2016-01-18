from flask import send_file, Response
import json
import os
from random import randint
from requests import codes

from fashion.database import get_fashion_items
import fashion.images as IMAGES


def validate(page):
    value = int(page)
    if value <= 0:
        raise ValueError
    return value


def create_routes(app):
    """
    Create routes for fashion flask app
    """
    @app.route('/fashion', methods=["GET"])
    @app.route('/fashion/<page>', methods=["GET"])
    def get_fashion_tips(page=1):
        """
        Gets a list of fashion items
        """
        try:
            # validates the page
            validated_page = validate(page)
            # gets the list of fashion items for the page
            rows = get_fashion_items(validated_page, 20)
            #converts rows to fashion items
            fashion_items = convert_to_fashion_item(rows)
            # randomizes the page of items
            random_list = randomize_list(fashion_items)
        except ValueError:
            return "BAD REQUEST", codes.BAD_REQUEST

        resp = Response(json.dumps(random_list), status=codes.ok, mimetype='application/json')

        return resp
    
    @app.route('/fashion/image/<image_name>', methods=["GET"])
    def get_image(image_name):
        """
        Gets an image for a fashion item
        """
        # gets the path of the image in the images folder
        image_path = os.path.join(os.path.dirname(IMAGES.__file__), image_name)
        # verifies that the image exists
        if not os.path.isfile(image_path):
            return None, codes.not_found
        # sends the image
        return send_file(image_path), codes.ok


def convert_to_fashion_item(rows):
    """
    Converts row items to a fashion item dictionaries
    """
    fashion_items = []
    for row in rows:
        fashion_items.append({
            "title": row[0],
            "blurb": max_word_count(row[1], 32),
            "author": row[2],
            "thumbnail_url": row[3],
            "details_url": row[4],
    })
    return fashion_items


def max_word_count(sentence, max_count):
    """
    Returns a sentence with at most max_count words
    """
    indexes = [i for i, char in enumerate(sentence) if char == " "]
    if len(indexes) >= max_count:
        return sentence[:indexes[max_count-1]]
    return sentence


def randomize_list(items):
    """
    Randomizes the list
    """
    random_list = []
    while items:
        random_list.append(items.pop(randint(0, len(items) - 1)))
    return random_list
