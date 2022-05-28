import random

start_syl = []
mid_syl = []
end_syl = []
choice = ['the Greatest', 'the Strongest', 'the Funniest', 'the Smallest', 'the Awesome']
story_verbs = ['suspect', 'delay', 'empty','match', 'arrange','arrest', 'encourage','observe','include']
places = ['toilet', 'room', 'office', 'village', 'city', 'town', 'hospital']

def name_gen(number_names):
    for i in range(0, number_names):
        generated = str(random.choice(start_syl)+random.choice(mid_syl)+random.choice(end_syl))
        print(generated.title() + f' {random.randint(1,5)}' + ' '+random.choice(choice)+' went to '+random.choice(places)+' to '+random.choice(story_verbs))

def main():

    consonants = "bcdfghjklmnpqrstvwxyz"
    consonants = list(consonants)

    for x in consonants:
        start_vowel = x + 'a'
        mid_vowel = x + 'e'
        end_vowel = 'o' + x
        start_syl.append(start_vowel)
        mid_syl.append(mid_vowel)
        end_syl.append(end_vowel)
    number_names = int(input('Random name generator, enter how many names you want to generate:'))

    while True:
        if number_names == 0:
            print('Try again')
        elif number_names >= 0:
            name_gen(number_names)
            break
main()
