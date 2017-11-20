import os
import pygame

def func():
    pygame.mixer.init()
    pygame.mixer.music.load(wavpath)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue

wavpath = os.path.abspath('../audioFile/Humidity_is_high.wav')
func()

