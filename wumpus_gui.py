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

RADIUS = 0.45*SQUARE_LEN

def board_graphics_init():
    pygame.init()
    board_width = B_R * SQUARE_LEN
    board_height = (B_C+1) * SQUARE_LEN
    screen = pygame.display.set_mode((board_width, board_height))
    return screen

def refresh_screen(board, screen):
    wump_img = pygame.image.load("icons/wumpus.png").convert()
    wump_img = pygame.transform.rotozoom(wump_img, 0, 0.25)
    pit_img = pygame.image.load("icons/pit.png").convert()
    pit_img = pygame.transform.rotozoom(pit_img, 0, 0.1)
    gold_img = pygame.image.load("icons/gold.png").convert()
    gold_img = pygame.transform.rotozoom(gold_img, 0, 0.1)
    bg_img = pygame.image.load("icons/bg.jpg").convert()
    bg_img = pygame.transform.rotozoom(bg_img, 0, 0.1)
    # screen.blit(gold_img, (0, 0)) 
    img = bg_img
    for col in range(B_C):
        for row in range(B_R):
            pygame.draw.rect(screen, BLUE, (col*SQUARE_LEN, row*SQUARE_LEN+SQUARE_LEN, SQUARE_LEN, SQUARE_LEN))
            if board[col][row].gold == True:
                img = gold_img
            elif board[col][row].pit == True:
                img = pit_img
            elif board[col][row].wumpus == True:
                img = wump_img
            screen.blit(img, (int(col*SQUARE_LEN), int(row*SQUARE_LEN+SQUARE_LEN))) 
            img = bg_img
    pygame.display.update() 

# def draw(screen):
#     pygame.draw.circle(screen, WHITE, (50, 50), RADIUS)
#     pygame.display.update()
