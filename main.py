"""Console Tic Tac Toe"""

__author__ = 'Eric-Nicolas'

STATES = " XO"
ROWS = COLUMNS = 3


def print_board(board):
    print("\t0)\t1)\t2)")
    for i in range(COLUMNS):
        print(str(i) + ')  |', board[i][0], '|', board[i][1], '|', board[i][2], '|')
        print("    --------------")


def check_victory(board):
    return False


def game_loop(board):
    player = 1
    column = row = -1

    print("Le joueur 1 possède les X. Le joueur 2 possède les O.")

    while not check_victory(board):
        print_board(board)
        print("C'est le tour de joueur", player)
        column = int(input("Entrez le numéro de la colonne : "))
        row = int(input("Entrez le numéro de la ligne : "))
        print("Vous avez joué la case :", (column, row))

        board[column][row] = STATES[player]

        if player == 1:
            player = 2
        else:
            player = 1


def main():
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    game_loop(board)


if __name__ == '__main__':
    main()
