import time

from getLightReadings import getLDR
from getHumiTempReadings import getTempHumReadings
from growthPrediction.growthANN import growthPredicions
#from AgroResearch.growthPrediction.growth import growthPredicion

currentTime = time.strftime("%H %M")

# Run the application in give periods
if currentTime== "08 00" or currentTime== "11 00" or currentTime== "13 00" or currentTime== "16 00" \
        or currentTime == "19 00" or currentTime== "22 00" or currentTime== "01 00" or currentTime == "04 00" :

    '''ldrValue = getLDR()
    array=[]
    array = getTempHumReadings()
    temp = array[0]
    humidity = array[1]'''

    #call the growthPredicion method in growthANN
    #pass the sensor readings
'''ldrValue = 1558
temp = 27
humidity =78'''
ldrValue = getLDR()
array=[]
array = getTempHumReadings()
temp = array[0]
humidity = array[1]
growthPredicions(ldrValue, temp, humidity)


