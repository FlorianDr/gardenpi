#!/usr/bin/python
import dht
import soil_humidity
import time
import db

while True:
	db.writeSoilHum(soil_humidity.read())
	db.writeHumAndTemp(dht.read())
	time.sleep(10)