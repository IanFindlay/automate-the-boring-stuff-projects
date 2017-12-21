"""Debug Coin Toss Program."""

import random

guess = input('Guess the coin toss! Enter heads or tails: ')
if guess != 'heads' and guess != 'tails':
    raise Exception('Guess must be heads or tails!')

GUESS_CONVERTER = {0: 'heads', 1: 'tails'}
toss = GUESS_CONVERTER[random.randint(0, 1)] # 0 is tails, 1 is heads

if toss == guess:
    print('You got it!')
else:
    guess = input('Nope! Guess again!: ')
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
