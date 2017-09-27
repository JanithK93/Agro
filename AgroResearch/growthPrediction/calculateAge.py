import datetime
import pygame


pygame.mixer.init()
pygame.mixer.music.load("../audioFile/Humidity_is_high.wav")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue

