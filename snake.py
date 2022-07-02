import pygame as pg

from constants import CELL_SIZE


class Snake:
    def __init__(self, screen, pos):
        self.screen = screen

        self.new_block = False
        self.dir = pg.Vector2(1, 0)
        self.last_dir = self.dir
        self.body = [pos + 2 * self.dir, pos + self.dir, pos]

        self.head_up_sprite = pg.image.load('Sprites/head_up.png').convert_alpha()
        self.head_down_sprite = pg.image.load('Sprites/head_down.png').convert_alpha()
        self.head_right_sprite = pg.image.load('Sprites/head_right.png').convert_alpha()
        self.head_left_sprite = pg.image.load('Sprites/head_left.png').convert_alpha()

        self.tail_up_sprite = pg.image.load('Sprites/tail_up.png').convert_alpha()
        self.tail_down_sprite = pg.image.load('Sprites/tail_down.png').convert_alpha()
        self.tail_right_sprite = pg.image.load('Sprites/tail_right.png').convert_alpha()
        self.tail_left_sprite = pg.image.load('Sprites/tail_left.png').convert_alpha()

        self.body_vertical_sprite = pg.image.load('Sprites/body_vertical.png').convert_alpha()
        self.body_horizontal_sprite = pg.image.load('Sprites/body_horizontal.png').convert_alpha()

        self.body_tr_sprite = pg.image.load('Sprites/body_tr.png').convert_alpha()
        self.body_tl_sprite = pg.image.load('Sprites/body_tl.png').convert_alpha()
        self.body_br_sprite = pg.image.load('Sprites/body_br.png').convert_alpha()
        self.body_bl_sprite = pg.image.load('Sprites/body_bl.png').convert_alpha()

    def move(self):
        body_copy = self.body[:(len(self.body) if self.new_block else -1)]
        body_copy.insert(0, body_copy[0] + self.dir)
        self.body = body_copy
        self.last_dir = self.dir
        self.new_block = False

    def add_block(self):
        self.new_block = True

    def draw(self):
        self.draw_head()
        self.draw_tail()

        for index, block in enumerate(self.body):
            rect = pg.Rect(int(block.x * CELL_SIZE), int(block.y * CELL_SIZE), CELL_SIZE, CELL_SIZE)

            if index == 0 or index == len(self.body) - 1:
                continue
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    self.screen.blit(self.body_vertical_sprite, rect)
                elif previous_block.y == next_block.y:
                    self.screen.blit(self.body_horizontal_sprite, rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        self.screen.blit(self.body_tl_sprite, rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        self.screen.blit(self.body_bl_sprite, rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        self.screen.blit(self.body_tr_sprite, rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        self.screen.blit(self.body_br_sprite, rect)

    def draw_head(self):
        head_sprite = self.head_left_sprite
        head_relation = self.body[1] - self.body[0]

        if head_relation == pg.Vector2(1, 0):
            head_sprite = self.head_left_sprite
        elif head_relation == pg.Vector2(-1, 0):
            head_sprite = self.head_right_sprite
        elif head_relation == pg.Vector2(0, 1):
            head_sprite = self.head_up_sprite
        elif head_relation == pg.Vector2(0, -1):
            head_sprite = self.head_down_sprite

        x, y = int(self.body[0].x * CELL_SIZE), int(self.body[0].y * CELL_SIZE)
        self.screen.blit(head_sprite, pg.Rect(x, y, CELL_SIZE, CELL_SIZE))

    def draw_tail(self):
        tail_sprite = self.tail_left_sprite
        tail_relation = self.body[-2] - self.body[-1]

        if tail_relation == pg.Vector2(1, 0):
            tail_sprite = self.tail_left_sprite
        elif tail_relation == pg.Vector2(-1, 0):
            tail_sprite = self.tail_right_sprite
        elif tail_relation == pg.Vector2(0, 1):
            tail_sprite = self.tail_up_sprite
        elif tail_relation == pg.Vector2(0, -1):
            tail_sprite = self.tail_down_sprite

        x, y = int(self.body[-1].x * CELL_SIZE), int(self.body[-1].y * CELL_SIZE)
        self.screen.blit(tail_sprite, pg.Rect(x, y, CELL_SIZE, CELL_SIZE))
