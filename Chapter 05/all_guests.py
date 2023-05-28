allGuests = {
  'Alice': {
    'apples': 5,
    'pretzels': 12
  },
  'Bob': {
    'ham sandwiches': 3,
    'apples': 2
  },
  'Carol': {
    'cups': 3,
    'apple pies': 1
  }
}

# Count the total number of guests coming to the party in allGuests
def totalGuests(allGuests, guests):
    for k, v in allGuests.items():
        guests = guests + 1
    return guests

print('Total number of guests coming to the party: ' + str(totalGuests(allGuests, 0)))
print('')

def totalBrought(guests, item):
  numBrought = 0
  for k, v in guests.items():
    numBrought = numBrought + v.get(item, 0)
  return numBrought


print('Number of things being brought:')
print(' - Apples         ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups           ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes          ' + str(totalBrought(allGuests, 'cakes')))
print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apple Pies     ' + str(totalBrought(allGuests, 'apple pies')))