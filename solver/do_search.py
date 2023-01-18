from solver.search import Search
from solver.node import create_initial_node

def do_search(game_level):
    initial_node = create_initial_node(game_level)
    depth = game_level.game.search_depth
    # bestValue, bestCup = Search.NegaMaxAlphaBetaPruning(initial_node, True, depth)
    bestValue, bestCup = Search.MiniMax(initial_node, depth, True)
    return (bestValue, bestCup)
    
