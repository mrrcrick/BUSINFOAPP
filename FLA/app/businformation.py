class Businformation:
    info = {}
    def __init__(self,info):
        self.info.bearing = info.bearing
        self.info.currentLocation = info.currentLocation
        self.info.destinationName = info.destinationName
        self.info.destinationNaptanId = info.destinationNaptanId
        self.info.direction = info.direction
        self.info.expectedArrival = info.expectedArrival
        self.info.id = info.id
        self.info.lineId = info.lineId
        self.info.lineName = info.lineName
        self.info.modeName = info.modeName
        self.info.naptanId = info.naptanId
        self.info.operationType = info.operationType
        self.info.platformName = info.platformName
        self.info.stationName = info.stationName
        self.info.timeToLive = info.timeToLive
        self.info.timeing_countdownServerAdjustment = info.timeing_countdownServerAdjustment
        self.info.timing_insert = info.timing_insert
        self.info.timing_read = info.timing_read
        self.info.timing_received = info.timing_received
        self.info.timing_sent = info.timing_sent
        self.info.timing_source = info.timing_source
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

    def settimeing_countdownServerAdjustment(countadj):
        self.info.timeing_countdownServerAdjustment = countadj

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

    def gettimeing_countdownServerAdjustment():
        return self.info.timeing_countdownServerAdjustment

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
