"""
check.py
By Eric-Nicolas
Defines functions that checks if one of the player won.
"""

from constants import *


def check_rows(board, player):
    for x in range(3):
        for y in range(3):
            if board[x][y] != STATES[player]:
                break
        else:
            return True
    return False


def check_columns(board, player):
    for x in range(3):
        for y in range(3):
            if board[y][x] != STATES[player]:
                break
        else:
            return True
    return False


def check_diagonals(board, player):
    for i in range(3):
        if board[i][i] != STATES[player]:
            break
    else:
        return True

    for i in range(3):
        if board[3 - i - 1][i] != STATES[player]:
            break
    else:
        return True
    return False


def check_victory(board, player):
    if check_rows(board, player) or check_columns(board, player) or check_diagonals(board, player):
        return True
    return False
