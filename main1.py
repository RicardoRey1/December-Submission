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
playerX = 360
playerY = 300
# moving on x or y
playerX_change = 0
playerY_change = 0


# drawing player image on screen
def player(x, y):
    screen.blit(playerAvatar, (x, y))


# Loop to make sure window doesn't close
running = True
while running:

    screen.fill((128, 128, 128))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # checking keystroke
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                playerY_change = -0.5
            if event.key == pygame.K_a:
                playerX_change = -0.5
            if event.key == pygame.K_s:
                playerY_change = 0.5
            if event.key == pygame.K_d:
                playerX_change = 0.5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                playerX_change = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                playerY_change = 0

    # adding the change to the x value and the y
    playerY += playerY_change
    playerX += playerX_change
    player(playerX, playerY)
    pygame.display.update()
