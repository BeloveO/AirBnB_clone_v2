#!/usr/bin/python3
"""
A script that starts a flask web application
"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    """
    Taking the /hbnb_filters function
    """
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    cities = list()
    for state in states:
        for city in state.cities:
            cities.append(city)
    return render_template('10-hbnb_filters.html',
                           states=states, state_cities=cities,
                           amenities=amenities)


@app.teardown_appcontext
def teardown(exception):
    """"
    Teardown
    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
