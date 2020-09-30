import pygame

pygame.init()
# creating the game window
screen = pygame.display.set_mode((800, 600))

# Creating the title and logo of game
icon = pygame.image.load('zombie.png')
pygame.display.set_icon(icon)
pygame.display.set_caption("Zombie Slayer")

# player
playerAvatar = pygame.image.load('player.png')
playerX = 400
playerY = 300


# drawing player image on screen
def player():
    screen.blit(playerAvatar, (playerX, playerY))


# Loop to make sure window doesn't close
running = True
while running:

    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player()
    pygame.display.update()
