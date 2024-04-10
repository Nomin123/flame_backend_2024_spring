import pygame

#initialize pygame
pygame.init()

#
WINDOW_WIDTH=600
WINDOW_HEIGTH=300
display_surface=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGTH))
pygame.display.set_caption("Blitting Images!")

#Define colors
GREEN=(0, 255, 0)
DARKGREEN=(10, 50, 10)
BLACK=(0,0,0)

#See all available system fonts
fonts=pygame.font.get_fonts()
for font in fonts:
    print(font)

    #
system_font=pygame.font.SysFont("calibri",64)
custom_font=pygame.font.Font("images/AttackGraffiti.ttf",32)

#Define Text
system_text=system_font.render("Dragons Rule!", True,GREEN,DARKGREEN)
system_text_rect=system_text.get_rect()
system_text_rect.center=(WINDOW_WIDTH //2 , WINDOW_HEIGTH // 2)

custom_text=custom_font.render("Move the dragon soon!",True,GREEN)
custom_text_rect=custom_text.get_rect()
custom_text_rect.center=(WINDOW_WIDTH //2 , WINDOW_HEIGTH // 2 + 100)

#The main game loop
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    #
    display_surface.blit(system_text, system_text_rect)
    display_surface.blit(custom_text,system_text_rect)

    #
    pygame.display.update()

    #End the game
pygame.quit()
