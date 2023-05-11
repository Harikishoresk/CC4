import numpy as np
import pygame
import sys
import math

Blue = (0,0,255)
Black = (0,0,0)
Red = (255,0,0)
Yellow = (255,255,0)

Row_count =6
Column_count = 7
def create_board():
    board = np.zeros((Row_count, Column_count))
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[Row_count-1][col] == 0

def get_next_open_row(board, col):
    for r in range(Row_count):
        if board[r][col] == 0:
            return r

def print_board(board):
    print(np.flip(board, 0))

def winning_move(board, piece):
#horizontal:
    for c in range(Column_count-3):
        for r in range(Row_count):
            if board[r][c] == piece \
                    and board[r][c+1] == piece \
                    and board[r][c+2] == piece \
                    and board[r][c+3] == piece:
                return True
#vertical:
    for c in range(Column_count):
        for r in range(Row_count-3):
            if board[r][c] == piece \
                    and board[r+1][c] == piece \
                    and board[r+2][c] == piece \
                    and board[r+3][c] == piece:
                return True
#positive slope:
    for c in range(Column_count-3):
        for r in range(Row_count-3):
            if board[r][c] == piece \
                    and board[r+1][c+1] == piece \
                    and board[r+2][c+2] == piece \
                    and board[r+3][c+3] == piece:
                return True
#negative slope:
    for c in range(Column_count-3):
        for r in range(3, Row_count):
            if board[r][c] == piece \
                    and board[r-1][c+1] == piece \
                    and board[r-2][c+2] == piece \
                    and board[r-3][c+3] == piece:
                return True

def draw_board(board):
    for c in range(Column_count):
        for r in range(Row_count):
            pygame.draw.rect(screen,Blue, (c*square_size, r*square_size+square_size, square_size, square_size))
            pygame.draw.circle(screen, Black, (int(c*square_size+square_size/2), int(r*square_size+square_size+square_size/2)), Radius)

    for c in range(Column_count):
        for r in range(Row_count):
            if board[r][c] == 1:
                pygame.draw.circle(screen, Red, (int(c * square_size + square_size / 2), height - int(r * square_size + square_size / 2)), Radius)
            if board[r][c] == 2:
                pygame.draw.circle(screen, Yellow, (int(c * square_size + square_size / 2), height - int(r * square_size + square_size / 2)), Radius)
    pygame.display.update()

board = create_board()
print_board(board)
game_over = False
turn = 0

pygame.init()

square_size = 100

width = Column_count*square_size
height = (Row_count+1)*square_size

size = (width, height)

Radius = int(square_size/2 - 5)

screen = pygame.display.set_mode(size)

draw_board(board)
pygame.display.update()

myfont = pygame.font.SysFont("monospace", 35)

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, Black, (0,0, width, square_size))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, Red, (posx, int(square_size/2)), Radius)
            else:
                pygame.draw.circle(screen, Yellow, (posx, int(square_size/2)), Radius)
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, Black, (0, 0, width, square_size))

            # player-1
            if turn == 0:
                posx = event.pos[0]
                col = int(math.floor(posx/square_size))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 1)

                    if winning_move(board, 1):
                        label = myfont.render("🤩CONGRATS!!, PLAYER-1 WINS", 1 , Red)
                        screen.blit(label, (40,10))
                        game_over = True

            else:
                posx = event.pos[0]
                col = int(math.floor(posx / square_size))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 2)

                    if winning_move(board, 2):
                        label = myfont.render("🤩CONGRATS!!, PLAYER-2 WINS", 2 , Yellow)
                        screen.blit(label, (40, 10))
                        game_over = True

            print_board(board)
            draw_board(board)

            turn += 1
            turn = turn % 2

            if game_over:
                pygame.time.wait(3000)