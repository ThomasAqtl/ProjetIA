import cmd
from Chessgame import *

intro1 = 'Type <help> to list available commands.\n'
intro2 = 'Type <help><command> to see details about given command.\n'
intro3 = 'Type <start> to begin a game.\n'

class ChessConsole(cmd.Cmd):

    #intro = 'Type <help> to list available commands. \n Type <start> to begin a game.'

    def __init__(self, mode: str):
        cmd.Cmd.__init__(self)
        self.player = None
        self.ia1 = None
        self.ia2 = None

        self.prompt = 'Chess > '
        self.completekey = 'tab'
        self.intro = intro1+intro2+intro3
        self.Game = None

        if mode == 'pvIA':
            self.player = Player('Player 1')
            self.player.turn = True

            self.ia1 = IA('IA1')
            self.ia1.turn = False

        elif mode == 'IAvIA':
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
            self.Game = Chessgame()
            self.Game.print()

    def do_move(self, arg):
        """
        Plays a move if a game has started. \n 
        Moves are written concatenating start and end case.
        - Use : move <move>
        - Ex : move e2e4 
        """
        if self.Game == None:
            print('You need to start a game !')
        else:
            if self.player != None:
                if self.player.turn == True:
                    try:
                        self.Game.move(arg)
                        self.player.turn = not self.player.turn
                    except:
                        print('Your input is incorrect.')
                else:
                    print('It is not your turn.')

    # called after each command. 
    # checks if game is ended
    def postcmd(self, line, stop):
        if self.Game != None:
            if self.Game.board.is_game_over():
                if self.Game.board.is_insufficient_material():
                    print('Game over : draw by insufficient material.')
                    return True
                if self.Game.board.is_stalemate():
                    print('Game over : draw by stalemate.')
                    return True
                if self.Game.board.is_checkmate():
                    if self.player != None:
                        if self.player.turn == True:
                            print('Game over : defeat by checkmate')
                        else:
                            print('Game over : win by checkmate')
                        return True
                    else:
                        if self.ia1 != None and self.ia2 != None:
                            if self.ia1.turn:
                                print('IA2 won !')
                            elif self.ia2.turn:
                                print('IA1 won !')
                if self.Game.board.is_repetition():
                    print('Game over : draw by repetition')
                    return True
            
            # score refresh
            if self.player != None:
                self.player.evaluate(self.Game.board)
                self.ia1.evaluate(self.Game.board)