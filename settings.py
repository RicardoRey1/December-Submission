import pygame
vector = pygame.math.Vector2
# RGB Colors to be used in the game
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
# healthbar colours
GREEN = (0, 255, 0)
YELLOW = (255, 0 ,0)
RED =  (255, 255, 0)

# game settings
WIDTH = 1024  # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 768  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = "Zombie"

TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

# player
PLAYER_SPEED = 150 # 150 pixels per second
PLAYER_D = 'player_idle_d.png'
PLAYER_W = 'player_idle_w.png'
PLAYER_A = 'player_idle_a.png'
PLAYER_S = 'player_idle_s.png'
PLAYER_HEALTH = 100

# HUD
# def draw_player_health(surf, x, y, percent):
    # if percent < 0:
       # percent = 0
   # BAR_LENGTH = 100
   # BAR_WIDTH = 20
   # fill = percent * BAR_LENGTH
   # fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
   # if percent > 0.7:
       # bar = GREEN
   # elif percent > 0.4:
       # bar = YELLOW
   # else:
       # bar = RED
   # pygame.draw.rect(surf, bar, fill_rect)

# weapons, settings will differ from weapon to weapon
BULLET_IMG = 'bullet.png'
BULLET_DMG = 10
BULLET_SPEED = 500
BULLET_ROF = 400 # rate of fire
TTLBULLET = 1000 # disappears after a second
OFFSET = vector(-5 ,0) # so that bullets position is coming out of gun
# zombie
ZOMBIE_IMG = 'zombie1.png'
ZOMBIE_HEALTH = 100
ZOMBIE_DMG = 20
ZOMBIE_SPEED = 100
# GRAPHICS PENDING
# WALL_IMG
# FLOOR_IMG
