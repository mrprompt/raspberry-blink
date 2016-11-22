#!/usr/bin/env python
#-*- coding: UTF-8 -*-
import time
import RPi.GPIO as GPIO

pin = 11
delay = 0.5

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)

try:
	while True:
		GPIO.output(pin, GPIO.HIGH)
		time.sleep(delay)

		GPIO.output(pin, GPIO.LOW)
		time.sleep(delay)

except KeyboardInterrupt:
	print("A keyboard interrupt has been noticed")

except Exception, e:
	print("An error or exception has ocurred: " + str(e))

finally:
	GPIO.cleanup()
