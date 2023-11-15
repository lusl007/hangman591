import random

class Hangman:
    
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_' * len(self.word)] # If player guesses 'a', the list would be ['a', '_', '_', '_', '_']
        self.num_letters = len(set(self.word)) # number of UNIQUE letters in the word that have not been guessed yet
        self.list_of_guesses = [] # list of the guesses that have already been tried
        
    
    def check_guess(self, guess):
        guess = guess.lower()
        
        if guess in self.word:
            print(f'Good guess! {guess} is in the word')

            for char in range(len(self.word)):
                if guess == self.word[char]: 
                    self.word_guessed[char] = guess 
                    print(char)
                    print(self.word_guessed) 
            
            self.num_letters -= 1 
            print(self.num_letters)
        else:
            self.num_lives -= 1
            print(f'Sorry, {guess} is not in the word')
            print(f'You have {self.num_lives} lives left.')        


    def ask_for_input(self):
        print(self.word) #comment this out in the end
        
        while True:
            print('Guess a letter')
            guess = input()

            if len(guess) == 1 and guess.isalpha():
                if guess in self.list_of_guesses:
                    print('You already tried that letter!')
                else:
                    self.check_guess(guess)
                    self.list_of_guesses.append(guess)
                    break
            else:
                print('Invalid letter. Please, enter a single alphabetical character.')

    
def play_game(word_list):
    game = Hangman(word_list)

    while True:
        if game.num_lives == 0:
            print('You lost!')
            print(f'The word was {game.word}')
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        elif game.num_letters == 0:
            print('Congratulations. You won the game!')
            break

word_list = ['banana'] #, 'apple', 'orange', 'strawberry', 'pineapple']
play_game(word_list)

