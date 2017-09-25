import numpy as pckg
import time
import pygame

#from ..growthPrediction import play_audio as play

def growthPredicions (ldrValue, temp, humidity):

    # assign parameter values
    lightReading = ldrValue
    temperatureReading = temp
    humidityReading = humidity

    # Mean value for the growth
    # Sample values are given for the testing purposes
    averageGrowth = 1.29
    averageHumidity = 77
    averageTemp = 24
    averageLight = 1500
    print("growth class")
    # keep the record about the amount of harmful enviroment changes occur
    effectCount = 0
    effectCountLight = 0
    effectCountHumidity = 0
    effectCountTemp = 0

    effectCountLightLow = 0
    effectCountHumidityLow = 0
    effectCountTempLow = 0

    actualGrowthCalculated = 1

    a = 0
    # try:
    if (a == 0):
        def nonlinear(facts, derive = False):
            if(derive == True):
                return facts*(1-facts)

            else:
                return 1/(1+pckg.exp(-facts))

        # Readings of the sensors are give as input using the array
        # sunlight, temperature, humidity respectively
        facts = pckg.array([[lightReading, temperatureReading, humidityReading]])

        # Expected output after processing
        # Values taken by monitoring growth of plants
        output = pckg.array([[actualGrowthCalculated]]).T

        pckg.random.seed(1)

        # Initialize weights randomly with a mean of 0
        weight1 = 2 * pckg.random.random((3, 1)) - 1

        # feed forward for all layers
        for i in range(600000):

            # Assign values to the first layer
            layer0 = facts;
            layer1 = nonlinear(pckg.dot(layer0, weight1))

            # Size of the error
            # Difference between real value and predicted value
            layer1Error = output - layer1

            # Sigmoid's slope at values in layer1
            layer1Value = layer1Error * nonlinear(layer1, True)

            # Update weights using latest output values
            weight1 += pckg.dot(layer0.T, layer1Value)

        print ("Output After Training:")
        print(layer1)








