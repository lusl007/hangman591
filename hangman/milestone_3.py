import random

word_list = ['banana', 'apple', 'orange', 'strawberry', 'pineapple']
word = random.choice(word_list)
print(word.upper())

def check_guess(guess):
    guess = guess.lower()
    
    if guess in word:
        print(f'Good guess! {guess} is in the word') # print letter in the correct place of the word on different line
    else:
        print(f'Sorry, {guess} is not in the word. Try again.')


def ask_for_input():
    
    while True:
        print('Guess a letter')
        guess = input()

        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print('Invalid letter. Please, enter a single alphabetical character.')

    check_guess(guess)


ask_for_input()


