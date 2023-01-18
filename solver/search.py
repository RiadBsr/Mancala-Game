from numpy import inf
from copy import deepcopy

class Search:


    @staticmethod
    def NegaMaxAlphaBetaPruning(game, player, depth, alpha=-inf, beta=inf):
        if game.gameOver() or depth == 1:
            bestValue = game.evaluate()
            bestCup = None
            if not player: # MIN (Human)
                bestValue = -bestValue
            return bestValue, bestCup
        bestValue = -inf
        bestCup = None
        for cup in game.state.possibleMoves(game.playerSide):
            child_game = deepcopy(game)
            child_game.state.doMove(game.playerSide,cup)
            value,_ = Search.NegaMaxAlphaBetaPruning(child_game, not player, depth-1, -beta, -alpha)
            value = -value
            if value > bestValue:
                bestValue = value
                bestCup = cup
            if bestValue > alpha:
                alpha = bestValue
            if beta <= alpha:
                break
        return bestValue, bestCup
    
    @staticmethod
    def MiniMax(game, depth, maximizingPlayer):
        if game.gameOver() or depth == 0:
            return game.evaluate(), None
        if maximizingPlayer:
            bestValue = -inf
            bestCup = None
            for cup in game.state.possibleMoves(game.playerSide):
                child_game = deepcopy(game)
                replay = child_game.state.doMove(game.playerSide, cup)
                if replay:
                    nextPlayer = maximizingPlayer
                else:
                    nextPlayer = not maximizingPlayer
                value,_ = Search.MiniMax(child_game, depth-1, nextPlayer)
                if value > bestValue:
                    bestValue = value
                    bestCup = cup
            return bestValue, bestCup
        else:
            bestValue = inf
            bestCup = None
            for cup in game.state.possibleMoves(game.playerSide):
                child_game = deepcopy(game)
                replay = child_game.state.doMove(game.playerSide, cup)
                if replay:
                    nextPlayer = maximizingPlayer
                else:
                    nextPlayer = not maximizingPlayer
                value,_ = Search.MiniMax(child_game, depth-1, nextPlayer)
                if value < bestValue:
                    bestValue = value
                    bestCup = cup
            return bestValue, bestCup