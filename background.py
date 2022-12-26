import pygame

from dimensions import Dimensions

class Background:
    def __init__(self, display) -> None:
        self.display = display
        self.image = pygame.transform.scale(pygame.image.load('assets/bg.png'), (Dimensions.WIDTH, Dimensions.HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)        

    def draw(self):
        self.display.blit(self.image, self.rect)