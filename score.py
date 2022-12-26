import pygame

class Score:
    def __init__(self, display):
        self.display = display
        self.font = pygame.font.Font('freesansbold.ttf', 32)

    def draw(self, score):
        current_render = self.font.render(f'Score: {score}', True, 'brown')
        self.display.blit(current_render, (10, 700))