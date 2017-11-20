import numpy as pckg
import math
import time
import pygame
import os

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
    averageTemp= 24
    averageLight = 1500
    print("hello")
    # keep the record about the amount of harmful enviroment changes occur
    effectCount = 0
    effectCountLight = 0
    effectCountHumidity = 0
    effectCountTemp = 0

    effectCountLightLow = 0
    effectCountHumidityLow = 0
    effectCountTempLow = 0


    actualGrowthCalculated = 1

    a=0
    #try:

def high_light():
    pygame.mixer.init()
    pygame.mixer.music.load("../audioFile/Sun_light_intensity_is_high.wav")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue



