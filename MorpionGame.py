#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 16:36:06 2021

@author: macmac
"""

from Player import *
from IA import *
from more_itertools import locate

class MorpionGame:
    
    NUM_SQUARES = 9
    EMPTY = ' '
    
    def __init__(self):
        #self.board = [self.board.append(EMPTY) for square in range(NUM_SQUARES)]
        self.board = self.new_board()
        self.win_conditions = ( (0, 1, 2),
                               (3, 4, 5), 
                               (6, 7, 8),
                               (0, 3, 6),
                               (1, 4, 7),
                               (2, 5, 8),
                               (0, 4, 8), 
                               (2, 4, 6) )
#         self.player = player #  X or O
        
    def new_board(self):
        """Create new board."""
        board = []
        for square in range(self.NUM_SQUARES):
            board.append(self.EMPTY)
        return board

#     def print(self):
#         return(print(self.board))

#     def display_board(self):
    
    def print(self):
        """Display the board on screen."""
        print("\n\t",self.board[0],"|",self.board[1],"|",self.board[2])
        print("\n\t-----------")
        print("\n\t",self.board[3],"|",self.board[4],"|",self.board[5])
        print("\n\t-----------")
        print("\n\t",self.board[6],"|",self.board[7],"|",self.board[8], "\n")
    
    
    def display_Choices():
        print ("-------------")
        print ("-------------")
        print ("  0 | 1 | 2")
        print ("  ---------")
        print ("  3 | 4 | 5")
        print ("  ---------")
        print ("  6 | 7 | 8")
        print ("-------------")
        print ("-------------")
        
     
    def empty_spots(self):
        """Create a list of empty/legal spots moves."""
        return list(locate(self.board,lambda s: s == self.EMPTY))
        
        
    
    def move(self, player, moveChoice:int):
        """Checks if the move choice is legal and returns True or False. If it's true the board is modified."""
        availableSpots = self.empty_spots()
        
        if moveChoice in availableSpots:
            
            self.board[moveChoice] = player.sign
            allowed = True
            
        else:
            print("This move is not allowed !")
            allowed = False

        return allowed
    
    
    
    def check_win(self,player):
        """Checks if the player (self.player) is the winner."""
        """ check if the player won """
        bool_ = False
      
        for condition in self.win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] == player.sign:
                bool_ = True
                
                return(True)
                #print("PLAYER ",self.player,"WINS")
        return(bool_)
    


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
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != ' ':
#                 bool_ = True               
            return(True)
            #print("PLAYER ",self.player,"WINS")

    if ' ' in board:
        return(False)
    else:
        return(True)


"""        

print("Initial board :")
#morpionBoard = [None, 'X', None, None, 'O', 'X', None,'O',None]

game = MorpionGame()
print(game.player)
print(game.board)
game.board[1]=game.player
print(game.board)
available = game.empty_spots()
print(available)
choix = 4
print(game.move(choix))
game.display_board()
"""