import pygame  

#
pygame.init()

#
WINDOW_WIDTH=600
WINDOW_HEIGTH=300
display_surface=pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGTH))
pygame.display.set_caption("Blitting Images!")

#Create images ... returns a Surface object with the image drawon on it.
#
dragon_left_image=pygame.image.load("images/dragon_right.png")
dragon_left_rect=dragon_left_image.get_rect()
dragon_left_rect.topleft=(0, 0)

dragon_right_image=pygame.image.load("images/dragon_right.png")
dragon_right_rect=dragon_right_image.get_rect()
dragon_right_rect.topright=(WINDOW_WIDTH,0)

#The maingame loop
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

            #
    display_surface.blit(dragon_left_image, dragon_left_rect)
    display_surface.blit(dragon_right_image, dragon_right_rect)

    pygame.draw.line(display_surface,(255, 255, 255),(0, 75),(WINDOW_WIDTH,75),4)

    #Update the display
    pygame.display.update()

        #End the game
pygame.quit()
    