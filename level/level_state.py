import random

class LevelState:
    def __init__(self):
        self.robot_position = (0, 0)
        self.board = {
            'A': 4,'B': 4,'C': 4,'D': 4,'E': 4,'F': 4,'1': 0,
            'L': 4,'K': 4,'J': 4,'I': 4,'H': 4,'G': 4,'2': 0,
        }
        self.PlayerCups = {1:['A','B','C','D','E','F'],2:['G','H','I','J','K','L']}
    
    def possibleMoves(self,Player):
        cups = []
        for key in self.board:
            if self.board[key] != 0 and key in self.PlayerCups[Player]:
                cups.append(key)
        return cups

    def opposite_player(self, Player):
        if Player == 1:
            return 2
        return 1

    def doMove(self,Player,cup=None): # Player: 1 or 2
        if cup == None:
            cup = random.choice(self.possibleMoves(Player))
        Nb_stones  = self.board[cup]
        self.board[cup] = 0     
        last_cup = None
        put = False
        while Nb_stones > 0:
            for key in self.board:
                if put and key != str(self.opposite_player(Player)):
                    self.board[key] += 1
                    Nb_stones -= 1
                    if Nb_stones == 0:
                        last_cup = key
                        break
                if key == cup:
                    put = True

        if last_cup in self.PlayerCups[Player] and self.board[last_cup] == 1:
            self.board[last_cup] = 0
            opposite_cup = self.PlayerCups[self.opposite_player(Player)][self.PlayerCups[Player].index(last_cup)]
            self.board[str(Player)] += self.board[opposite_cup] + 1
            self.board[opposite_cup] = 0
        
        return last_cup == str(Player) # Returns if replay or not

