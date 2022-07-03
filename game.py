import pygame as pg
from random import randint
import sys

from snake import Snake
from fruit import Fruit
from score import Score
from constants import CELL_SIZE, CELL_NUMBER, FPS

SCREEN_UPDATE = pg.USEREVENT


class Game:
    def __init__(self):
        pg.init()

        self.font = pg.font.Font('Fonts/supermario.otf', 30)
        self.crunch_sound = pg.mixer.Sound('Sounds/crunch.wav')

        self.screen = pg.display.set_mode((CELL_NUMBER * CELL_SIZE, CELL_NUMBER * CELL_SIZE))
        self.clock = pg.time.Clock()

        self.snake = Snake(self.screen, pg.Vector2(5, 5))
        self.fruit = Fruit(self.screen, self.get_random_pos())
        self.score = Score(self.screen, self.font, pg.Vector2(CELL_NUMBER // 2 - 2, 0))

        pg.time.set_timer(SCREEN_UPDATE, 125)

    def get_random_pos(self):
        area = [[] for _ in range(CELL_NUMBER)]
        for i in range(CELL_NUMBER):
            area[i] = [0 for _ in range(CELL_NUMBER)]
        for block in self.snake.body:
            area[int(block.x)][int(block.y)] = 1
        free_pos = list()
        for i in range(CELL_NUMBER):
            for j in range(CELL_NUMBER):
                if area[i][j]:
                    continue
                free_pos.append(pg.Vector2(i, j))
        return free_pos[randint(0, len(free_pos) - 1)]

    def game_over(self):
        pg.quit()
        sys.exit()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit = Fruit(self.screen, self.get_random_pos())
            self.snake.add_block()
            self.score.add()
            self.crunch_sound.play()

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < CELL_NUMBER or not 0 <= self.snake.body[0].y < CELL_NUMBER:
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def handle_input(self, event):
        if event.key == pg.K_UP and self.snake.last_dir != pg.Vector2(0, 1):
            self.snake.dir = pg.Vector2(0, -1)
        if event.key == pg.K_DOWN and self.snake.last_dir != pg.Vector2(0, -1):
            self.snake.dir = pg.Vector2(0, 1)
        if event.key == pg.K_LEFT and self.snake.last_dir != pg.Vector2(1, 0):
            self.snake.dir = pg.Vector2(-1, 0)
        if event.key == pg.K_RIGHT and self.snake.last_dir != pg.Vector2(-1, 0):
            self.snake.dir = pg.Vector2(1, 0)

    def update(self):
        self.check_fail()
        self.check_collision()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.game_over()
            if event.type == SCREEN_UPDATE:
                self.snake.move()
            if event.type == pg.KEYDOWN:
                self.handle_input(event)

    def render(self):
        self.screen.fill((175, 215, 70))
        self.snake.draw()
        self.fruit.draw()
        self.score.draw()

    def run(self):
        while True:
            self.update()
            self.render()

            pg.display.update()
            self.clock.tick(FPS)
