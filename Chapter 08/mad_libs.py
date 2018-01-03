#!\usr\bin\env python3

"""Read txt file and let the user replace nouns, verbs, adverbs and adjectives.

Usage:
Enter name of any txt file in the cwd and follow prompts to madlib its content
"""

import os
import re

# Prompt for file name in cwd to read and save its content to string variable
file_name = input('Enter the name of the template file you wish to use: ')
lib = open('{0}/{1}.txt'.format(os.getcwd(), file_name))
string = lib.read()

# Find all madlibbable prompt words
replaced = 0
madlib_regex = re.compile(r'(NOUN|VERB|ADVERB|ADJECTIVE)')
matches = madlib_regex.findall(string)

# For each word, prompt for user replacement then replace it in the string
for found in matches:
    sub = input('Enter a ' + found + ': ')
    string = string.replace(found, sub, 1)

print(string)
