#!/usr/bin/python
import sys
import dhtreader

# Choose our device
DHT11 = 11
DHT22 = 22
AM2302 = 22

dhtreader.init()
dev_type = AMT2302

# Choose our pin
dhtpin = 4

while True:
    t, h = dhtreader.read(dev_type, dhtpin)
    if t and h:
        print("Temp = {0} *C, Hum = {1} %".format(t, h))
    else:
        print("Failed to read from sensor, maybe try again?")
    time.sleep(2)
