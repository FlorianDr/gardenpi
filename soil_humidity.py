#!/usr/bin/env python
import time
import RPi.GPIO as GPIO, time, os

DEBUG = 1
GPIO.setmode(GPIO.BCM)

# read SPI data from MCP3008 chip, 8 possible adc's (0 thru 7)
def readadc(adcnum, clockpin, mosipin, misopin, cspin):
	if ((adcnum > 7) or (adcnum < 0)):
		return -1
	GPIO.output(cspin, True)

	GPIO.output(clockpin, False)  # start clock low
	GPIO.output(cspin, False)     # bring CS low

	commandout = adcnum
	commandout |= 0x18  # start bit + single-ended bit
	commandout <<= 3    # we only need to send 5 bits here
	for i in range(5):
		if (commandout & 0x80):
			GPIO.output(mosipin, True)
		else:
   			GPIO.output(mosipin, False)
                commandout <<= 1
                GPIO.output(clockpin, True)
                GPIO.output(clockpin, False)

	adcout = 0
	# read in one empty bit, one null bit and 10 ADC bits
	for i in range(12):
		GPIO.output(clockpin, True)
		GPIO.output(clockpin, False)
		adcout <<= 1
		if (GPIO.input(misopin)):
			adcout |= 0x1

	GPIO.output(cspin, True)

	adcout /= 2       # first bit is 'null' so drop it
	return adcout

def convert_soil_humidity_linear(input):
	return (input * 1.0 / 700) * 100	

if __name__=='__main__':

	try:
		# change these as desired
		SPICLK = 18
		SPIMISO = 23
		SPIMOSI = 24
		SPICS = 25

		# set up the SPI interface pins 
		GPIO.setup(SPICLK, GPIO.OUT)
		GPIO.setup(SPIMISO, GPIO.IN)
		GPIO.setup(SPIMOSI, GPIO.OUT)
		GPIO.setup(SPICS, GPIO.OUT)

		# Note that bitbanging SPI is incredibly slow on the Pi as its not
		# a RTOS - reading the ADC takes about 30 ms (~30 samples per second)
		# which is awful for a microcontroller but better-than-nothing for Linux
		while True:
			ret = readadc(0, SPICLK, SPIMOSI, SPIMISO, SPICS)
			print ret," ",convert_soil_humidity_linear(ret),"\t"
			time.sleep(1) 
       
	except KeyboardInterrupt:
		pass

	GPIO.cleanup()
