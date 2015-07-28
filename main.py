#!/usr/bin/python
import dht
import soil_humidity
import time
import db
import valve

while True:
	soil_humid = soil_humidity.read()
	db.writeSoilHum(soil_humid)
	db.writeHumAndTemp(dht.read())
	if (soil_humid < 50)
		valve.open(17, 5)
	time.sleep(10)