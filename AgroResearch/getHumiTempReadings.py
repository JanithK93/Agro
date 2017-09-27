'''import RPi.GPIO as GPIO
import dht11
import time
import datetime

def getTempHumReadings():

	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	#GPIO.cleanup()

	# read data using pin 4
	instance = dht11.DHT11(pin=4)

	result = instance.read()
	if result.is_valid():
		arrayReadings = [result.temperature, result.humidity]
		return  arrayReadings
		GPIO.cleanup()
	else:
		print("invalid")'''

