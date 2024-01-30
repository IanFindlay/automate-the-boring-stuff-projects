#!/usr/bin/env python3

"""Walk a folder tree and print the names of files above a chosen size."""

import os


folder = input("Enter the absolute path of the folder you'd like to search: ")

threshold = input("Enter the maximum file size that you'd"
                  " like to ignore (in megabytes): ")

for folders, subfolders, filenames in os.walk(folder):

    for filename in filenames:

        size = os.path.getsize(os.path.join(folders, filename))

        if size > int(threshold) * 10 ** 6:   # MB to byte conversion
            print(filename, '| Size = ', size // 10 ** 6, 'MB' '| Path =',
                  os.path.join(folders, filename))
