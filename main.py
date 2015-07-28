#!/usr/bin/python
import dht
import soil_humidity
import time
import db
import valve

while True:
	soil_humid = soil_humidity.read()
	db.write_soil_hum(soil_humid)
	print soil_humid

	temp_and_hum = dht.read()
	db.write_temp_and_hum(temp_and_hum)
	print temp_and_hum

	if (soil_humid < 50):
		print "should water now"
		valve.open_for(5)

	time.sleep(10)
