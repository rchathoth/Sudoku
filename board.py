import pygame
from cell import Cell
from sudoku_generator import SudokuGenerator, generate_sudoku

class Board:

    def __init__(self, width, height, screen, difficulty):
        self.screen = screen
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty

        generator = SudokuGenerator(9, self.difficulty)

        generator.fill_values()

        self.solution = []
        for row in generator.get_board():
            self.solution.append(row[:])

        generator.remove_cells()
        self.board = [row[:] for row in generator.get_board()]
        self.model = [row[:] for row in self.board]

        #rest of init is pasted from notes

        self.cells = []
        cell_size = min(width // 9, height // 9)
        for row in range(9):
            cell_row = []
            for col in range(9):
                cell = Cell(self.board[row][col], row, col, screen)
                cell.size = cell_size
                cell_row.append(cell)
            self.cells.append(cell_row)
        
        # Track selected cell
        self.selected = None
        
        # Track which cells are editable (not pre-filled)
        self.editable = [[self.board[row][col] == 0 for col in range(9)] for row in range(9)]
    


    
    def draw(self):
        box_size = int(self.width // 3)
        cell_size = box_size // 3

        for i in range(1,3):
            pygame.draw.line(self.screen, "black", (0, i*box_size), (self.height, i*box_size), 8)
            pygame.draw.line(self.screen, "black", (i*box_size, 0), (i*box_size, self.width), 8)
        
        for i in range(1,9):
            pygame.draw.line(self.screen, "black", (i*cell_size, 0), (i*cell_size, self.width), 4)
            pygame.draw.line(self.screen, "black", (0, i*cell_size), (self.height, i*cell_size), 4)
    
    def select(self, row, col):
        self.selected = (row, col)

