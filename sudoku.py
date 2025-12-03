import pygame
from board import Board
from cell import Cell
from sudoku_generator import generate_sudoku

pygame.init()

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
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")

    running = True

    while running:
        # Start screen → choose difficulty
        difficulty = start_screen(screen)
        if difficulty is None:   # user closed window
            break

        # Create board: 540px for grid, bottom 60px for buttons
        board_height = 540
        board = Board(WIDTH, board_height, screen, difficulty)

        # Create buttons under the board
        btn_y = board_height + 10   # e.g., y = 550
        reset_btn   = Button("Reset",   40,  btn_y, 120, 40)
        restart_btn = Button("Restart", 210, btn_y, 120, 40)
        exit_btn    = Button("Exit",    380, btn_y, 120, 40)

        playing = True

        while playing:
            screen.fill(WHITE)

            # Draw board and buttons
            board.draw()
            reset_btn.draw(screen)
            restart_btn.draw(screen)
            exit_btn.draw(screen)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    playing = False
                    running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()

                    # Button clicks
                    if reset_btn.is_clicked((mx, my)):
                        board.reset_to_original()
                    elif restart_btn.is_clicked((mx, my)):
                        playing = False   # back to start screen
                    elif exit_btn.is_clicked((mx, my)):
                        playing = False
                        running = False
                    else:
                        # Click inside board area -> compute row/col from mouse coords
                        if my < board_height:
                            # get cell size from board (set in Board.__init__)
                            try:
                                cell_size = board.cells[0][0].size
                            except Exception:
                                cell_size = min(WIDTH // 9, board_height // 9)
                            col = mx // cell_size
                            row = my // cell_size
                            if 0 <= row < board.rows and 0 <= col < board.cols:
                                board.select(row, col)


                elif event.type == pygame.KEYDOWN:
                    # Number keys 1–9: sketch value (store as sketched_value on the selected cell)
                    if pygame.K_1 <= event.key <= pygame.K_9:
                        num = event.key - pygame.K_0
                        if board.selected:
                            r, c = board.selected
                            if board.editable[r][c]:
                                board.cells[r][c].sketched_value = num

                    # Enter: commit sketched value
                    elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                        if board.selected:
                            r, c = board.selected
                            cell = board.cells[r][c]
                            if cell.sketched_value != 0:
                                board.place_number(cell.sketched_value)

                    # Delete / Backspace: clear selected cell (only if editable)
                    elif event.key in (pygame.K_BACKSPACE, pygame.K_DELETE):
                        if board.selected:
                            r, c = board.selected
                            if board.editable[r][c]:
                                board.cells[r][c].value = 0
                                board.cells[r][c].sketched_value = 0
                                board.update_board()

                    # Arrow keys: move selection (wrap/clamp within bounds)
                    elif event.key in (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT):
                        if not board.selected:
                            board.select(0, 0)
                        else:
                            r, c = board.selected
                            if event.key == pygame.K_UP:
                                r = max(0, r - 1)
                            elif event.key == pygame.K_DOWN:
                                r = min(board.rows - 1, r + 1)
                            elif event.key == pygame.K_LEFT:
                                c = max(0, c - 1)
                            elif event.key == pygame.K_RIGHT:
                                c = min(board.cols - 1, c + 1)
                            board.select(r, c)

            # After events: check win/lose once board is full
            if playing and board.is_full():
                won = board.check_board()
                result = game_over(screen, won)
                if result == "restart":
                    playing = False     # go back to outer loop → start_screen()
                else:
                    playing = False
                    running = False

    pygame.quit()

def game_over(screen, won):

    big_font = pygame.font.SysFont("Arial", 60)
    small_font = pygame.font.SysFont("Arial", 30)

    if won:
        title = big_font.render("You Win!", True, (0, 150, 0))
    else:
        title = big_font.render("You Lose!", True, (200, 0, 0))

    subtitle = small_font.render("Press R to restart or Q to quit", True, BLACK)

    title_x = WIDTH // 2 - title.get_width() // 2
    title_y = HEIGHT // 2 - 60
    sub_x = WIDTH // 2 - subtitle.get_width() // 2
    sub_y = HEIGHT // 2 + 10

    waiting = True
    while waiting:
        screen.fill(WHITE)
        screen.blit(title, (title_x, title_y))
        screen.blit(subtitle, (sub_x, sub_y))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return "restart"
                if event.key == pygame.K_q:
                    return "quit"

if __name__ == "__main__":
    main()

