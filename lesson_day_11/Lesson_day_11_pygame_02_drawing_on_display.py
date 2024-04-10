import pygame

#Initialize Pygame
pygame.init()

#Creagte a display surface and set its caption
WINDOW_WIDTH=600
WINDOW_HEIGTH=600
display_surface=pygame.display.set_mode((WINDOW_WIDTH , WINDOW_HEIGTH))
pygame.display.set_caption("Drawing Objects")

#
BLACK=(0, 0, 0)
WHITE=(255, 255, 255)
RED=(255, 0, 0)
GREEN=(0, 255, 0)
BLUE=(0, 0, 255)
YELLOW=(255, 255, 0)
CYAN=(0, 255, 255)
MAGNETA=(255, 0, 255)

#G
display_surface.fill(BLUE)

#
#
pygame.draw.line(display_surface, RED,( 0,0), (100,100),5)
pygame.draw.line(display_surface,GREEN, (100,100), (200,300),1)

#
pygame.draw.circle(display_surface, WHITE,(WINDOW_WIDTH // 2, WINDOW_HEIGTH //2,),200, 6)
pygame.draw.circle(display_surface, YELLOW,(WINDOW_WIDTH // 2, WINDOW_HEIGTH //2,),195, 0
)

#
pygame.draw.rect(display_surface , CYAN,(500, 0 , 0, 100))
pygame.draw.rect(display_surface , MAGNETA,(500, 100 , 50, 100))

#
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

#
    pygame.display.update()

#End the game
pygame.quit()
