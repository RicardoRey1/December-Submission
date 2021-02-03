import pygame
import sys
from os import path
from sprites import *
from settings import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        pygame.key.set_repeat(500, 100)
        self.load_data()

    # load a pre-exisiting map and graphics for the game.
    def load_data(self):
        game_data = path.dirname(__file__)
        img_folder = path.join(game_data, 'img')# this will be the images for stuff in the game
        self.map_data = [] # we will add the map text to this
        self.player_img = path.join(game_data, 'img')
        self.player_img_w = pygame.image.load(path.join(img_folder, PLAYER_W)).convert_alpha() # loading from img folder
        self.player_img_a = pygame.image.load(path.join(img_folder, PLAYER_A)).convert_alpha()
        self.player_img_s = pygame.image.load(path.join(img_folder, PLAYER_S)).convert_alpha()
        self.player_img_d = pygame.image.load(path.join(img_folder, PLAYER_D)).convert_alpha()
        self.zombie_img = pygame.image.load(path.join(img_folder, ZOMBIE_IMG)).convert_alpha()
        self.bullet_img = pygame.image.load(path.join(img_folder, BULLET_IMG)).convert_alpha()
        # reading the map file
        with open(path.join(game_data, 'map2'), 'rt') as f:
            for line in f:
                # each line in map text file appended to list
                self.map_data.append(line)
        pass

    def spawn(self):
        # initialize all variables and do all the setup for new game, groups for sprites
        self.all_sprites = pygame.sprite.Group()
        self.zombies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.player = Player(self, 50, 50) # player spawn location
        # using enumerate to output both index and value where row = index value and tiles is the string
        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles):
                if tile == "z":
                    Zombie(self, col, row) # spawns a zombie at said column and row in map file
                if tile == 'p':
                    Player(self, col, row) # spawns player at p
                if tile == '1':
                    Wall(self, col, row) # spawns a wall at said column and row in map file


    def run(self):
        # game loop , set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    # allows player to quit game
    def quit(self):
        pygame.quit()
        sys.exit()

    def update(self):
        # update the game loop
        self.all_sprites.update()
        # player hit
        # hits = pygame.sprite.spritecollide(self.player, self.zombies, False, self.player.rect)
        # for hit in hits:
             # self.player.health -= ZOMBIE_DMG
            # hit.velo = vector(0, 0) # have zombie stop after hit
            #  if self.player.health <= 0:
                # self.playing = False # ends game
        # if hits:
            # self.player.position += vector( 20, 0).rotate(-hits[0].deg)


        # zombie hit
        hits = pygame.sprite.groupcollide(self.zombies, self.bullets, False, True)
        for hit in hits:
            hit.health -= BULLET_DMG # take away health when hit by bullet
            hit.velo = vector(0, 0) # when zombie shot, slowed slightly

    def draw_grid(self):
        # drawing the grid of the game
        for x in range(0, WIDTH, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        self.screen.fill(LIGHTGREY)
        self.all_sprites.draw(self.screen)
        # self.draw_grid()

        pygame.display.flip()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit() # quits when esc


    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

# creating the game object
game = Game()
game.show_start_screen()
while True:
    game.spawn()
    game.run()
    game.show_go_screen()
