from copy import deepcopy

ROBOT ='R'
WALL = 'O'
SPACE = ' '
TARGET = 'S'
BINGO = '*'
BOX = 'B'
DOT='.'
DEADLOCK = 'D'

def findDeadlocks(board):
    deadlocks = deepcopy(
        board
    )  # the new board where we're going to add 'D' where there is deadlock spot
    coords = []  # here we save the coordinates of the deadlocks

    # detecter les deadlock en coin
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == SPACE:
                if (
                    (board[i + 1][j] == WALL and board[i][j + 1] == WALL)
                    or (board[i - 1][j] == WALL and board[i][j - 1] == WALL)
                    or (board[i + 1][j] == WALL and board[i][j - 1] == WALL)
                    or (board[i - 1][j] == WALL and board[i][j + 1] == WALL)
                ):
                    # if the "SPACE" (floor) is in a corner then put 'D' and save its coordinates
                    deadlocks[i][j] = "D"
                    coords.append([i, j])

    # detecter les deadlock en ligne
    remaining = deepcopy(coords)
    for coord1 in coords:
        remaining.remove(coord1)
        for (
            coord2
        ) in (
            remaining
        ):  # pour chaque 2 coins d'une même ligne ou d'une même colonne on verifie si un mur continue les relie

            # Cas de la même ligne
            if coord1[0] == coord2[0]:
                if coord1[1] > coord2[1]:
                    tmp = coord2
                    coord2 = coord1
                    coord1 = tmp
                if (
                    all(
                        e == WALL
                        for e in board[coord1[0] + 1][coord1[1] + 1 : coord2[1]]
                    )
                    or all(
                        e == WALL
                        for e in board[coord1[0] - 1][coord1[1] + 1 : coord2[1]]
                    )
                ) and TARGET not in board[coord1[0]][coord1[1] : coord2[1]]:
                    for i in range(coord1[1] + 1, coord2[1]):
                        if board[coord1[0]][i] == SPACE:
                            deadlocks[coord1[0]][i] = "D"

            # Cas de la même colonne
            if coord1[1] == coord2[1]:
                if coord1[0] > coord2[0]:
                    tmp = coord2
                    coord2 = coord1
                    coord1 = tmp
                if (
                    all(
                        e == WALL
                        for e in [
                            row[coord1[1] + 1]
                            for row in board[coord1[0] + 1 : coord2[0]]
                        ]
                    )
                    or all(
                        e == WALL
                        for e in [
                            row[coord1[1] - 1]
                            for row in board[coord1[0] + 1 : coord2[0]]
                        ]
                    )
                ) and TARGET not in [
                    row[coord1[1]] for row in board[coord1[0] + 1 : coord2[0]]
                ]:
                    for i in range(coord1[0] + 1, coord2[0]):
                        if board[i][coord1[1]] == SPACE:
                            deadlocks[i][coord1[1]] = "D"

    return deadlocks


# This function returns True if the dynamic board is in a deadlock state else it returns False
def checkDeadlock(robot_block, deadlockMap):
    for i in range(len(robot_block)):
        for j in range(len(robot_block[0])):
            if robot_block[i][j] == BOX and deadlockMap[i][j] == DEADLOCK:
                return True
    return False
