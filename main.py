"""
main.py
By Eric-Nicolas
Is the program's point of entry.
"""

from game import *


def main():
    board = [[NONE, NONE, NONE], [NONE, NONE, NONE], [NONE, NONE, NONE]]
    game_loop(board)


if __name__ == '__main__':
    main()
