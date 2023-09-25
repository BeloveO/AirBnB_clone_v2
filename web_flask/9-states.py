#!/usr/bin/python3
"""
A script that starts a flask web application
"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """
    Taking the /states function
    """
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """
    Taking the /states/<id> function
    """
    states = storage.all(State).values()
    for state in states:
        if id == state.id:
            return render_template('9-states.html',
                                   state=state, state_cities=state.cities)
    return render_template('9-states.html', not_found=True)


@app.teardown_appcontext
def teardown(exception):
    """"
    Teardown
    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
