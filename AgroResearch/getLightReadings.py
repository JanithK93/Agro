#!/usr/local/bin/python
'''
import RPi.GPIO as GPIO
import time

def getLDR ():
    #GPIO.setmode(GPIO.BOARD)
    GPIO.setmode(GPIO.BCM)


    #define the pin that goes to the circuit
    pin_to_circuit = 25


    def rc_time (pin_to_circuit):
        count = 0

        #Output on the pin for
        GPIO.setup(pin_to_circuit, GPIO.OUT)
        GPIO.output(pin_to_circuit, GPIO.LOW)
        time.sleep(2.0)

        #Change the pin back to input
        GPIO.setup(pin_to_circuit, GPIO.IN)

    try:
        ldr = rc_time(pin_to_circuit)
        return ldr
        #print (ldr)
    except KeyboardInterrupt:
        pass
    finally:
           GPIO.cleanup() '''
