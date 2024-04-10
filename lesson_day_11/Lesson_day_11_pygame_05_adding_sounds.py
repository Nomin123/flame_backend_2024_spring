import pygame  

#
pygame.init()

#
WINDOW_WIDTH=600
WINDOW_HEIGTH=300
display_surface=pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGTH))
pygame.display.set_caption("Adding Sounds")

#Load sound effects
sound_1=pygame.mixer.Sound('audios/sound_1.wav')
sound_2=pygame.mixer.Sound('audios/sound_2.wav')

#Play the sound effect
sound_1.play()
pygame.time.delay(2000)
sound_2.play()
pygame.time.delay(2000)

#Change the volume of sound effect
sound_2.set_volume(.1)
sound_2.play()

#Load background music
pygame.mixer.music.load('audios/music.wav')

#Play the stop the music
pygame.mixer.music.play(-1, 0, 0)
pygame.time.delay(1000)
sound_2.play()
pygame.time.delay(5000)
pygame.mixer.music.stop()

#
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

 #End the game
pygame.quit()       