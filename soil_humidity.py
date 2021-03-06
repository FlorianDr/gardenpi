#!/usr/bin/env python
import RPi.GPIO as GPIO, time, os


low_bound = 300.0
high_bound = 680.0

# read SPI data from MCP3008 chip, 8 possible adc's (0 thru 7)
def readadc(adcnum, clockpin, mosipin, misopin, cspin):
	GPIO.setmode(GPIO.BCM)
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
	if input < low_bound :
		return 0
	elif input > high_bound :
		return 100
	else :
		return (((input * 1.0) - low_bound) / high_bound) * 100

def read_from_sensor():
	GPIO.setmode(GPIO.BCM)

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

	ret = readadc(0, SPICLK, SPIMOSI, SPIMISO, SPICS)

	GPIO.cleanup()
	return ret

def read():
	return convert_soil_humidity_linear(read_from_sensor());

def read_live():
	while True:
		print read_from_sensor()
		time.sleep(2)
