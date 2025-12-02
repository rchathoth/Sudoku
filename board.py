import pygame

class Board:

    def __init__(self, width, height, screen, difficulty):
        self.screen = screen
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
    
    def draw(self):
        