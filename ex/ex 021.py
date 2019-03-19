'''
Faça um programa que abra e reproduza o audio de um arquivo mp3
'''

import pygame

pygame.mixer.init()
pygame.mixer_music.load('ex021.mp3')
pygame.mixer_music.play()


while pygame.mixer.music.get_busy():
    pause = int(input('Digite 1 para parar e qualquer outro numero para continuar: '))
    if pause == 1:
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()
input()
