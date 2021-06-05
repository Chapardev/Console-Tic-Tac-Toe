"""Console Tic Tac Toe"""

__author__ = 'Eric-Nicolas'


STATES = " XO"
DASHES = 13


def print_line():
    for _ in range(DASHES):
        print('-', end='')


def show_table(x, y):
    print('\t', end='')
    for i in range(x):
        print(' ' + str(i) + ') ', end=' ')
    print()
    for i in range(y):
        print('\t', end='')
        print_line()
        print('\n' + str(i) + ')  ', end='')
        for j in range(DASHES):
            if j % 4 == 0:
                print('|', end='')
            else:
                print(' ', end='')
        print()
    print('\t', end='')
    print_line()


def main():
    print("Hello World!")
    show_table(3, 3)


if __name__ == '__main__':
    main()
