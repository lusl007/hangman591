import random

class Hangman:
    
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for char in self.word] # If player guesses 'a', the list would be ['a', '_', '_', '_', '_']       # need to enter underscores to it?
        self.num_letters = len(set(self.word)) # number of UNIQUE letters in the word that have not been guessed yet       # list or just integer?
        self.list_of_guesses = [] # list of the guesses that have already been tried

        word_list = ['banana', 'apple', 'orange', 'strawberry', 'pineapple']
        
    
    def check_guess(self, guess):
        guess = guess.lower()
        
        if guess in self.word:
            print(f'Good guess! {guess} is in the word')

            for char in range(len(self.word)):
                if guess == self.word[char]:
                    self.word_guessed == guess
                    print(self.word_guessed) 
            self.num_letters -= 1 

        else:
            self.num_lives == self.num_lives -1
            print('Sorry, {guess} is not in the word')
            print('You have {num_lives} lives left.')        


    def ask_for_input(self):
    
        while True:
            print('Guess a letter')
            guess = input()

            if len(guess) != 1 and guess.isalpha():
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                check_guess(guess)
                guess.append(self.list_of_guesses)
        


            #if len(guess) == 1 and guess.isalpha():
                #break
            #else:
                #print('Invalid letter. Please, enter a single alphabetical character.')

    
    ask_for_input()

