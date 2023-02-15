#!/usr/bin/python3
""" starts a flask web application """

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Display all available info in a HTML body"""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    places = storage.all("Place")
    users = storage.all("User").values()
    return render_template("100-hbnb.html", states=states,
                           amenities=amenities, places=places, users=users)


@app.teardown_appcontext
def teardown_app(exc):
    """ closes the app session """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
