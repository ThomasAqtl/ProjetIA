#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 16:33:12 2021

@author: macmac
"""

import cmd
import MorpionGame

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

            self.ia1 = IA('IA1')
            self.ia1.turn = False

        elif mode == 'IAvsIA':
            self.ia1 = IA('IA1')
            self.ia1.turn = True

            self.ia2 = IA('IA2')
            self.ia2.turn = False
    
     def do_start(self, arg):
        """
        Start a new game.\n 
        If you are in IA vs IA mode, the game will run automatically.\n
        """
        if self.Game != None:
            print('A game is already running')
        else:
            self.Game = MorpionGame()
            ##############
            #print what ??
            ##############
            self.Game.print()
            
            
            
     def do_move(self, arg):
         """
         Plays a move if a game has started. \n 
         Moves are written as the number of case
         - Use : move <move>
         - Ex : move 5
         """
         if self.Game == None:
             print('You need to start a game !')
         else:
             if self.player != None:
                 if self.player.turn == True:
                     print("Which case number do you choose ?")
                     self.Game.displayChoices()
                     try:
                         self.Game.move(arg)
                         self.player.turn = not self.player.turn
                         ##############
                         #How do we know where to catch the exception ????
                         ##############
                     except:
                             print('Your input is incorrect.')
                 else:
                     print('It is not your turn.')
           
            
     # called after each command. 
     # checks if game is ended
     def postcmd(self, line, stop):
         pass
    
        
        

