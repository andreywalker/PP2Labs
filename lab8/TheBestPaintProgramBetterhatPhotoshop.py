import pygame
pygame.init()
screen = pygame.display.set_mode((800,800))
running=True

screen.fill((0,0,0))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if not pygame.mouse.get_pressed()==(0,0,0):
        pygame.draw.circle(screen,(20,88,99),pygame.mouse.get_pos(),10)
    pygame.display.update()
    
    
