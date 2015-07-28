#!/usr/bin/env python
import time
import RPi.GPIO as GPIO, time, os

def open(seconds, pin):
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, True)
	time.sleep(seconds)
	GPIO.output(pin, False)
	GPIO.cleanup()