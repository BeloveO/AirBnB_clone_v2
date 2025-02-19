#!/usr/bin/python3
"""
A script that starts a flask web application
"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def city_state():
    """
    Taking the /cities_by_states function
    """
    states = storage.all(State).values()
    cities = list()
    for state in states:
        for city in state.cities:
            cities.append(city)
    return render_template('8-cities_by_states.html', states=states,
                           state_cities=cities)


@app.teardown_appcontext
def teardown(exception):
    """"
    Teardown
    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
