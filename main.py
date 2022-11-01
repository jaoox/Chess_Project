import pygame
from chessboard import display
from chessboard.board import Board
from chessboard.constants import STARTING_FEN
from chessboard.pieces import Piece, PieceColor, PieceType
from chessboard.fenparser import FenParser

#class Node(object):


print(Board.board_rect)
game_board = display.start()
game_board.update_pieces(STARTING_FEN)

while True:
    display.update(STARTING_FEN, game_board)
    display.movement()



display.terminate()









