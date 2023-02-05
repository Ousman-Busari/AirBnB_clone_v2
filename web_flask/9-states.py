#!/usr/bin/python3
""" starts a flask web application """

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """ Display a HTML page with a sorted list of states """
    states = storage.all("State")
    return render_template("9-states.html", state=states)

@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """ Displays a HTML page with info of the state whose id is given """
    states = storage.all("State")
    for state in states.values():
        if state.id == id:
            state = state
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown_app(exc):
    """ closes the app session """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
