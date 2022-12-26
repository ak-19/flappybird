import pygame

from dimensions import Dimensions

class Setup:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Flappy bird')
        self.display = pygame.display.set_mode((Dimensions.WIDTH, Dimensions.HEIGHT))

    def get_display(self):
        return self.display

    def quit(self):
        pygame.quit()