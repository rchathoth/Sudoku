import pygame
from board import Board
from cell import Cell
from sudoku_generator import generate_sudoku

pygame.init()

'''
FLOW OF THIS FILE:
Initialize Pygame - done
  ↓
start_screen() [LOOP: wait for difficulty selection]
  ↓
difficulty selected
  ↓
Create Board(difficulty)
  ↓
Main Game Loop [LOOP: handle events, draw, check win]
  ├─ Handle mouse/keyboard
  ├─ Update board
  ├─ Draw everything
  └─ Check if won?
       ↓ (if won)
Game Over Screen
  ↓
Restart or Exit?
  ↓
END
'''

# CONSTANTS
WIDTH, HEIGHT = 540, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
LIGHT_GRAY = (240, 240, 240)

# BUTTON CLASS
class Button:
    def __init__(self, text, x, y, width, height, font_size=30):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.color = GRAY
        self.font = pygame.font.SysFont("Arial", font_size)
    
    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)
        pygame.draw.rect(win, BLACK, self.rect, 2)
        txt = self.font.render(self.text, True, BLACK)
        text_x = self.rect.x + (self.rect.width / 2) - (txt.get_width() / 2)
        text_y = self.rect.y + (self.rect.height / 2) - (txt.get_height() / 2)

        win.blit(txt, (text_x, text_y))
    
    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

# START SCREEN
def start_screen(screen):    
    title_font = pygame.font.SysFont("Arial", 60)
    title_text = title_font.render("Welcome to Sudoku", True, BLACK)

    easy_btn = Button("Easy", 170, 200, 200, 60)
    medium_btn = Button("Medium", 170, 300, 200, 60)
    hard_btn = Button("Hard", 170, 400, 200, 60)
    
    loop = True

    while loop:
        screen.fill(WHITE)
        
        title_x = (WIDTH / 2) - (title_text.get_width() / 2)
        screen.blit(title_text, (title_x, 100))
        
        easy_btn.draw(screen)
        medium_btn.draw(screen)
        hard_btn.draw(screen)
        
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                
                if easy_btn.is_clicked(pos):
                    difficulty = 30
                    loop = False
                elif medium_btn.is_clicked(pos):
                    difficulty = 40
                    loop = False
                elif hard_btn.is_clicked(pos):
                    difficulty = 50
                    loop = False
    
    return difficulty

# MAIN FUNCTION
def main():
    pass

def game_over():
    pass

if __name__ == "__main__":
    main()

