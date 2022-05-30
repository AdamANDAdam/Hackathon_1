import random

deck_base = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10 , 'Jack', 'Queen', 'King', 'Joker']
def deck_perp():
    '''
    We prepare the deck (for now only two decks but we could make all 4, it is a purposeful complication.
    '''
    print("Welcome to the deck war!")
    deck_hearts = []
    deck_spades = []
    deck_base = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10 , 'Jack', 'Queen', 'King', 'Joker']
    for i in deck_base:
        deck_hearts.append(str(i) + ' hearts')
        deck_spades.append(str(i) + ' spades')
    return deck_hearts, deck_spades

def game_play1(deck_hearts, deck_spades):
    #print(deck_spades)
    #print(deck_hearts)
    k = 0
    while k < 10:
        selected_card1 = random.choice(deck_hearts)
        selected_card2 = random.choice(deck_spades)
        print(selected_card1)
        print(selected_card2)
        selected_card_index1 = deck_hearts.index(selected_card1)
        selected_card_index2 = deck_spades.index(selected_card2)
        # print(selected_card_index1)
        # print(selected_card_index2)
        if selected_card_index1 > selected_card_index2:
            print('Hearts won')
        elif selected_card_index2 > selected_card_index1:
            print('Spades won')
        else:
            print('Draw')
            k -= 1
        k += 1
def game_play2(deck_hearts, deck_spades):

    new_deck_1 = []
    new_deck_2 = []
    for i in deck_base:
        if i == 'Ace':
            i = 1
        elif i == 'Jack':
            i = 11
        elif i == 'Queen':
            i = 12
        elif i == 'King':
            i = 13
        elif i == 'Joker':
            i = 14
        new_deck_1.append(i)
        new_deck_2.append(i)
    iteration = 0
    while iteration < 10:
        selected1 = random.choice(new_deck_1)
        selected2 = random.choice(new_deck_2)
        quick_patch1 = 'Hearts'
        quick_patch2 = 'Spades'
        if selected1 == 1:
            print(quick_patch1 + ' Ace')
        elif selected1 == 11:
            print(quick_patch1 + ' Jack')
        elif selected1 == 12:
            print(quick_patch1 + ' Queen')
        elif selected1 == 13:
            print(quick_patch1 + ' King')
        elif selected1 == 14:
            print(quick_patch1 + ' Joker')
        else:
            print(quick_patch1 + ' '  + str(selected1))
        if selected2 == 1:
            print(quick_patch2 + ' Ace')
        elif selected2 == 11:
            print(quick_patch2 + ' Jack')
        elif selected2 == 12:
            print(quick_patch2 + ' Queen')
        elif selected2 == 13:
            print(quick_patch2 + ' King')
        elif selected2 == 14:
            print(quick_patch2 + ' Joker')
        else:
            print(quick_patch2 + ' ' + str(selected2))

        new_deck_1.remove(selected1)
        new_deck_2.remove(selected2)
        if selected1 > selected2:

            print('Hearts won!')
        elif selected1 < selected2:
            print('Spades won!')
        else:
            print('Draw!')
            iteration -= 1
        iteration+=1

def main():

    deck_hearts, deck_spades = deck_perp()
    print(deck_perp.__doc__)
    what_type = input('Remove randomly chosen card from the deck? YES or NO')
    if what_type == 'YES':
        game_play1(deck_hearts, deck_spades)
    elif what_type == 'NO':
        game_play2(deck_hearts,deck_spades)


main()