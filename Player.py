class Player:

    def __init__(self, name: str):
        self.name = name
        self.game = None
        self.turn = None
        self.score = None

    def move(self, move: str):
        pass

    def evaluate(self, board) -> int:
        pass
    
    def check_win_board(self,board):
        try:
           
            n = len(board)
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
                
                if board[condition[0]] == board[condition[1]] == board[condition[2]] == self.sign:
                    bool_ = True

                    return(True)
                    #print("PLAYER ",self.player,"WINS")
            return(bool_)
        except:
            
            return(False)
   