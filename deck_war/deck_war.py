import random
import sys

deck_base = ['Ace', 2, 3, 4, 5, 6, 7, 8 , 9, 10, 'Jack', 'Queen', 'King', 'Joker']
deck_clubs = []
deck_diamonds = []
deck_hearts = []
deck_spades = []

def deck_prep():
    for i in deck_base:
        deck_spades.append(str(i) + ' spades')
        deck_hearts.append(str(i) + ' hearts')
    print(deck_spades)
    print(deck_hearts)
def type1():
    local_counter = 0
    while local_counter < 10:
        selected1 = random.choice(deck_spades)
        selected2 = random.choice(deck_hearts)
        index1 = deck_spades.index(selected1)
        index2 = deck_hearts.index(selected2)

        if index2 > index1:
            print(selected1, ' ')
            print(selected2, ' ')
            print('Hearts won!')
        elif index1 < index2:
            print(selected1, ' ')
            print(selected2, ' ')
            print('Spades won!')
        local_counter += 1
    sys.exit()
def type2():
    loc_counter = 0
    while loc_counter < 10:
        selected1 = random.choice(deck_spades)
        selected2 = random.choice(deck_hearts)
        index1 = deck_spades.index(selected1)
        index2 = deck_hearts.index(selected2)
        print(index1, index2)
        if index2 ==

        loc_counter += 1
    sys.exit()

def main():
    deck_prep()
    print('Deck war')
    play = input('After fight: RETURN or DISCARD?')

    while True:


        if play == 'RETURN':
            type1()
        elif play == 'DISCARD':
            type2()
        else:
            print("Type RETURN or DISCARD, try again")
            break
main()