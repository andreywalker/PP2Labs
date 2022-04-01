import pygame
pygame.init()
screen = pygame.display.set_mode((800,800))

pygame.mixer.init()
pygame.mixer.music.load("crossoff.mp3")
pygame.mixer.music.play(0)

running=True
while running:
    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running = False