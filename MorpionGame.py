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
    
    # Board dimension = 3 A MODIFIER
    # dim = 3
    
    def __init__(self,player : str):
        self.board = [None, None, None, None, None, None, None,None,None]
        self.player = player #  X or O
         
         
         
#def newGameBoard(self):
    # morpionBoard = [None] * dim
    #morpionBoard = [None]
        
    
    def displayBoard(self):
        print(self.board[0],"|",self.board[1],"|",self.board[2])
        print("---------")
        print(self.board[3],"|",self.board[4],"|",self.board[5])
        print("---------")
        print(self.board[6],"|",self.board[7],self.board[8])
    
    
    def displayChoices():
        print ("-------------")
        print ("-------------")
        print ("  0 | 1 | 2")
        print ("  ---------")
        print ("  3 | 4 | 5")
        print ("  ---------")
        print ("  6 | 7 | 8")
        print ("-------------")
        print ("-------------")
        
    
    # Function emptySpots returns a list of indexes referring to all empty spots available on the board  
    def emptySpots(self):
        return list(locate(self.board,lambda s: s == None))
        #emptyIndex = list(locate(morpionBoard,lambda s: s == None))
        #print(emptyIndex)
        
        
    
    def move(self, moveChoice:int):
        availableSpots = self.emptySpots(self)
        if (moveChoice in availableSpots):
            # need attribute that says wich player is playing so we can put it in the list
            self.board[moveChoice] = game.player
            # why ajouter allowed
            allowed = True
        else:
            print("This move is not allowed !")
            allowed = False
        return allowed
    
        

print("Initial board :")
morpionBoard = [None, 'X', None, None, 'O', 'X', None,'O',None]
player = 'X'
game = MorpionGame
game.board = morpionBoard
game.player = 'X'
MorpionGame.displayBoard(game)
#MorpionGame.displaychoices()
if (MorpionGame.move(game,1)):
    print ("\n\n")
    print("Board after a move :\n")
    MorpionGame.displayBoard(game)
#displaychoices()
