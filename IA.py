from Player import *
from Chessgame import *
# from MorpionGame import is_game_over
import random



def is_game_over(board):
#         bool_ = False
    win_conditions = ( (0, 1, 2),
                           (3, 4, 5), 
                           (6, 7, 8),
                           (0, 3, 6),
                           (1, 4, 7),
                           (2, 5, 8),
                           (0, 4, 8), 
                           (2, 4, 6) )
    for condition in win_conditions:
        if board[condition[0]] != ' ' and board[condition[0]] == board[condition[1]] == board[condition[2]] :
#                 bool_ = True               
            return(True)
            #print("PLAYER ",self.player,"WINS")

    if ' ' in board:
        return(False)
    else:
        return(True)
    
def a_winner(board):
    bool_ = False
    win_conditions = ( (0, 1, 2),
                           (3, 4, 5), 
                           (6, 7, 8),
                           (0, 3, 6),
                           (1, 4, 7),
                           (2, 5, 8),
                           (0, 4, 8), 
                           (2, 4, 6) )
    for condition in win_conditions:
        if board[condition[0]] != ' ' and board[condition[0]] == board[condition[1]] == board[condition[2]] :
            bool_ = True               
            return(True)
#             print("PLAYER ",self.player,"WINS"
    return(bool_)

class IA(Player):

    def __init__(self, name: str):
        super().__init__(name)
    
    def movin(self,board,move,min_or_max):
        try:
            if len(board)==9:
                feuille = list(board)
                if min_or_max == "max":
                    feuille[move] = self.sign
                else:
                    if self.sign == 'X':
                        feuille[move] = 'O'
                    else:
                        feuille[move] = 'X'
            
            
        except:
            feuille = board
        return(feuille)
        
    
    
    def leg_moves(self,board):
        try:
            if len(board)==9:
                legal_moves = [i for i, x in enumerate(board) if x == ' ']
            
            
            
        except:
            legal_moves = list(board.legal_moves)
        return(legal_moves)
    

    def pickMove(self, board):
        
        try:
            if len(board)==9:
                legal_moves = [i for i, x in enumerate(board) if x == ' ']
                feuilles_score = []
                for moves in legal_moves:
                    feuille = list(board)
                    feuille[moves] = self.sign
                    feuilles_score.append(self.minMax(feuille,10,"min"))
                index_max = feuilles_score.index(max(feuilles_score))
                move = legal_moves[index_max]
            
        except:
            legal_moves = list(board.legal_moves)
            move = random.choice(legal_moves) 
        return(move)

    def evaluate(self, board):
        try:
            if len(board)==9:
                win = self.check_win_board(board)
                if win:
                    return(100)
                elif a_winner(board):
                    return(-100)
                elif is_game_over(board):
                    return(-20)
                else:
                    return(0)
            
            
        except:
            return(0)



    def minMax(self, board, depth, min_or_max: str):
        
        if depth == 0 or is_game_over(board):
            
#             if self.evaluate(board)*(depth+1) != 0:
#                 print("SCORE = ", self.evaluate(board)*(depth+1))
            return self.evaluate(board)
        
        if min_or_max == "max" :
            value = -10000
            for move in self.leg_moves(board):
                feuille = self.movin(board,move,min_or_max)
                value = max(value, self.minMax(feuille, depth-1, "min"))
            return value
        else:
            value = 10000
            for move in self.leg_moves(board):
                feuille = self.movin(board,move,min_or_max)
                value = min(value, self.minMax(feuille, depth-1, "max"))
            return value