import numpy as np
import pygame
import cv2
from pygame.locals import *


diseased_area = 10
green_area = 20



if(diseased_area > green_area):
    pygame.mixer.init()
    pygame.mixer.music.load("audioFile/Severity_is_high.wav")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue

elif(diseased_area  <  green_area):
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

