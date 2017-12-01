import numpy as np
import pygame
import cv2
from pygame.locals import *



def severityPred(averageSpotArea,leafArea):

    if(averageSpotArea > leafArea):
        pygame.mixer.init()
        pygame.mixer.music.load("audioFile/Severity_is_high.wav")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue

    elif(averageSpotArea <  leafArea):
        pygame.mixer.init()
        pygame.mixer.music.load("audioFile/Severity_is_low.wav")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue

    else:
        pygame.mixer.init()
        pygame.mixer.music.load("audioFile/Severity_is_moderate.wav")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue

