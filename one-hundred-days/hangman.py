#Hangman Game

import random

#Create a list of words
word_list = [
  "british", "suave", "integrity", "accent", "evil", "genius", "Downton"
]

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#Draw the hangman

HANGMAN_PICS = [
  '''
    +---+
    |   |
        |
        |
        |
        |
        |
        |

=========''', '''
    +---+
    |   |
    O   |
        |
        |
        |
        |
        |   
=========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
        |
        |
=========''', '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
        |
        |
=========''', '''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
        |
        |
=========''', '''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
        |
        |
=========''', '''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
        |
        |
========='''
]

#Create a variable called 'display' with the same number of letters as the chosen_word.
#This will be the variable that displays the blanks at the start of each round.
display = []
for i in range(word_length):
  display += "_"
print(display)

while not end_of_game:
  print(HANGMAN_PICS[6 - lives])
  guess = input("Guess a letter: ").lower()

  #Loop through each position in the chosen_word;
  for position in range(word_length):
    letter = chosen_word[position]
    #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
    if letter == guess:
      display[position] = letter
  print(display)

  #If guess is not a letter in the chosen_word,
  #Then reduce 'lives' by 1.
  #If lives goes down to 0 then the game should stop and it should print "You lose."
  if guess not in chosen_word:
    lives -= 1
    if lives == 0:
      end_of_game = True
      print()
      print("You lose!")

  #Join all the elements in the list and turn it into a String.
  print(f"{' '.join(display)}")

  #Check if user has got all letters.
  if "_" not in display:
    end_of_game = True
    print()
    print("You win!")

