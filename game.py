import pygame

from background import Background

from bird import Bird

from obstacle import Obstacle

from score import Score

from play_again import PlayAgain

class Game:
    def load(self):
        self.bird = Bird(self.display)
        self.obstacle = Obstacle(self.display)   
        self.score = 0
             
    def __init__(self, display):
        self.display = display
        self.run = True
        self.pause = False
        self.clock = pygame.time.Clock()
        self.fps = 30
        
        self.background = Background(display)
        self.load()

        self.score_text = Score(display)
        self.play_again_text = PlayAgain(display)

    def run_game_loop(self):
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    self.run = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.bird.set_move(-12)
                    elif event.key == pygame.K_p and self.pause:
                        self.load()
                        self.pause = False
                elif event.type == pygame.KEYUP:
                    self.bird.set_move(6)
            
            self.background.draw()

            if self.pause:                 
                self.play_again_text.draw()
            else:
                self.bird.update()

                self.obstacle.update()
        
                self.bird.draw()

                self.obstacle.draw()

                self.score_text.draw(self.score) 
                
                if self.obstacle.collided_with(self.bird.rect): self.pause = True

                self.score = self.obstacle.get_score()

            pygame.display.update()

            self.clock.tick(self.fps)