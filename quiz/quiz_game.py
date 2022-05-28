import random


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
    ans = input('Enter answer YES or NO')
    if ans == 'YES':
        test = 1
        if key_1 == test:
            print("Great!")
        else:
            print("Nooo!")


main()