import pygame

pygame.init()
pygame.mixer.init()

# Create the window
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("BOOM!")

# Load explosion sound
explosion = pygame.mixer.Sound("explosion.wav")

running = True

while running:
    for event in pygame.event.get():

        # Close the window with the mouse X
        if event.type == pygame.QUIT:
            running = False

        # Play explosion whenever a key is pressed
        elif event.type == pygame.KEYDOWN:
            explosion.play()

pygame.quit()