#!/usr/bin/python
import dht
import soil_humidity
import time
import db
import valve

while True:
	soil_humid = soil_humidity.read()
	db.writeSoilHum(soil_humid)
	print soil_humid
	
	hum_and_temp = dht.read()
	db.writeHumAndTemp(hum_and_temp)
	print hum_and_temp

	if (soil_humid < 50):
		valve.open(17, 5)
	
	time.sleep(10)