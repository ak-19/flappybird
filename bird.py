import pygame

from dimensions import Dimensions

class Bird:
    def __init__(self, display):
        self.display = display
        self.image = pygame.transform.scale(pygame.image.load('assets/bird.png'), (48, 48))
        self.rect = self.image.get_rect()
        
        self.rect.x = 100
        self.rect.y = 370
        self.dy = 6

    def update(self):
        self.rect.y  = min(Dimensions.HEIGHT - 165, max(0, self.rect.y  + self.dy))

    def set_move(self, dy):
        self.dy = dy

    def draw(self):
        self.display.blit(self.image,  self.rect)