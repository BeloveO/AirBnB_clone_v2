#!/usr/bin/python3
"""
A script that starts a flask web application
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    Taking the / function
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Taking the /hbnb function
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """
    Replacing _ with space
    """
    return "C {}".format(text).replace('_', ' ')


@app.route('/python/')
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """
    Making routes with default text
    """
    return "Python {}".format(text).replace('_', ' ')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
