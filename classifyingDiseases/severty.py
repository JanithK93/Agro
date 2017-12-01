import numpy as np
import pygame
import cv2
from pygame.locals import *


da = 10
ga = 20

ta = da + ga

dp = (da / ta)*100

if(da > ga):
    pygame.mixer.init()
    pygame.mixer.music.load("audioFile/Severity_is_high.wav")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue

elif(da < ga):
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

