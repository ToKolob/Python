import pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('C:/Users/Pichau/Desktop/Tia Fatima Histórias/FormatFactoryPart1.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
#a versão atual exige que se coloque o input() antes dp .wait() para tocar