import pygame
from random import randint, gauss
pygame.font.init()
SCREEN_SIZE = (800, 600)


def rend_color():
    return (randint(0, 255), randint(0, 255), randint(0, 255))


class Snake:
    def __init__(self, coord, health, size, color=None):
        self.coord = coord
        self.health = health
        self.size = size
        if color == None:
            color = rend_color()
        self.color = color




class GameField:
    pass


class Enemy:
    def __init__(self, coord = None, color = None, rad=10):
        """Create enemy, color and size"""
        if coord == None:
            color = [randint(rad, SCREEN_SIZE[0] - rad), randint(rad, SCREEN_SIZE[1] - rad)]
        self.coord = coord
        if color == None:
            color = rend_color()
        self.color = color

    def check_snake_take(self, ball):
        dist = sum([(self.coord[i] - ball.coord[i])**2 for i in range(2)])**0.5
        min_dist = self.rad + ball.rad
        return dist <= min_dist


class GameManager:
    pass

