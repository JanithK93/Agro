import numpy as pckg
import math
import time
import pygame
import os

#from growthPrediction import play_audio as play

def growthPredicions (ldrValue, temp, humidity):

    # assign parameter values
    lightReading = ldrValue
    temperatureReading = temp
    humidityReading = humidity

    # Mean value for the growth
    # Sample values are given for the testing purposes
    averageGrowth = 1.2
    averageHumidity = 82
    averageTemp= 24
    averageLight = 2500

    # keep the record about the amount of harmful enviroment changes occur
    effectCount = 0
    effectCountLight = 0
    effectCountHumidity = 0
    effectCountTemp = 0

    effectCountLightLow = 0
    effectCountHumidityLow = 0
    effectCountTempLow = 0

    actualGrowthCalculated = 1

    try:
            def nonlinear(facts, derive = False):
                if(derive == True):
                    return facts*(1-facts)

                else:
                    return 1/(1+pckg.exp(-facts))

            # Readings of the sensors are give as input using the array
            # sunlight, temperature, humidity respectively
            facts = pckg.array([[ lightReading, temperatureReading, humidityReading ]])

                               #[6.20,29,81.2],
                               #[6.59,27.5,81.6],
                               #[5.87,28,82] ])

            # Expected output after processing
            # Values taken by monitoring growth of plants

            output = pckg.array([[ actualGrowthCalculated ]]).T

                                  #[0.001531],
                                  #[0.001100],
                                  #[0.001011] ])

            pckg.random.seed(1)

            # Initialize weights randomly with a mean of 0
            weight1 = 2*pckg.random.random((3,4))-1
            weight2 = 2*pckg.random.random((4,1))-1

            # feed forward for all layers
            for i in range(60000):

                layer0 = facts;
                layer1 = nonlinear(pckg.dot(layer0,weight1))
                layer2 = nonlinear(pckg.dot(layer1,weight2))

                # Size of the error
                # Difference between real value and predicted value
                layer2Error = output-layer2

                if (layer2Error [0]) != 0 and (layer2Error[0]) >= 0.0001:
                    # Print the amount of error when it satisfies the condition

                    '''if(i % 100000) == 0:
                        print ("Error" + str(pckg.mean(pckg.abs(layer2Error))))'''

                    layer2Value = layer2Error*nonlinear(layer2,derive = True)

                    # How much layer1 values affected to layer2 error with respect to te weights
                    layer1Error = layer2Value.dot(weight2.T)


                    layer1Value = layer1Error*nonlinear(layer1, derive = True)

                    # updating weights to reduce the error
                    weight2 += layer1.T.dot(layer2Value)
                    weight1 += layer0.T.dot(layer1Value)

            print "Predicted Value in squre inches:  ", float(layer2[0])
            #print ("Predicted Value:  ", math.ceil(int(chkVal)))

            # if predicted value is not greater than the average growth keep a record by increasing effectCount
            if (layer2[0] < averageGrowth) or (layer2[0] > averageGrowth):
                effectCount += 1

                # if effecCount is equal or greater than 3 checks which factor causes the effect to make the warning
                if effectCount >= 1:
                    light = lightReading
                    temp = temperatureReading
                    humi = humidityReading

                    # keep records about each factor
                    if light > averageLight:
                        effectCountLight += 1

                        # sound the alarm
                        if effectCountLight >= 1:
                            #
                            # Sound the alarm for high intensity
                            #
                            '''abPath = os.path.dirname("D:\Git\Agro\AgroResearch")
                            wavpath = os.path.join(abPath, 'Sun_light_intensity_is_high.wav')
                            pygame.mixer.init()
                            pygame.mixer.music.load(wavpath)
                            pygame.mixer.music.play()
                            while pygame.mixer.music.get_busy() == True:
                                continue'''
                            #high_light()
                            pygame.mixer.init()
                            pygame.mixer.music.load("audioFile/Sun_light_intensity_is_high.wav")
                            pygame.mixer.music.play()
                            while pygame.mixer.music.get_busy() == True:
                                continue
                            effectCountLight=0
                            effectCount=0

                    elif light < averageLight:
                        effectCountLightLow += 1

                        # sound the alarm
                        if effectCountLightLow >= 3:
                            #
                            # Sound the alarm for low intensity
                            #
                            pygame.mixer.init()
                            pygame.mixer.music.load("audioFile/Sun_light_intensity_is_low.wav")
                            pygame.mixer.music.play()
                            while pygame.mixer.music.get_busy() == True:
                                continue

                            effectCountLight = 0
                            effectCount = 0

                    if  temp > averageTemp:
                        effectCountTemp += 1

                        if effectCountTemp >= 1:
                            #
                            # Sound the alarm for high temperature
                            #
                            pygame.mixer.init()
                            pygame.mixer.music.load("audioFile/Temperature_is_high.wav")
                            pygame.mixer.music.play()
                            while pygame.mixer.music.get_busy() == True:
                                continue

                            effectCountTemp = 0
                            effectCount = 0

                    elif temp < averageTemp:
                        effectCountTempLow += 1

                        if effectCountTempLow >= 1:
                            #
                            # Sound the alarm for low temperature
                            #
                            pygame.mixer.init()
                            pygame.mixer.music.load("audioFile/Temperature_is_Low.wav")
                            pygame.mixer.music.play()
                            while pygame.mixer.music.get_busy() == True:
                                continue

                            effectCountTemp = 0
                            effectCount = 0

                    if humi > averageHumidity:
                        effectCountHumidity += 1

                        if effectCountHumidity >= 1:
                            #
                            # Sound the alarm for high humidity
                            #
                            pygame.mixer.init()
                            pygame.mixer.music.load("audioFile/Sun_light_intensity_is_high.wav")
                            pygame.mixer.music.play()
                            while pygame.mixer.music.get_busy() == True:
                                continue

                            effectCountHumidity = 0
                            effectCount = 0

                    elif humi < averageHumidity:
                        effectCountHumidityLow += 1

                        if effectCountHumidityLow >= 1:
                            #
                            # Sound the alarm for lo humidity
                            #
                            pygame.mixer.init()
                            pygame.mixer.music.load("audioFile/Humidity_is_high.wav")
                            pygame.mixer.music.play()
                            while pygame.mixer.music.get_busy() == True:
                                continue

                            effectCountHumidity = 0
                            effectCount = 0

    except:
        '''print ("Error occured in taking readings")
        print ("Sun light :", lightReading)
        print("Humidity :", humidityReading)
        print("Temperature :", temperatureReading)

        #
        # Sound the alarm for high humidity
        #
        pygame.mixer.init()
        pygame.mixer.music.load("../audioFile/Error_sensor_readings.wav")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue'''

def high_light():
    pygame.mixer.init()
    pygame.mixer.music.load("audioFile/Sun_light_intensity_is_high.wav")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue



