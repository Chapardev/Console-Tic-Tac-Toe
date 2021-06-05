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


def game_loop():
    pass


def main():
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    print_board(board)


if __name__ == '__main__':
    main()
