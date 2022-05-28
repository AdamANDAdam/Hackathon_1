import random

def game_play(choice1,choice2, row_1, row_2, row_3, title):
    if choice1 == 'A':
        row_1.pop(1)
        row_1.insert(1,'O')
        print(*title, '\n', row_1, '\n', row_2, '\n', row_3)
    if choice1 == 'B':
        row_1.pop(2)
        row_1.insert(2,'O')
        print(*title, '\n', row_1, '\n', row_2, '\n', row_3)
    if choice1 == 'C':
        row_1.pop(2)
        row_1.insert(2,'O')
        print(*title, '\n', row_1, '\n', row_2, '\n', row_3)


def main():

    player1, player2 = input("Enter two names use space: ").split()
    print("O is {} and X is {}".format(player1, player2))
    print('The board looks as follows:')
    title = ['        C1', '    C2', '   C3']
    row_1 = ['R1', 'A', 'B', 'C']
    row_2 = ['R2', 'D', 'E', 'F']
    row_3 = ['R3', 'G', 'H', 'I']
    print(*title, '\n', row_1, '\n', row_2, '\n', row_3)

    choice_1 = input('O type position: ')
    choice_2 = input('O type position: ')
    game_play(choice_1,choice_2, row_1, row_2, row_3, title)
main()