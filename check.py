from constants import *

__author__ = 'Eric-Nicolas'


def check_victory(board, player):
    # Checking rows
    for x in range(3):
        for y in range(3):
            if board[x][y] != STATES[player]:
                break
        else:
            print()
            return True

    # Checking columns
    for x in range(3):
        for y in range(3):
            if board[y][x] != STATES[player]:
                break
        else:
            print()
            return True

    # Checking diagonals
    for i in range(3):
        if board[i][i] != STATES[player]:
            break
    else:
        return True

    for i in range(3):
        if board[3-i-1][i] != STATES[player]:
            break
    else:
        return True

    return False
