import pygame
import World

B_R, B_C = 10, 10
SQUARE_LEN = 50

GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
DARKSEAGREEN = (143, 188, 143)
MEDIUMSEAGREEN = (0, 250, 154)

RADIUS = 0.45*SQUARE_LEN

def board_graphics_init():
    pygame.init()
    board_width = B_R * SQUARE_LEN
    board_height = (B_C) * SQUARE_LEN
    screen = pygame.display.set_mode((board_width, board_height))
    return screen

def refresh_screen(board, dir, screen):
    # for c in range(B_C):
    #     for r in range(B_R):
    #         board[c][r], board[B_C-c-1][B_R-r-1] = board[B_C-c-1][B_R-r-1], board[c][r]
    for c in range(B_C):
        board[c], board[B_C-c-1] = board[B_C-c-1], board[c]
    font = pygame.font.Font(None, 30)
    info = ''
    color = MEDIUMSEAGREEN
    for col in range(B_C):
        for row in range(B_R):
            if board[col][row].visited:
                color = DARKSEAGREEN
            if board[col][row].agent:
                if dir == 0:
                    info += '>'
                elif dir == 1:
                    info += 'v'
                elif dir == 2:
                    info += '<'
                elif dir == 3:
                    info += '^'
            if board[col][row].wumpus:
                info += 'W'
            if board[col][row].pit:
                info += 'P'
            if board[col][row].gold:
                info += 'G'
            if board[col][row].breeze:
                info += 'B'
            if board[col][row].stench:
                info += 'S'
            pygame.draw.rect(screen, color, (col*SQUARE_LEN, B_R*SQUARE_LEN - row*SQUARE_LEN-SQUARE_LEN, SQUARE_LEN-2, SQUARE_LEN-2))
            
            text = font.render(info, True, (BLACK))
            text_rect = text.get_rect(center=(col*SQUARE_LEN+SQUARE_LEN//2, B_R*SQUARE_LEN-SQUARE_LEN - row*SQUARE_LEN+SQUARE_LEN//2))
            screen.blit(text, text_rect)
            info = '' 
            color = MEDIUMSEAGREEN
                
    pygame.display.update() 

# def draw(screen):
#     pygame.draw.circle(screen, WHITE, (50, 50), RADIUS)
#     pygame.display.update()
