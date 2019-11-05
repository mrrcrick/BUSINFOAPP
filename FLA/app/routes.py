from flask import render_template,request, Response
from app import app
from flask import jsonify
import requests
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from app.businformation import Businformation
import os

db = SQLAlchemy(app)



@app.route('/')
@app.route('/index')
def index():
    data = requests.get('https://api.tfl.gov.uk/StopPoint/490009333W/arrivals')
    resp = Response(data)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.route('/busarrivals')
def busarrivals():
    times =[]
    data = requests.get('https://api.tfl.gov.uk/StopPoint/490009333W/arrivals')
    info = data.json()
    for bustime in info:
        print("----------------- \n")
        print(bustime)
    result = db.engine.execute("INSERT INTO tfl (bearing) VALUES (1);")
    result = db.engine.execute("SELECT * from tfl")
    #print (result.fetchall())
    resp = Response(data)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.route('/update', methods = ['POST', 'PUT' ,'GET'])
def update():
    try:
        return request.method
    except:
        #print "This didn't work."
        return "not found"
