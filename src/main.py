import pygame
from pygame.locals import *
from chessPictures import *
from colors import *
from interpreter import draw

first_row = [rock, knight, bishop, queen, king, bishop, knight, rock] #
pawn_row = [pawn] * 8

def create_chessboard():
    board = []
    for row in range(8):
        board_row = []
        for col in range(8):
            if (row + col) % 2 == 0:
                board_row.append(square)
            else:
                board_row.append(square.negative()) #
        board.append(board_row)
    return board

def place_pieces(board):
    for col in range(8):
        board[7][col] = board[7][col].under(first_row[col]) #
        board[6][col] = board[6][col].under(pawn)
        
    for col in range(8):
        board[0][col] = board[0][col].under(first_row[col].negative())
        board[1][col] = board[1][col].under(pawn.negative())

    return board

def build_full_board(board):
    rows = []
    for row in board:
        row_picture = row[0]
        for col in row[1:]:
            row_picture = row_picture.join(col) #
        rows.append(row_picture)

    full_board = rows[0]
    for row_picture in rows[1:]:
        full_board = full_board.up(row_picture) #

    return full_board

if __name__ == "__main__":
    board = create_chessboard()
    board = place_pieces(board)
    full_board_picture = build_full_board(board)
    draw(full_board_picture)
