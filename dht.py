#!/usr/bin/python
import dhtreader
import time

# Pin of DHT data and type of sensor
DHT = 4
type = 11

# Get values from sensor
def getDhtData():
    global temperature
    global humidity

    dhtreader.init()
    value = dhtreader.read(type, DHT)

    i = 0
    while True:
        if (value != None):
            temperature = "%.0f" % value[0]
            humidity = "%.0f" % value[1]
            break
        else:
            i += 1

            if (i == 10):
                temperature = 0
                humidity = 0
                break
            time.sleep(0.5)

getDhtData()
print "temperature: " + str(temperature) + "C"
print "humidity: " + str(humidity) + "%"
