import numpy as pckg
import time


currentTime = time.strftime("%H %M")

# Mean value for the growth
# Sample values are given for the testing purposes
averageGrowth = 0.0001
averageHumidity = 80
averageTemp= 24
averageLight = 5

# keep the record about the amount of harmful enviroment changes occur
effectCount = 0
effectCountLight = 0
effectCountHumidity = 0
effectCountTemp = 0

effectCountLightLow = 0
effectCountHumidityLow = 0
effectCountTempLow = 0


# Run the application in give periods
#if currentTime== "08 00" or currentTime== "11 00" or currentTime== "13 00" or currentTime== "16 00" or currentTime== "19 00" or currentTime== "22 00" or currentTime== "01 00" \
       # or currentTime == "04 00" :

if currentTime == currentTime: # just for the testing purposes

    def nonlinear(facts, derive = False):
        if(derive == True):
            return facts*(1-facts)

        else:
            return 1/(1+pckg.exp(-facts))

    # Readings of the sensors are give as input using the array
    # sunlight, temperature, humidity respectively
    facts = pckg.array([ [5.40,28,81],
                       [6.20,29,81.2],
                       [6.59,27.5,81.6],
                       [5.87,28,82] ])

    # Expected output after processing
    # Values taken by monitoring growth of plants

    output = pckg.array([ [0.001029],
                          [0.001531],
                          [0.001100],
                          [0.001011] ])

    pckg.random.seed(1)

    # Initialize weights randomly with a mean of 0
    weight1 = 2*pckg.random.random((3,4))-1
    weight2 = 2*pckg.random.random((4,1))-1

    # feed forward for all layers
    for i in xrange(600000):

        layer0 = facts;
        layer1 = nonlinear(pckg.dot(layer0,weight1))
        layer2 = nonlinear(pckg.dot(layer1,weight2))

        # Size of the error
        # Difference between real value and predicted value
        layer2Error = output-layer2

        if (layer2Error [0]) != 0 and (layer2Error[0]) >= 0.000000000001:
            # Print the amount of error when it satisfies the condition

            if(i % 100000) == 0:
                print "Error" + str(pckg.mean(pckg.abs(layer2Error)))

            layer2Value = layer2Error*nonlinear(layer2,derive = True)

            # How much layer1 values affected to layer2 error with respect to te weights
            layer1Error = layer2Value.dot(weight2.T)


            layer1Value = layer1Error*nonlinear(layer1, derive = True)

            weight2 += layer1.T.dot(layer2Value)
            weight1 += layer0.T.dot(layer1Value)

    print layer2

    # if predicted value is not greater than the average growth keep a record by increasing effectCount
    if layer2[1] < averageGrowth:
        effectCount += 1

        # if effecCount is equal or greater than 3 checks which factor causes the effect to make the warning
        if effectCount >= 3:
            light = facts[0]
            temp = facts[1]
            humi = facts[2]

            # keep records about each factor
            if light > averageLight:
                effectCountLight += 1

                # sound the alarm
                if effectCountLight >= 3:
                    #
                    # Sound the alarm as necessary
                    #
                    effectCountLight=0
                    effectCount=0

            elif light < averageLight:
                effectCountLightLow += 1

                # sound the alarm
                if effectCountLightLow >= 3:
                    #
                    # Sound the alarm as necessary
                    #
                    effectCountLight = 0
                    effectCount = 0

            if  temp > averageTemp:
                effectCountTemp += 1

                if effectCountTemp >= 3:
                    #
                    # Sound the alarm as necessary
                    #
                    effectCountTemp = 0
                    effectCount = 0

            elif temp < averageHumidity:
                effectCountTempLow += 1

                if effectCountTempLow >= 3:
                    #
                    # Sound the alarm as necessary
                    #
                    effectCountTemp = 0
                    effectCount = 0

            if humi > averageHumidity:
                effectCountHumidity += 1

                if effectCountHumidity >= 3:
                    #
                    # Sound the alarm as necessary
                    #
                    effectCountHumidity = 0
                    effectCount = 0

            elif humi < averageHumidity:
                effectCountHumidityLow += 1

                if effectCountHumidityLow >= 3:
                    #
                    # Sound the alarm as necessary
                    #
                    effectCountHumidity = 0
                    effectCount = 0









