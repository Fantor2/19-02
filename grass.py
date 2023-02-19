import pygame as pg

class Grass(pg.sprite.Sprite):
    def __init__(self,filename,screen):
        self.screen = screen
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(
            filename).convert()
        self.rect = self.image.get_rect()
    def update(self):
        pass
    def draw(self):
        self.screen_blit(self.image,self.rect)
