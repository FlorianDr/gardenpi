#!/usr/bin/python
import Adafruit_DHT

sensor = Adafruit_DHT.AM2302
pin = 4

def read:
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        if humidity is not None and temperature is not None:
            return (humidity, temperature)
