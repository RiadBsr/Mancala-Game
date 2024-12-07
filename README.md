# Mancala Game with AI Opponent

This project is a Python implementation of the Mancala game with an AI opponent. The game is built using Pygame for the graphical interface and includes various states and components to manage the game flow. The AI opponent uses search algorithms to determine the best moves.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Game Components](#game-components)
- [Game States](#game-states)
- [AI Opponent](#ai-opponent)
  - [Minimax Algorithm](#minimax-algorithm)
  - [Negamax Algorithm with Alpha-Beta Pruning](#negamax-algorithm-with-alpha-beta-pruning)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/RiadBsr/Mancala-Game.git
    cd mancala-ai
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

To start the game, run the following command:
```sh
python [game.py](http://_vscodecontentref_/1)
```

## Game Components

- **Button**: A class to create interactive buttons in the game.
- **ArrowButton**: A specialized button with arrow graphics.
- **ButtonCup**: A button representing a cup in the Mancala board.
- **GameGrid**: A class to draw the game grid.

## Game States

- **State**: The base class for different game states.
- **Splash**: The splash screen state.
- **MainMenu**: The main menu state.
- **SettingsMenu**: The settings menu state.
- **GameLevel**: The game level state for two-player mode.
- **GameLevelAi**: The game level state for playing against the AI.
- **GameWon**: The state displayed when the game is won.

## AI Opponent

The AI opponent in this game uses search algorithms to determine the best moves. The two main algorithms implemented are Minimax and Negamax with Alpha-Beta Pruning.

### Minimax Algorithm

The Minimax algorithm is a recursive algorithm used for decision-making in game theory. It provides an optimal move for the player assuming that the opponent also plays optimally. The algorithm works by simulating all possible moves and their outcomes, and then choosing the move that maximizes the player's minimum gain.

The implementation of the Minimax algorithm can be found in the `Search` class in the file `solver/search.py`:
```py
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
            value, _ = Search.MiniMax(child_game, depth-1, nextPlayer)
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
            value, _ = Search.MiniMax(child_game, depth-1, nextPlayer)
            if value < bestValue:
                bestValue = value
                bestCup = cup
        return bestValue, bestCup
```
### Negamax Algorithm with Alpha-Beta Pruning

The Negamax algorithm is a variant of the Minimax algorithm that simplifies the implementation by taking advantage of the zero-sum property of two-player games. Alpha-Beta Pruning is an optimization technique for the Negamax algorithm that reduces the number of nodes evaluated in the search tree.

The implementation of the Negamax algorithm with Alpha-Beta Pruning can be found in the `Search` class in the file `solver/search.py`:
```py
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
        child_game.state.doMove(game.playerSide, cup)
        value, _ = Search.NegaMaxAlphaBetaPruning(child_game, not player, depth-1, -beta, -alpha)
        value = -value
        if value > bestValue:
            bestValue = value
            bestCup = cup
        if bestValue > alpha:
            alpha = bestValue
        if beta <= alpha:
            break
    return bestValue, bestCup
```
## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
