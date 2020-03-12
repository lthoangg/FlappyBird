import pygame
import os

base_img = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","base.png")))

class Base:
    vel = 5
    width =  base_img.get_width()
    img = base_img

    def __init__(self, y=730):
        self.y = y
        self.x1 = 0
        self.x2 = self.width

    def move(self):
        self.x1 -= self.vel
        self.x2 -= self.vel

        if self.x1 + self.width <0:
            self.x1 = self.x2 + self.width
        if self.x2 + self.width <0:
            self.x2 = self.x1 + self.width

    def draw(self, win):
        win.blit(self.img, (self.x1, self.y))
        win.blit(self.img, (self.x2, self.y))