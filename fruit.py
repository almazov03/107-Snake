import random
import pygame as pg

from constants import CELL_SIZE, CELL_NUMBER


class Fruit:
    def __init__(self, screen, pos):
        self.screen = screen
        self.pos = pos
        self.sprite = pg.image.load('Sprites/apple.png').convert_alpha()

    def draw(self):
        rect = pg.Rect(int(self.pos.x * CELL_SIZE), int(self.pos.y * CELL_SIZE), CELL_SIZE, CELL_SIZE)
        self.screen.blit(self.sprite, rect)
