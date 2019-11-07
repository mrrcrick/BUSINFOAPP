from flask import render_template,request, Response
from app import app
import requests
import os
import datetime
import json
import sqlite3

class Businformation:

    info = {}
    con =''
    arrivaltable = []
    def __init__(self):
        self.arrivaltable =[]

    def log_error(self,e):
        f=open("logs/log.txt", "a+")
        now = datetime.datetime.now()
        currenttime = now.strftime('%d-%m-%Y-%H:%M:%S') + ('-%02d' % (now.microsecond / 10000))
        f.write('\n')
        f.write(str(currenttime)+' '+str(e))
        #f.write(e)
        f.close()

    def update(self):
        try:
            dbpath = 'database/tfl.db'
            con = sqlite3.connect(dbpath)
            cur = con
        except sqlite3.Error as e:
            print("Error could not connect")
            log_error(e)
            return "error"

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
            try:
                cur.executemany("INSERT INTO tfl (data,timestamp) VALUES (?, ?)", values_to_insert)
                con.commit()
            except sqlite3.Error as e:
                self.log_error(e)

        else:
            print("no data")


    #for bustime in info:
    def gettable(self):
        data = self.settable()
        return data
   # load database into class object
    def settable(self):
        tabledata=[]
        try:
            dbpath = 'database/tfl.db'
            con = sqlite3.connect(dbpath)
            cur = con
            info = cur.execute("SELECT * from tfl ORDER BY tfl_id DESC")
        except sqlite3.Error as e:
            print("Error database")
            self.log_error(e)
            return "error"
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
                #set human readable arrival time
                arrivetime = arrivalinfo['expectedArrival'].split('T')
                humantime = (arrivetime[1].strip("Z"))
                arrivalinfo['human_time_arriv'] = humantime
                tabledata.append(arrivalinfo)
            self.arrivaltable = tabledata
            return tabledata
        else:
            print("nothing in table")
        return self.info

    def clear(self):
        try:
            dbpath = 'database/tfl.db'
            con = sqlite3.connect(dbpath)
            cur = con
            info = cur.execute("DELETE from tfl")
            con.commit()
        except sqlite3.Error as e:
            print("Error could not connect")
            self.log_error(e)
            return "error"
