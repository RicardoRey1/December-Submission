import pygame
from settings import *
vector = pygame.math.Vector2 # this will be used for vectors with the game
# such as calculating the distance between the player and zombie

class Player(pygame.sprite.Sprite): # inherits from sprite class in pygame
    def __init__(self, game, x, y):
        self.position = vector(x, y) # for x and y
        self.groups = game.all_sprites
        self.game = game
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = game.player_img_w
        self.rect = self.image.get_rect()
        self.velocity = vector(0,0)
        self.previous = 0
        self.deg = 0
        self.health = PLAYER_HEALTH

    def move(self, dx=0, dy=0):
        # allow player to change x and y(move) values if wall_collision = false
        if not self.wall_collision(dx,dy):
            self.position.x += dx
            self.position.y += dy

    def wall_collision(self, dx=0, dy=0 ):
        for wall in self.game.walls:
            if wall.x == self.position.x +dx and wall.y == self.position.y +dy:
                return True
        return False


    # movement system using pygame keystroke functions
    def key_pressed(self):
        self.velocity = vector(0, 0)
        keystroke = pygame.key.get_pressed()
        if keystroke[pygame.K_a]:
            self.velocity.x = -PLAYER_SPEED
            self.image = self.game.player_img_a
            self.deg = 180  # set the degrees to 180 when shooting
        if keystroke[pygame.K_d]:
            self.velocity.x = +PLAYER_SPEED
            self.image = self.game.player_img_d
            self.deg = 0
        if keystroke[pygame.K_s]:
            self.velocity.y = +PLAYER_SPEED
            self.image = self.game.player_img_s
            self.deg = 270
        if keystroke[pygame.K_w]:
            self.velocity.y = -PLAYER_SPEED
            self.image = self.game.player_img_w
            self.deg = 90
        if keystroke[pygame.K_SPACE]:
            now = pygame.time.get_ticks()
            if now - self.previous > BULLET_ROF:  # if its been long enough since last shot then able to shoot
                self.previous = now
                dir = vector(1, 0).rotate(-self.deg) #
                position = self.position + OFFSET.rotate(-self.deg) # position is the player position + offset
                Bullet(self.game, position, dir)


    def update(self):
        self.key_pressed()
        self.position += self.velocity * self.game.dt
        self.rect.topleft = self.position
        if pygame.sprite.spritecollideany(self, self.game.walls):
            self.position -= self.velocity * self.game.dt
            self.rect.topleft = self.position

class Zombie(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.zombies
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = game.zombie_img
        self.game = game
        self.x = x
        self.y = y
        self.health = ZOMBIE_HEALTH
        self.acc = vector(0, 0)
        self.velo = vector(0, 0)
        self.position = vector(x, y) * TILESIZE
        self.rect = self.image.get_rect()
        self.rect.center = self.position
        self.deg = 0

    def z_health(self):
        # colour of health bar changes depending on %
        if self.health > 70:
            bar = GREEN
        elif self.health > 40:
            bar = YELLOW
        else:
            bar = RED
        width = int(self.rect.width * self.health / 100) # width of healthbar = width of sprite x health as %
        self.health_bar = pygame.Rect(0, 0, width, 7) # healthbar rectangle setup
        if self.health < 100:
            pygame.draw.rect(self.image, bar, self.health_bar)


    def update(self):
        self.deg = (self.game.player.position - self.position).angle_to(vector(1,0)) # this calculates the angle from the zombie to player
        self.image = pygame.transform.rotate(self.game.zombie_img, self.deg) # rotates the zombie to the angle
        self.rect = self.image.get_rect()
        self.rect.center = self.position # applies postition to zombie angle
        # motion
        self.acc = vector(ZOMBIE_SPEED, 0).rotate(-self.deg) # runs foward direction at the
        self.acc += self.velo *-1 # some friction against acceleration
        self.velo += self.acc * self.game.dt # velocity = accelation * time
        self.position += self.velo * self.game.dt + 0.5 * self.acc * self.game.dt **2 # equation:s = ut + 0.5at^2
        self.rect.center = self.position
        if self.health <=0:
            self.kill()

class Wall(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.x = x
        self.y = y
        self.groups = game.all_sprites, game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(DARKGREY)
        self.rect = self.image.get_rect()
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Bullet(pygame.sprite.Sprite):
    def __init__(self, game, position, dir):
        self.groups = game.all_sprites, game.bullets
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = game.bullet_img
        self.game = game
        self.rect = self.image.get_rect()
        self.position = position# vector as player doesnt travel bullet speed when shooting
        self.rect.center = position
        self.velo = dir * BULLET_SPEED
        self.spawn_time = pygame.time.get_ticks() # so we know when to delete bullet


    # updates for bullet class: position from velo and rect
    def update(self):
        self.position += self.velo * self.game.dt
        self.rect.center = self.position
        if pygame.sprite.spritecollideany(self,  self.game.walls):
            self.kill() # if hits anything then gets deleted
        if pygame.time.get_ticks() - self.spawn_time > TTLBULLET:
            self.kill() # if greater than ttl of bullet then delete
