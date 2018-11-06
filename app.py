#!/usr/bin/env python3

# https://stackoverflow.com/questions/50728328/python-how-to-show-matplotlib-in-flask

import os
import io
from flask import Response,Flask, render_template


app = Flask(__name__)

@app.route("/map")
def plotpage():
    return render_template('map.html')

@app.route("/")
def homepage():
    return render_template('home.html')


if __name__=="__main__":
    port = port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, port=port)
