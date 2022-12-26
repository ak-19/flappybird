import pygame

class PlayAgain:
    def __init__(self, display):
        self.display = display
        self.font = pygame.font.Font('freesansbold.ttf', 42)

    def draw(self):
        current_render = self.font.render(f'Press "P" to start', True, 'white')
        current_render2 = self.font.render(f'"Space" to jump', True, 'white')
        self.display.blit(current_render, (70, 300))
        self.display.blit(current_render2, (70, 350))