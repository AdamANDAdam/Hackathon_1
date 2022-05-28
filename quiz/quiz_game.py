import random

# More questions can be always added
bank_of_questions = {
    'Is water wet?' : 1,
    'Is cat a dog?': 0,
    'Do you need oxygen to breath?': 1,
    'Does the air weigh more than a water?': 0
}

def rand_question():
    rand_sel = random.randint(1,len(bank_of_questions))
    printing(rand_sel)
    return rand_sel

def main():

    k = input('Start game by typing ENTER')
    if k == 'ENTER':
        rand_question()

    else:
        print('Wrong input, Try again')
        main()

def printing(rand_sel):
    key_1 = list(bank_of_questions)[rand_sel]
    val_1 = list(bank_of_questions.values())[rand_sel]
    print(key_1)
    ans = int(input('Enter answer: 1 for YES or 0 for NO'))
    while True:
        if ans == val_1:
            print("Correct")
            break
        elif ans != val_1:
            print("Incorrect!")
            break
        else:
            print("Try again type 1 or 0 onnly!")


main()