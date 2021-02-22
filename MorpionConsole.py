#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 16:33:12 2021

@author: macmac
"""

import cmd
from MorpionGame import *

intro1 = 'Type <help> to list available commands.\n'
intro2 = 'Type <help> <command> to see details about given command.\n'
intro3 = 'Type <start> to begin a game.\n'


class MorpionConsole(cmd.Cmd):
    
    def __init__(self, mode: str):
        
        cmd.Cmd.__init__(self)
        self.player = None
        self.ia1 = None
        self.ia2 = None

        self.prompt = 'Tic-Tac-Toe > '
        self.completekey = 'tab'
        self.intro = intro1+intro2+intro3
        self.Game = None

        if mode == 'HvsIA':
            self.player = Player('Player 1')
            self.player.turn = True
            self.player.sign = 'X'

            self.ia1 = IA('IA1')
            self.ia1.turn = False
            self.ia1.sign = 'O'

        elif mode == 'IAvsIA':
            self.ia1 = IA('IA1')
            self.ia1.turn = True
            self.ia1.sign = 'X'

            self.ia2 = IA('IA2')
            self.ia2.turn = False
            self.ia2.sign = 'O'
    
    def do_start(self, arg):
        """
        Start a new game.\n 
        If you are in IA vs IA mode, the game will run automatically.\n
        """
        if self.Game != None:
            print('A game is already running')
        else:
            self.Game = MorpionGame()
            self.Game.print()
            ##############
            #print what ??
            ##############
            
     
    def do_move(self, arg): 
        """
        Plays a move if a game has started. \n 
        Moves are written as the number of case
        - Use : move <move>
        - Ex : move 5
        """
#         if self.Game == None:
#             print('You need to start a game !')
       
#         else:
            
#             if self.player != None:
                
#                 if self.player.turn == True:
                    
#                     #print("Which case number do you choose ?")
#                     #self.Game.displayChoices()
#                     try:
#                         self.Game.move(arg)
#                         self.player.turn = not self.player.turn
#                          ##############
#                          #How do we know where to catch the exception ????
#                          ##############
#                     except:
#                         print('Your input is incorrect.')
#                 else:
#                     print('It is not your turn.')

        if self.Game == None:
            print('You need to start a game !')
        else:
            if self.player != None:
                if self.player.turn == True:
                    res = None
                    try:
                        res = self.Game.move(self.player,int(arg))
                        
                    except:
                        
                        print('Your input is incorrect.')
                        res = False
                    if res :
                        self.Game.print()
#                         print(self.Game.check_win(self.player))
                        self.ia1.turn = not self.ia1.turn
                        self.player.turn = not self.player.turn

                else:
                    print('It is not your turn.')
            
    # called after each command. 
    # checks if game is ended
    
    def postcmd(self, line, stop):
        if self.Game != None:
            
            if self.player != None:
                if self.player.turn :
                    player = self.ia1
                elif self.ia1.turn :
                    player = self.player
            elif self.ia2 != None:
                if self.ia2.turn :
                    player = self.ia1
                elif self.ia1.turn :
                    player = self.ia2

            if self.Game.check_win(player):

                if self.player != None:
                    if self.player.turn :
                        print("You lost :'(")
                    else:
                        print('You won !')
                    return True

                else:
                    if self.ia1 != None and self.ia2 != None:
                        if self.ia1.turn:
                            print('IA2 won !')
                        elif self.ia2.turn:
                            print('IA1 won !')
            elif is_game_over(self.Game.board):
                print('Game over : no winner')
                    
            elif self.player != None:
                self.player.evaluate(self.Game.board)
                self.ia1.evaluate(self.Game.board)

                if self.ia1.turn :

                    move = self.ia1.pickMove(self.Game.board)
#                     if (move in self.Game.board.legal_moves):

                    self.Game.move(self.ia1,move)
                    self.Game.print()
                    self.ia1.turn = not self.ia1.turn
                    self.player.turn = not self.player.turn

            elif self.ia2 != None:
                self.ia2.evaluate(self.Game.board)
                self.ia1.evaluate(self.Game.board)

                if self.ia1.turn:
                    ia = self.ia1
                    n_ia = 1
                else:
                    ia = self.ia2
                    n_ia = 2
                move = ia.pickMove(self.Game.board)
#                 if (move in self.Game.board.legal_moves):
                 

                self.Game.move(ia,move)
                self.Game.print()
                self.ia1.turn = not self.ia1.turn
                self.ia2.turn = not self.ia2.turn








