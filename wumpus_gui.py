import pygame
import World

B_R, B_C = 10, 10
SQUARE_LEN = 60

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

def refresh_graphics(board, dir, screen):
    font = pygame.font.Font(None, 30)
    info = ''
    for c in range(B_C):
        board[c], board[B_C-c-1] = board[B_C-c-1], board[c]

    bg_img = pygame.image.load('icons/bg.jpg')
    icon_size = (SQUARE_LEN-1, SQUARE_LEN-1)
    bg_img = pygame.transform.scale(bg_img, icon_size)

    wump_img = pygame.image.load('icons/wumpus.png')
    wump_img = pygame.transform.scale(wump_img, icon_size)

    player_right = pygame.image.load('icons/agent_right1.png')
    player_right = pygame.transform.scale(player_right, icon_size)

    player_left = pygame.image.load('icons/agent_left1.png')
    player_left = pygame.transform.scale(player_left, icon_size)

    player_up = pygame.image.load('icons/agent_up1.png')
    player_up = pygame.transform.scale(player_up, icon_size)

    player_down = pygame.image.load('icons/agent_down1.png')
    player_down = pygame.transform.scale(player_down, icon_size)

    pit_img = pygame.image.load('icons/pit.png')
    pit_img = pygame.transform.scale(pit_img, icon_size)

    gold_img = pygame.image.load('icons/gold.png')
    gold_img = pygame.transform.scale(gold_img, icon_size)

    breeze_img = pygame.image.load('icons/breeze.png')
    breeze_img = pygame.transform.scale(breeze_img, icon_size)

    stench_img = pygame.image.load('icons/stench.png')
    stench_img = pygame.transform.scale(stench_img, icon_size)

    alt_bg_img = pygame.image.load('icons/bg1.png')
    alt_bg_img = pygame.transform.scale(alt_bg_img, icon_size)

    color = MEDIUMSEAGREEN
    for col in range(B_C):
        for row in range(B_R):
            pos = (col*SQUARE_LEN, B_R*SQUARE_LEN - row*SQUARE_LEN-SQUARE_LEN)
            screen.blit(bg_img, pos)
            
            if board[col][row].agent:
                player_img = player_right
                if dir == 0:
                    player_img = player_right
                    # info += '>'
                elif dir == 1:
                    player_img = player_down
                    # info += 'v'
                elif dir == 2:
                    player_img = player_left
                    # info += '<'
                elif dir == 3:
                    player_img = player_up
                    # info += '^'
                screen.blit(player_img, pos)
            if board[col][row].wumpus:
                screen.blit(wump_img, pos)
            if board[col][row].pit:
                screen.blit(pit_img, pos)
                # info += 'P'
            if board[col][row].gold:
                screen.blit(gold_img, pos)
                # info += 'G'
            if board[col][row].breeze:
                screen.blit(breeze_img, pos)
                # info += 'B'
            if board[col][row].stench:
                screen.blit(stench_img, pos)
                # info += 'S'
            
            if not board[col][row].visited:
                screen.blit(alt_bg_img, pos)
            # pygame.draw.rect(screen, color, (col*SQUARE_LEN, B_R*SQUARE_LEN - row*SQUARE_LEN-SQUARE_LEN, SQUARE_LEN-2, SQUARE_LEN-2))
            
            text = font.render(info, True, (BLACK))
            text_rect = text.get_rect(center=(col*SQUARE_LEN+SQUARE_LEN//2, B_R*SQUARE_LEN-SQUARE_LEN - row*SQUARE_LEN+SQUARE_LEN//2))
            screen.blit(text, text_rect)
            info = '' 
            color = MEDIUMSEAGREEN
                
    pygame.display.update()
    pass


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
