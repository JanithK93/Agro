import time
import numpy as np
#from getLightReadings import getLDR
#from getHumiTempReadings import getTempHumReadings
from growthPrediction.growthANN import growthPredicions
from featureExtraction.AverageSpotArea import averageSpotArea
from classifyingDiseases.severity import severityPred
from featureExtraction.LeafArea import leafArea
from featureExtraction.DiseaseSpotColour import SpotColour
from classifyingDiseases.disease import neural

currentTime = time.strftime("%H %M")
autoRun= False
# Run the application in give periods
#if currentTime== "08 00" or currentTime== "11 00" or currentTime== "13 00" or currentTime== "16 00" \
        #or currentTime == "19 00" or currentTime== "22 00" or currentTime== "01 00" or currentTime == "04 00" :

a=0
if(a==0):
    autoPath ="~/etc/rc.local"
    text="sudo nano /home/pi/Agro/AgroResearch/main.py"
    with open(autoPath,'a+') as bash:
        for line in open(autoPath):
            content=bash.readlines()
            if (text == content):
                autoRun==True
            else:
                content=bash.write("\n")
                content=bash.write(text)

    '''ldrValue = getLDR()
    array=[]
    array = getTempHumReadings() //tocheck
    temp = array[0]
    humidity = array[1]'''

    #call the growthPredicion method in growthANN
    #pass the sensor readings
    ldrValue = 2500
    temp = 27
    humidity =78

    averageSpotArea = 2013757.0
    leafArea = 1631530.0
    SpotColour = np.array([149.73122173334914, 107.11454451521105, 199.46005456416424])

    growthPredicions(ldrValue, temp, humidity)
    severityPred(averageSpotArea,leafArea)
    neural(SpotColour)
