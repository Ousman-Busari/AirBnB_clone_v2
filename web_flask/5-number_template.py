#!/usr/bin/python3
""" starts a flask web application """

from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def home():
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    return "HBNB"


@app.route('/c/<text>')
def c(text):
    return "C {}".format(text.replace("_", " "))


@app.route("/python", defaults={"text": "is cool"})
@app.route("/python/<text>")
def python(text):
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>")
def number(n):
    if type(n) == int:
        return "{} is a number".format(n)


@app.route("/number_template/<int:n>")
def number_template(n):
    if type(n) == int:
        return render_template("5-number.html", number=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
