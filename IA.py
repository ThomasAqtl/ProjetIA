
from Player import *
from Chessgame import *
import random

class IA(Player):

    def __init__(self, name: str):
        super().__init__(name)
        
    def pickMove(self, board):
        legal_moves = list(board.legal_moves)
        return(random.choice(legal_moves))
        

    def evaluate(self, board):
        pass

    def minMax(self):
        pass