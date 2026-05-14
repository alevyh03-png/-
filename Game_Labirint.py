import pygame
import random
import sys
import time

# размер окна
width = 800
height = 600

clet = 30
fps = 50

# collor
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
gray = (128, 128, 128)

# статус игры
s_menu = 0
s_play = 1
s_pause = 2
s_go = 3

# Клетки лабиринта
doroga = 0
stena = 1
player_cell = 2
exit_cell = 3

# Классы
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Labirint")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 25)
        self.state = s_menu
        self.maze = None
        self.player = None
        self.enemy = None
        self.small_font = pygame.font.Font(None, 15)
        self.difficulty = 1

    def start(self):
        while True:
            self.on_key()
            if self.state == s_play:
                self.tick()
            self.draw()
            pygame.display.flip()
            self.clock.tick(fps)

    def new(self):
        self.state = s_play
        print("New game", self.difficulty)
        self.maze = Maze(11, 11)
        self.maze.make()
        self.player = Player(1, 1)

    def on_key(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_1:
                    self.difficulty = 0
                    self.new()
                if event.key == pygame.K_2:
                    self.difficulty = 1
                    self.new()
                if event.key == pygame.K_3:
                    self.difficulty = 2
                    self.new()
                if self.state == s_play:
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        self.player.go(0, -1, self.maze)
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        self.player.go(0, 1, self.maze)
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        self.player.go(-1, 0, self.maze)
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        self.player.go(1, 0, self.maze)


    def tick(self):
        pass

    def draw(self):
        self.screen.fill(black)
        if self.state == s_menu:
            text = self.font.render("Menu: play 1 2 3", True, white)
            self.screen.blit(text, (30, 30))

        elif self.state == s_play:
            text = self.font.render("Play go", True, white)
            self.screen.blit(text, (30, 30))

            for y in range(self.maze.height):
                for x in range(self.maze.width):
                    c = self.maze.pole[y][x]
                    if c == stena:
                        pygame.draw.rect(self.screen, black, (x * clet, y * clet, clet, clet))
                    elif c == doroga:
                        pygame.draw.rect(self.screen, green, (x * clet, y * clet, clet, clet))
            pygame.draw.rect(self.screen, blue, (self.player.x * clet, self.player.y * clet, clet, clet))

        elif self.state == s_pause:
            text = self.font.render("Pause", True, white)
            self.screen.blit(text, (30, 30))

        elif self.state == s_go:
            text = self.font.render("GAME OVER", True, red)
            self.screen.blit(text, (30, 30))


class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pole = []
        for y in range(height):
            row = []
            for x in range(width):
                row.append(stena)
            self.pole.append(row)

    def is_stena(self, x, y):
        if self.pole[y][x] == stena:
            return True
        return False

    def make(self):
        for y in range(self.height):
            for x in range(self.width):
                if x == 0 or x == self.width - 1 or y == 0 or y == self.height - 1:
                    self.pole[y][x] = stena  # границы — стены
                else:
                    self.pole[y][x] = doroga
        self.pole[self.height - 2][self.width - 2] = exit_cell

    def wall(self, x, y):
        pass

    def set_cell(self, x, y, value):
        pass

    def get_cell(self, x, y):
        pass

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def go(self, dx, dy, maze):
        n_x = self.x + dx
        n_y = self.y + dy
        if not maze.is_stena(n_x, n_y):
            self.x = n_x
            self.y = n_y


class Enemy:
    def __init__(self):
        pass

    def go(self, px, py, maze):
        pass


class UI:
    def __init__(self):
        pass

    def draw_menu(self):
        pass

    def draw_game(self):
        pass

    def draw_pause(self):
        pass

    def draw_over(self):
        pass


if __name__ == '__main__':
    game = Game()
    game.start()
