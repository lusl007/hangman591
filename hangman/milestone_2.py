import random

word_list = ['banana', 'apple', 'orange', 'strawberry', 'pineapple']
print(word_list)

# get a random element of the list
word = random.choice(word_list)
print(word)

# user input for a single letter
guess = input('Please input a single letter: ')
print(guess)

# validate user input
# must be a single letter and alphabetical character
if len(guess) == 1 and guess.isalpha():
    print('Good guess!')
else:
    print('Oops! That is not a valid input.')