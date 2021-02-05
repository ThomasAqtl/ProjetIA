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