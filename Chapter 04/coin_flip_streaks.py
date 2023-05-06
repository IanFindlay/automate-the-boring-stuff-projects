import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    coin_flips = []
    for i in range(100):
        if random.randint(0, 1) == 0:
            coin_flips.append('H')
        else:
            coin_flips.append('T')

    # Code that checks if there is a streak of 6 heads or tails in a row.
    for i in range(len(coin_flips) - 6):    # -6 because we are checking 6 values at a time
        if coin_flips[i] == coin_flips[i + 1] == coin_flips[i + 2] == coin_flips[i + 3] == coin_flips[i + 4] == coin_flips[i + 5]:
            numberOfStreaks += 1
            break

print('Chance of streak: %s%%' % (numberOfStreaks / 100))
