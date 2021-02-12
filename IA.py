
from Player import *
from Chessgame import *


class IA(Player):

    def __init__(self, name: str):
        super().__init__(name)
        
    def pickMove(self, board):
        legal_moves = list(board.legal_moves)
        return legal_moves[0]
        

    def evaluate(self, board):
        pass

    def minMax(self):
        pass