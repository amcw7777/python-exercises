import pygame
import sys
 
pygame.init()
window = pygame.display.set_mode((600,600))
  
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.fill( (0,0,0) ) # black background
    pygame.draw.rect( window, (255,255,255), (250,250,100,100) ) # white square
    pygame.display.update()
