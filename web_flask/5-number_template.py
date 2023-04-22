#!/usr/bin/python3

"""Simple Flask server"""
from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

app.url_map.strict_slashes = False


@app.route("/")
def index():
    """Index router"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """HBNB route"""
    return "HBNB"


@app.route("/c/<text>")
def c_route(text):
    """c Route"""
    return f"C {escape(text.replace('_', ' '))}"


@app.route("/python")
def python_no_param():
    """Python route without param"""
    return "Python is cool"


@app.route("/python/<text>")
def python_route(text):
    """Python route with param"""
    return f"Python {escape(text.replace('_', ' '))}"


@app.route("/number/<int:n>")
def number(n):
    """This route is gonna work just if n is integer"""
    return f"{n} is a number"


@app.route("/number_template/<int:n>")
def number_template(n):
    """Number template router"""
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
