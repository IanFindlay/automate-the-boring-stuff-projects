#!/usr/bin/env python3

"""Search for a regex pattern in all txt files in a directory."""

import os
import re

# List all files in directory and filter those that aren't txt files
files = os.listdir(os.getcwd())
txt_files = []

txt_regex = re.compile(r'.txt')

for doc in files:
    if txt_regex.search(doc) is not None:
        txt_files.append(doc)

# Write regex to match
search_regex = re.compile(r'\s?\w*\!')   # Matches all words ending in !

# Open each txt file in turn and if regex triggers print matches to console
for doc in txt_files:
    opened_file = open('{0}/{1}'.format(os.getcwd(), doc))
    contents = opened_file.read()
    string = ''.join(contents)
    found = search_regex.findall(string)
    found_str = ' '.join(found)
    print(found_str)
