import pygame
import os

background_img = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","bg.png")))

class bg:
    def __init__(self, x=0 ,y=0 ):
        self.x = 0
        self.y =0
        self.img = background_img
    
    def draw(self, win):
        win.blit(self.img,(0,0))