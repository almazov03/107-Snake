import pygame as pg

from constants import CELL_SIZE
from fruit import Fruit


class Score:
    def __init__(self, screen, font, pos):
        self.font = font
        self.screen = screen
        self.pos = pos * CELL_SIZE
        self.res = 0

    def add(self): self.res += 1

    def draw(self):
        score_surface = self.font.render(f'SCORE : {self.res}', True, (56, 74, 12))
        self.screen.blit(score_surface, self.pos)


