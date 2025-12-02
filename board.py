import pygame

class Board:

    def __init__(self, width, height, screen, difficulty):
        self.screen = screen
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
    
    def draw(self):
    

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
                box = [self.board[x][y] for x in range(i + 3) for y in range(j + 3)]
                if sorted(box) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    return False
        
        # Else return True
        return True
            