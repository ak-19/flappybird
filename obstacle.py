import pygame

from random import randint

from dimensions import Dimensions

class Obstacle:
    def load_values(self):
        self.x = Dimensions.WIDTH - Dimensions.OBSTACLE_WIDTH
        self.y = randint(100, 400)

        self.top_obstacle = [self.x, 0, Dimensions.OBSTACLE_WIDTH, self.y]
        self.bottom_obstacle = [self.x, self.y + Dimensions.GAP, Dimensions.OBSTACLE_WIDTH, Dimensions.HEIGHT - (self.y + Dimensions.GAP) - 120]

    def __init__(self, display):
        self.display = display
        self.dx = 6           
        self.load_values()       
        self.score = 0

    def update(self):
        self.top_obstacle[0] -= self.dx 
        self.bottom_obstacle[0] -= self.dx 
        if self.top_obstacle[0] < 0: 
            self.load_values()
            self.score += 1

    def get_score(self):
        return self.score

    def reset_score(self):
        self.score = 0

    def draw(self):
        pygame.draw.rect(self.display, 'green', self.top_obstacle)
        pygame.draw.rect(self.display, 'green', self.bottom_obstacle)

    def collided_with(self, rect):
        if self.top_obstacle[0] <= rect[0] <= self.top_obstacle[0] + Dimensions.OBSTACLE_WIDTH or self.top_obstacle[0] <= rect[0] + rect[2] <= self.top_obstacle[0] + Dimensions.OBSTACLE_WIDTH:
            if rect[1] < self.y or rect[1] + rect[3] > self.y + Dimensions.GAP:
                return True        
        return False
        