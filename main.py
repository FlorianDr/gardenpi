#!/usr/bin/python
#import dht
import soil_humidity
import time
import Queue
import db
import valve

min_water = (2.0/3.0) * 100
secs_watering = 5
q_size = 5

q = Queue(5)

while True:
	soil_humid = soil_humidity.read()
	db.write_soil_hum(soil_humid)
	print soil_humid

	temp_and_hum = dht.read()
	db.write_temp_and_hum(temp_and_hum)
	print temp_and_hum
	time.sleep(10)

def check_watering(soil_humid) :
	if q.full() :
		q.get()
	q.put(soil_humid)
	soil_avg = sum(q) / q_size
	if (soil_avg < min_water) :
		print "will water now"
		db.write_watering(secs_watering)
		valve.open_for(secs_watering)
