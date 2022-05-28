'''Initial code'''
import sys


def hidden_word(password_check, password):

    for i in range(len(password)):
        if password[i] == password_check:
            return password[i]
    return False

def hangman(counter_err):
    base = '_____'
    pole = '|'
    bar = '----'
    head = 'o'
    body = '|'
    legs = '^'

    if counter_err == 1:
        print(base)
    elif counter_err == 2:
        print('  ' + pole)
        print(base)
    elif counter_err == 3:
        print('  ' + pole)
        print('  ' + pole)
        print(base)
    elif counter_err == 4:
        print('  ' + bar)
        print('  ' + pole)
        print('  ' + pole)
        print(base)
    elif counter_err == 5:
        print('  ' + bar)
        print('  ' + pole + '  ' + head)
        print('  ' + pole)
        print('  ' + pole)
        print(base)
    elif counter_err == 6:
        print('  ' + bar)
        print('  ' + pole + '  ' + head)
        print('  ' + pole + '  ' + body)
        print('  ' + pole)
        print(base)
    elif counter_err == 7:
        print('You lost!')
        print('  ' + bar)
        print('  ' + pole + '  ' + head)
        print('  ' + pole + '  ' + body)
        print('  ' + pole + '  ' + legs)
        print(base)
        sys.exit()
#     # if V1 == 1:
#     #     base = '_____'
#     # elif V1 == 2:
#
#
#     # print('  ' + bar)
#     # print('  ' + pole + '    ' + rope)
#     # print('  ' + pole + '  ')
#     # print('  ' + pole + '  ')
#     # print(base)
def guessed_print(list_guessed):
    list_guessed = sorted(list_guessed)
    print(f'Password has a lenght of: {len(password)}\n')
    print(f' You have guessed positions in password: {list_guessed}')
    if len(list_guessed) == 6:
        print('You won!')
        sys.exit()
def main_P():
    counter_err = 0
    list_guessed = []
    #print(password[1])
    while True:
        password_check = (input('Enter the hidden word or a letter: \n'))

        if len(password_check) > 1:
            password_check = list(password_check)
            if password == password_check:
                print('You won!')
                break
        password_check = str(password_check)

        if hidden_word(password_check,password) != False:
            (print('Nice guess: ', hidden_word(password_check, password)))
            guessed_char = hidden_word(password_check, password)
            idx_char = int(password.index(str(guessed_char)))
            list_guessed.append(idx_char)
            #print(f'Currently guessed password looks like: {password[idx_char]}')
            guessed_print(list_guessed)

        else:
            print('Nope - it is wrong, your hangman is now looking like this:')
            counter_err = counter_err + 1
            hangman(counter_err)


k = ''
password = ['P', 'o', 'l', 'a', 'n', 'd']

main_P()
