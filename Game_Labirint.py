import pygame
import random
import sys
from colorama.winterm import WinColor
import Windows_Game

# collor
black = WinColor.BLACK
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
gray = (128, 128, 128)

# Клетки лабиринта
doroga = 0
stena = 1
player_cell = 2
exit_cell = 3

# Классы
class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pole = [[stena]*self.height]*self.width
        

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

    def wall(self, x, y):
        pass

    def set_cell(self, x, y, value):
        pass

    def get_cell(self, x, y):
        pass

class Player:
    def __init__(self):
        pass

    def go(self, dx, dy, maze):
        pass


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
    game = Windows_Game.Game()
    game.start()
