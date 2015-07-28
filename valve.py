#!/usr/bin/env python
import time
import RPi.GPIO as GPIO, time, os

def open_for(seconds):
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(17, GPIO.OUT)
	GPIO.output(17, False)
	time.sleep(seconds)
	GPIO.cleanup()