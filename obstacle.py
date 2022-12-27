import pygame

from random import randint

from dimensions import Dimensions

class Obstacle:
    def load_values(self):
        x = Dimensions.WIDTH - Dimensions.OBSTACLE_WIDTH
        y = randint(100, 400)
        
        self.image1 = pygame.transform.scale(pygame.image.load('assets/pipe-down.png'), (Dimensions.OBSTACLE_WIDTH, y))
        self.image2 = pygame.transform.scale(pygame.image.load('assets/pipe-up.png'), (Dimensions.OBSTACLE_WIDTH, 750 - (y - Dimensions.GAP)))

        self.rect1 = self.image1.get_rect()
        self.rect2 = self.image2.get_rect()

        self.rect1.topleft = (x, 0)           
        self.rect2.topleft = (x, y + Dimensions.GAP)           

    def __init__(self, display):
        self.display = display
        self.dx = 6           
        self.load_values()       
        self.score = 0

    def update(self):
        self.rect1.x -= self.dx 
        self.rect2.x -= self.dx 
        if self.rect1.x < 0: 
            self.load_values()
            self.score += 1

    def get_score(self):
        return self.score

    def reset_score(self):
        self.score = 0

    def draw(self):
        self.display.blit(self.image1, self.rect1)   
        self.display.blit(self.image2, self.rect2)   

    def collided_with(self, rect):
        if self.rect1.x <= rect[0] <= self.rect2.x + Dimensions.OBSTACLE_WIDTH or self.rect1.x <= rect[0] + rect[2] <= self.rect1.x  + Dimensions.OBSTACLE_WIDTH:
            if rect[1] < self.rect1.y + Dimensions.GAP or rect[1] + rect[3] >= self.rect2.y:
                return True        
        return False
        