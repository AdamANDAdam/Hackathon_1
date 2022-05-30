import random
import sys


def score_check(row1, row2, row3):

    if row1.count("O") == 3 or row2.count("O") == 3 or row3.count("O") == 3:
        print("Player with circles won!")
        sys.exit()
    elif row1[1] == row2[1] == row3[1] == 'O' or row1[2] == row2[2] == row3[2] == 'O' or row1[3] == row2[3] == row3[3] == 'O' or row1[1] == row2[2] == row3[3] == 'O' :
        print("Player with circles won!")
        sys.exit()
    elif row1.count("X") == 3 or row2.count("X") == 3 or row3.count("X") == 3:
        print("Player with crosses won!")
        sys.exit()
    elif row1[1] == row2[1] == row3[1] == 'X' or row1[2] == row2[2] == row3[2] == 'X' or row1[3] == row2[3] == row3[3] == 'X' or row1[1] == row2[2] == row3[3] == 'X':
        print("Player with crosses won!")
        sys.exit()

def game_play1(choice1, row_1, row_2, row_3, title, played_counter):
    if choice1 == 'A':
        row_1.pop(1)
        if played_counter % 2 == 0:
            row_1.insert(1,'X')
        else:
            row_1.insert(1, 'O')
        print(*title, '\n', row_1, '\n', row_2, '\n', row_3)
    if choice1 == 'B':
        row_1.pop(2)
        if played_counter % 2 == 0:
            row_1.insert(2,'X')
        else:
            row_1.insert(2, 'O')
        print(*title, '\n', row_1, '\n', row_2, '\n', row_3)
    if choice1 == 'C':
        row_1.pop(3)
        if played_counter % 2 == 0:
            row_1.insert(3,'X')
        else:
            row_1.insert(3, 'O')
        print(*title, '\n', row_1, '\n', row_2, '\n', row_3)
    if choice1 == 'D':
        row_2.pop(1)
        if played_counter % 2 == 0:
            row_2.insert(1,'X')
        else:
            row_2.insert(1, 'O')
        print(*title, '\n', row_1, '\n', row_2, '\n', row_3)
    if choice1 == 'E':
        row_2.pop(2)
        if played_counter % 2 == 0:
            row_2.insert(2,'X')
        else:
            row_2.insert(2, 'O')
        print(*title, '\n', row_1, '\n', row_2, '\n', row_3)
    if choice1 == 'F':
        row_2.pop(3)
        if played_counter % 2 == 0:
            row_2.insert(3,'X')
        else:
            row_2.insert(3, 'O')
        print(*title, '\n', row_1, '\n', row_2, '\n', row_3)
    if choice1 == 'G':
        row_3.pop(1)
        if played_counter % 2 == 0:
            row_3.insert(1, 'X')
        else:
            row_3.insert(1, 'O')
        print(*title, '\n', row_1, '\n', row_2, '\n', row_3)
    if choice1 == 'H':
        row_3.pop(2)
        if played_counter % 2 == 0:
            row_3.insert(2,'X')
        else:
            row_3.insert(2, 'O')
        print(*title, '\n', row_1, '\n', row_2, '\n', row_3)
    if choice1 == 'I':
        row_3.pop(3)
        if played_counter % 2 == 0:
            row_3.insert(3,'X')
        else:
            row_3.insert(3, 'O')
        print(*title, '\n', row_1, '\n', row_2, '\n', row_3)
# def game_play2(choice2, row_1, row_2, row_3, title):
    return row_1, row_2, row_3

def main():

    player1, player2 = input("Enter two names use space: ").split()
    print("O is {} and X is {}".format(player1, player2))
    print('The board looks as follows:')
    played_counter=0
    title = ['        C1', '    C2', '   C3']
    row_1 = ['R1', 'A', 'B', 'C']
    row_2 = ['R2', 'D', 'E', 'F']
    row_3 = ['R3', 'G', 'H', 'I']
    print(*title, '\n', row_1, '\n', row_2, '\n', row_3)
    PC_or_USER = input('Do you want to play with PC or with a user? YES or NO')

    while True:
        if PC_or_USER == 'NO':
            choice_1 = input(f'Player {player1} "O" circle - type position: ')
            played_counter += 1
            game_play1(choice_1, row_1, row_2, row_3, title, played_counter)
            choice_2 = input(f'Player {player2} "X" cross - type position: ')
            played_counter += 1
            game_play1(choice_2, row_1, row_2, row_3, title, played_counter)
            # game_play2(choice_1, row_1, row_2, row_3, title)
            score_check(row_1,row_2,row_3)
        elif PC_or_USER == 'YES':
            choice_1 = input(f'Player {player1} "O" circle - type position: ')
            played_counter += 1

            poll = ["A", "B","C","D","E","F","G","H","I"]
            poll.remove(choice_1)

            game_play1(choice_1, row_1, row_2, row_3, title, played_counter)

            choice_2 = random.choice(poll)
            played_counter += 1
            game_play1(choice_2, row_1, row_2, row_3, title, played_counter)
            poll.remove(choice_2)
            # game_play2(choice_1, row_1, row_2, row_3, title)
            score_check(row_1, row_2, row_3)
            import time
            for x in range(0, 5):
                b = "Loading" + "." * x
                print(b, end="\r")
                time.sleep(1)
        else:
            print("In this case, good bye")
            break
main()