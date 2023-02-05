#!/usr/bin/python3
""" starts a flask web application """

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """ Display a HTML page with a sorted list of states
    and the cities under them, also sorted"""
    states = storage.all("State")
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown_app(exc):
    """ closes the app session """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
