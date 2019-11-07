from flask import render_template,request, Response
from app import app
from flask import jsonify
import requests
from app.businformation import Businformation
import os
import json

busarrival = Businformation()
# show 5 most recent updates
@app.route('/')
@app.route('/index')
def index():
    updaterr = busarrival.update()
    info = busarrival.gettable()
    if (isinstance(updaterr, str) or isinstance(info , str)):
        return render_template("dbaseerror.html")
    else:
        return render_template('index.html',information = info[0:5])
# show list  of api calls made with with timestamp
@app.route('/timestamp')
def timestamp():
    info = busarrival.gettable()
    if (isinstance(info , str)):
        return render_template("dbaseerror.html")
    else:
        return render_template('timestamp.html',information = info)

# clear the database
@app.route('/clear')
def clear():
    err = busarrival.clear()
    if (isinstance(err,str)):
        return render_template("dbaseerror.html")
    else:
        return  render_template("deleted.html")
