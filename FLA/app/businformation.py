from flask import render_template,request, Response
from app import app
import requests
#from flask_sqlalchemy import SQLAlchemy
#from sqlalchemy import create_engine
#from app.businformation import Businformation
import os
import datetime
import json
import sqlite3

class Businformation:

    info = {}
    con =''
    arrivaltable = []
    def __init__(self):
        v= 999
        self.arrivaltable =[]
    
    def update(self):
        dbpath = os.path.join(os.getcwd(),'/database/tfl.db')
        dbpath = 'database/tfl.db'
        con = sqlite3.connect(dbpath)
        cur = con

        data = requests.get('https://api.tfl.gov.uk/StopPoint/490009333W/arrivals')
        info = data.json()
        cur = con.cursor()
        if (len(info)>0):
            values_to_insert =[]
            for businformation in info:
                now = datetime.datetime.now()
                currenttime = now.strftime('%d-%m-%Y-%H:%M:%S') + ('-%02d' % (now.microsecond / 10000))
                stringify = json.dumps(businformation )
                values_to_insert.append((stringify,currenttime))
            cur.executemany("INSERT INTO tfl (data,timestamp) VALUES (?, ?)", values_to_insert)
            con.commit()
        else:
            print("no data")


        #for bustime in info:
    def gettable(self):
        data = self.settable()
        return data

    def settable(self):
        tabledata=[]
        count =0
        dbpath = os.path.join(os.getcwd(),'/database/tfl.db')
        dbpath = 'database/tfl.db'
        con = sqlite3.connect(dbpath)
        cur = con
        info = cur.execute("SELECT * from tfl ORDER BY tfl_id DESC")
        text = list(info)

        if (info):
            for row in text:
                arrivalinfo = {}
                jsondata =  json.loads(row[1] )
                arrivalinfo['tfl_id'] = row[0]
                arrivalinfo['timestamp'] = row[2]
                arrivalinfo['vehicleId'] = jsondata['vehicleId']
                arrivalinfo['towards'] = jsondata['towards']
                arrivalinfo['bearing']= jsondata['bearing']
                arrivalinfo['currentLocation'] = jsondata['currentLocation']
                arrivalinfo['destinationName'] = jsondata['destinationName']
                arrivalinfo['destinationNaptanId'] = jsondata['destinationNaptanId']
                arrivalinfo['direction'] = jsondata['direction']
                arrivalinfo['expectedArrival'] = jsondata['expectedArrival']
                arrivalinfo['id'] = jsondata['id']
                arrivalinfo['lineId'] = jsondata['lineId']
                arrivalinfo['lineName'] = jsondata['lineName']
                arrivalinfo['modeName'] = jsondata['modeName']
                arrivalinfo['naptanId'] = jsondata['naptanId']
                arrivalinfo['operationType'] = jsondata['operationType']
                arrivalinfo['platformName'] = jsondata['platformName']
                arrivalinfo['stationName'] = jsondata['stationName']
                arrivalinfo['timeToLive'] = jsondata['timeToLive']
                arrivalinfo['timing_countdownServerAdjustment'] = jsondata['timing']['countdownServerAdjustment']
                arrivalinfo['timing_insert'] = jsondata['timing']['insert']
                arrivalinfo['timing_read'] = jsondata['timing']['read']
                arrivalinfo['timing_received'] = jsondata['timing']['received']
                arrivalinfo['timing_sent'] = jsondata['timing']['sent']
                arrivalinfo['timing_source'] = jsondata['timing']['source']
                tabledata.append(arrivalinfo)
            return tabledata

        else:
            print("nothing in table")


        return self.info



    def clear(self):
        dbpath = os.path.join(os.getcwd(),'/database/tfl.db')
        dbpath = 'database/tfl.db'
        con = sqlite3.connect(dbpath)
        cur = con
        info = cur.execute("DELETE from tfl")
        con.commit()

    #setters
    def setbearing(bear):
        self.info.bearing = bear

    def setcurrentLocation(loc):
        self.info.currentLocation = loc

    def setdestinationName(destName):
        self.info.destinationName = destName

    def setdestinationNaptanId(id):
        self.info.destinationNaptanId = id

    def setdirection(dir):
        self.info.direction = dir

    def setexpectedArrival(arr):
        self.info.expectedArrival = arr

    def setid(id):
        self.info.id = id

    def setlineId(lineId):
        self.info.lineId = lineId

    def setlineName(lineName):
        self.info.lineName = lineName

    def setmodeName(modeName):
        self.info.modeName = modeName

    def setnaptanId(napId):
        self.info.naptanId = napId

    def setoperationType(optype):
        self.info.operationType = optype

    def setplatformName(setplat):
        self.info.platformName = setplat

    def setstationName(statname):
        self.info.stationName = statname

    def settimeToLive(ttliv):
        self.info.timeToLive = ttliv

    def settiming_countdownServerAdjustment(countadj):
        self.info.timing_countdownServerAdjustment = countadj

    def settiming_insert(settimeins):
        self.info.timing_insert = settimeins

    def settiming_read(read):
        self.info.timing_read = read

    def settiming_received(setre):
        self.info.timing_received = setre

    def settiming_sent(setse):
        self.info.timing_sent = setse

    def settiming_source(settimesrc):
        self.info.timing_source = settimesrc

    #getters
    def getbearing():
        return self.info.bearing

    def getcurrentLocation():
        return self.info.currentLocation

    def getdestinationName():

        return self.info.destinationName
    def getdestinationNaptanId():
        return self.info.destinationNaptanId

    def getdirection():
        return self.info.direction

    def getexpectedArrival():
        return self.info.expectedArrival

    def getid():
        return self.info.id

    def getlineId():
        return self.info.lineId

    def getlineName():
        return self.info.lineName

    def getmodeName():
        return self.info.modeName

    def getnaptanId():
        return self.info.naptanId

    def getoperationType():
        return self.info.operationType

    def getplatformName():
        return self.info.platformName

    def getstationName():
        return self.info.stationName

    def gettimeToLive():
        return self.info.timeToLive

    def gettiming_countdownServerAdjustment():
        return self.info.timing_countdownServerAdjustment

    def gettiming_insert():
        return self.info.timing_insert

    def gettiming_read():
        return self.info.timing_read

    def gettiming_received():
        return self.info.timing_received

    def gettiming_sent():
        return self.info.timing_sent

    def gettiming_source():
        return self.info.timing_source
    def getinformation():
        return self.info
