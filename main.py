import os
from ChessConsole import *
#import MorpionConsole


if __name__ == "__main__":
    
    # ========================== GAME CHOICE ==========================
    print('Chose your game (pick number)')
    print('1. Chess')
    print('2. Tic-Tac-Toe')

    choice = input()
    while not (choice == '1' or choice == '2'):
        print('Type 1 or 2 to chose your game')
        choice = input()

    if choice == '1':
        chosen_game = 'chess'
    elif choice == '2':
        chosen_game = 'tic-tac-toe'

    print('You picked ' + chosen_game + '.\n')

    # ========================== MODE CHOICE ==========================
    print('Chose your game mode (pick number)')
    print('1. You play vs AI')
    print('2. AI vs AI (spectate)')

    mode_choice = input()
    while not (mode_choice != '1' or mode_choice != '2'):
        print('Type 1 or 2 to chose your game mode.')
        mode_choice = input()

    # ================== GAME AND MODE ATTRIBUTION ====================
    if chosen_game == 'chess':
        if mode_choice == '1':
            console = ChessConsole('HvsIA')
        elif mode_choice == '2':
            console = ChessConsole('IAvsIA')
    elif chosen_game == 'tic-tac-toe':
        if mode_choice == '1':
            console = MorpionConsole('HvsIA')
        elif mode_choice == '2':
            console = MorpionConsole('IAvsIA')
        

    # ================== LAUNCH CHOSEN GAME CONSOLE ===================
    os.system('clear') #clear terminal
    console.cmdloop()
    