#!/usr/bin/python3

"""Simple Flask server"""
from flask import Flask

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


if __name__ == "__main__":
    app.run(host="0.0.0.0")
