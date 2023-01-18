from copy import deepcopy

class Node:

    def __init__(self, mancala_board, playerSide):
        self.state = mancala_board
        self.playerSide = playerSide
        self.value = None
    
    def gameOver(self):
        emptyCups_P1, emptyCups_P2 = 0, 0
        for key in self.state.board:
            if key in self.state.PlayerCups[1] and self.state.board[key] == 0:
                emptyCups_P1 += 1
            if key in self.state.PlayerCups[2] and self.state.board[key] == 0:
                emptyCups_P2 += 1
        if emptyCups_P1 == 6:
            Nb_stones = 0
            for key in self.state.PlayerCups[2]:
                    Nb_stones += self.state.board[key]
            self.state.board['1'] += Nb_stones
            return True
        elif emptyCups_P2 == 6:
            Nb_stones = 0
            for key in self.state.PlayerCups[1]:
                    Nb_stones += self.state.board[key]
            self.state.board['2'] += Nb_stones
            return True
        return False
    
    def findWinner(self):
        if self.state.board['1'] > self.state.board['2']:
            return 1
        return 2
    
    def evaluate(self):
        self.value = self.state.board['1'] - self.state.board['2']
        return abs(self.value)


def create_initial_node(game_level):
    level = deepcopy(game_level.level)
    turn = deepcopy(game_level.turn)
    initial_node = Node(level,turn)
    return initial_node
