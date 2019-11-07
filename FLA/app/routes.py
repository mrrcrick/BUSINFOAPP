from flask import render_template,request, Response
from app import app
from flask import jsonify
import requests
from app.businformation import Businformation
import os
import json





@app.route('/')
@app.route('/index')
def index():
    busarrival = Businformation()
    busarrival.update()
    info = (busarrival.gettable())
    return render_template('index.html',information = info)

@app.route('/timestamp')
def timestamp():
    busarrival = Businformation()
    busarrival.update()
    info = (busarrival.gettable())
    return render_template('timestamp.html',information = info)


@app.route('/busarrivals')
def busarrivals():
    times =[]
    #data = requests.get('https://api.tfl.gov.uk/StopPoint/490009333W/arrivals')
    #info = data.json()
    #for bustime in info:
    #    print("----------------- \n")
    #    print(bustime)
    #result = db.engine.execute("INSERT INTO tfl (bearing) VALUES (1);")
    #result = db.engine.execute("SELECT * from tfl")
    #print (result.fetchall())
    busarrival = Businformation()
    #busarrival.update()

    resp = Response(busarrival.gettable())
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.route('/update', methods = ['POST', 'PUT' ,'GET'])
def update():
    try:
        return request.method
    except:
        #print "This didn't work."
        return "not found"

@app.route('/clear')
def clear():
    busarrival = Businformation()
    busarrival.clear()
    return  "clear"
