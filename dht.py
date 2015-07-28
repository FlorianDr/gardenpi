#!/usr/bin/python
import sys
import dhtreader
import db
import time

# Choose our device
DHT11 = 11
DHT22 = 22
AM2302 = 22

dhtreader.init()
devType = AM2302

# Choose our pin
dhtpin = 4

while True:
    t, h = dhtreader.read(devType, dhtpin)
    if t and h:
        db.writeHumAndTemp(t, h)
        print("Temp = {0} *C, Hum = {1} %".format(t, h))
    else:
        print("Failed to read from sensor")
    time.sleep(3)
