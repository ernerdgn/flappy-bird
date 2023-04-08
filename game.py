import pygame
import random

pygame.init()

# MAP
WIDTH = 288
HEIGHT = 512

# COLOR(S)
WHITE = (255,255,255)

# SPRITES
background_image = pygame.image.load("images/background.png")
bird_image = pygame.image.load("images/bird.png")
pipe_image = pygame.image.load("images/pipe.png")
reversed_pipe_image = pygame.transform.flip(pipe_image, False, True)

# FONT
font = pygame.font.SysFont("Consolas", 32)

# CLASSES
class Bird:
    def __init__(self, WIN):
        # start pos
        self.x = 50
        self.y = 200
        # pixel
        self.width = 34
        self.height = 24
        # physics
        self.velocity = 0
        self.gravity = 0.5
        self.WIN = WIN

    def update(self):
        self.velocity += self.gravity
        self.y += self.velocity

    def jump(self):
        self.velocity = -7

    def draw(self, WIN):
        WIN.blit(bird_image, (self.x, self.y))

class Pipe:
    def __init__(self, x, WIN):
        # position
        self.x = x
        # pixel
        self.width = 52
        self.top_height = random.randint(100,300)
        self.bottom_height = 512 - self.top_height - 100
        #self.bird = bird
        self.WIN = WIN

    def update(self):
        self.x -= 2

    def offscreen(self):
        return self.x < -self.width
    
    def collide_with(self, bird):
        if (bird.x + bird.width > self.x and bird.x < self.x + self.width):
            if (bird.y < self.top_height or bird.y + bird.height > 512 - self.bottom_height):
                return True
        return False
    
    def draw(self, WIN):
        WIN.blit(reversed_pipe_image, (self.x, 0), (0, 320 - self.top_height, self.width, self.top_height))
        WIN.blit(pipe_image, (self.x, 512 - self.bottom_height), (0, 0, self.width, self.bottom_height))

