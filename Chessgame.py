import chess
import chess.engine
from Player import *
from IA import *

    
class Chessgame:

    def __init__(self):
        self.game = chess
        self.board = chess.Board()

    #  move = 'e2e4', beg = e2, end = e4
    def move(self, move: str):
        move = move.upper()
        beg = move[0:2] 
        end = move[2:4]
        start_case = getattr(self.game, beg)
        end_case = getattr(self.game, end)
        if (self.game.Move(start_case, end_case) in self.board.legal_moves):
            print(beg,'->', end, ':')
            self.board.push(self.game.Move(start_case, end_case))
            self.print()
            #print(self.info["score"].relative)
            return("done")
            # self.board.pop()
        else:
            print("This move is not allowed !")
            return("fail")

    def print(self):
        print(self.board)
        print()