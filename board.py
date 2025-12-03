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
        self.original_board = [row[:] for row in self.board]
        self.rows = 9
        self.cols = 9

   

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

        for r in range(self.rows):
            for c in range(self.cols):
                cell = self.cells[r][c]
                if self.selected == (r, c):
                    cell.selected = True
                else:
                    cell.selected = False
                cell.draw()
    
    def select(self, row, col):
        self.selected = (row, col)    

    def place_number(self, value):
        # Sets the value of the current selected cell equal to the user entered value. 
        # Called when the user presses the Enter key.
        if self.selected:
            row, col = self.selected
            if self.editable[row][col]:
                self.cells[row][col].value = value
                self.cells[row][col].sketched_value = 0
                self.update_board()
                
    def reset_to_original(self):
        # Resets all cells in the board to their original values 
        # (0 if cleared, otherwise the corresponding digit).
        for r in range(self.rows):
            for c in range(self.cols):
                self.board[r][c] = self.original_board[r][c]
                self.cells[r][c].value = self.original_board[r][c]
                self.cells[r][c].sketched_value = 0

    def is_full(self):
        # Returns a Boolean value indicating whether the board is full or not.
        for row in self.board:
            for val in row:
                if val == 0:
                    return False
        return True

    def update_board(self):
        # Updates the underlying 2D board with the values in all cells.
        for r in range(self.rows):
            for c in range(self.cols):
                self.board[r][c] = self.cells[r][c].value

    def find_empty(self):
        # Finds an empty cell and returns its row and col as a tuple (x,y).
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] == 0:
                    return (i, j)
        return None

    def check_board(self):
        # Check whether the Sudoku board is solved correctly.
        
        # Check rows
        for row in self.board:
            if sorted(row) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                return False
        
        # Check columns
        for col in range(self.cols):
            column = [self.board[row][col] for row in range(self.rows)]
            if sorted(column) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                return False
        
        # Check 3x3 boxes
        for i in range(0, self.rows, 3):
            for j in range(0, self.cols, 3):
                box = [self.board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if sorted(box) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    return False
        
        # Else return True
        return True
            


