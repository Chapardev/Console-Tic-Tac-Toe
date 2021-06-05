"""
game.py
By Eric-Nicolas
Defines utilitarian functions and the game loop function.
"""

from check import *


def print_board(board):
    print("      0)  1)  2)")
    print("    --------------")
    for i in range(3):
        print(str(i) + ')  |', board[i][0], '|', board[i][1], '|', board[i][2], '|')
        print("    --------------")


def get_value_safely(value, name):
    while value == -1:
        try:
            value = int(input("Entrez le numéro de la " + name + " : "))
            if value < 0 or value > 2:
                raise ValueError
        except ValueError:
            print("Veuillez entrer un nombre compris entre 0 et 2 (inclus).")
            value = -1
    return value


def game_loop(board):
    player = 2
    print("Le joueur 1 possède les X. Le joueur 2 possède les O.")

    while not check_victory(board, player):
        column = row = -1
        if player == 1:
            player = 2
        else:
            player = 1

        print_board(board)

        print("C'est le tour de joueur ", player, '.', sep='')
        column = get_value_safely(column, "colonne")
        row = get_value_safely(row, "ligne")
        print("Vous avez joué la case :", (column, row))

        if board[row][column] == NONE:
            board[row][column] = STATES[player]
        else:
            print("Déjà marqué ici.")

    print_board(board)
    print("Le joueur", player, "a gagné !")
