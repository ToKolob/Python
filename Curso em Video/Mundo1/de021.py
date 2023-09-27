import pygame

pygame.init()
pygame.mixer.init()

# Caminho para o arquivo MP3 que você deseja reproduzir
caminho_mp3 = "C:/Users/Pichau/Desktop/Tia Fatima Histórias/FormatFactoryPart1.mp3"

try:
    pygame.mixer.music.load(caminho_mp3)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        continue

except pygame.error as e:
    print("Erro ao reproduzir o arquivo MP3:", e)

pygame.quit()
