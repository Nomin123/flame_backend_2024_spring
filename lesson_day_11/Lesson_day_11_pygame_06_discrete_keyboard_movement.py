import pygame  

#
pygame.init()

#
WINDOW_WIDTH=600
WINDOW_HEIGTH=300
display_surface=pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGTH))
pygame.display.set_caption("Discrete Movement!")

#Set game value
VELOCITY=30

#Load in images
dragon_image=pygame.image.load("images/dragon_right.png")
dragon_rect=dragon_image.get_rect()
dragon_rect.centerx=WINDOW_WIDTH//2
dragon_rect.bottom=WINDOW_HEIGTH

#
running=True
while running:
    for event in pygame.event.get():
        print(event)
        if event.type==pygame.QUIT:
            running=False

            #Check for discrete movement
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                dragon_rect.x-=VELOCITY
            if event.key==pygame.K_RIGHT:
                dragon_rect.x+=VELOCITY
            if event.key==pygame.K_UP:
                dragon_rect.y-=VELOCITY
            if event.key==pygame.K_DOWN:
                dragon_rect.y+=VELOCITY

#Fill the display surface to cover old images
    display_surface.fill((0, 0, 0))

    #Blit (copy) assets to the screen
    display_surface.blit(dragon_image, dragon_rect)

    #Update the display
    pygame.display.update()

 #End the game
pygame.quit() 