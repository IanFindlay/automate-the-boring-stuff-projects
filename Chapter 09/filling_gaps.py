#!/usr/bin/env python3

"""Fix gaps in files with a chosen prefix in a specified folder."""

import os
import re
import shutil

folder = input("Enter the absolute path of the folder you'd like to search: ")

prefix = input("Enter the prefix (up to the numbering) of the files whose"
               "numbering you'd like to check: ")

# Regex to find the chosen sequentially named files
ordered_regex = re.compile(r'({0})(\d*)(.*)(\..*)'.format(prefix))

found = []       # Keep track of numbering of files with chosen prefix

# Filewalk to find files with chosen prefix
for folders, subfolders, filenames in os.walk(folder):
    for filename in filenames:

        if ordered_regex.search(filename) is not None:

            # Determine length of numbering digits (for later naming)
            num_length = int(len(ordered_regex.search(filename).group(2)))

            # Find extension of files (for later naming)
            extension = ordered_regex.search(filename).group(4)

            # Number of files with chosen prefix
            found.append(ordered_regex.search(filename).group(2))

    ordered = sorted([int(x) for x in found])

# Loop to check for corret numbering based on amount of files found
for number in range(1, len(found) + 1):

    # Calculate amount of 0's to prepend to reconstruct original format
    zeroes = '0' * (num_length - len(str(number)))

    # Recreate path of what should be the next file
    current_file = '{}/{}{}{}{}'.format(folder, prefix, zeroes,
                                        number, extension)

    # Check if the file exists
    if os.path.exists(current_file) is False:
        # Find numbering of actual next file and format path
        next_num = ordered[number - 1]
        next_zeroes = '0' * (num_length - len(str(next_num)))
        next_file = (folder + '/' + prefix + str(next_zeroes)
                     + str(next_num) + extension)

        # Rename actual to desired through shutil move
        shutil.move(next_file, current_file)

print('File numbering has been fixed.')
