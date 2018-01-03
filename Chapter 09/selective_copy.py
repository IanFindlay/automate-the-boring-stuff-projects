#!/usr/bin/env python3

"""Walk through a folder tree and copy all files of a particular extension."""

import os
import shutil


folder = input('Enter the absolute filepath of'
               ' the directory you wish to copy from: ')

extension = input("Enter the extension you'd like to copy: ")

destination = input("Enter destination folder's absolute filepath: ")

for folders, subfolders, filenames in os.walk(folder):

        for filename in filenames:

            if filename.endswith('{}'.format(extension)):
                shutil.copy(os.path.join(folders, filename), destination)

print('Selective copying has finished - all files of', extension,
      'type have been copied from', os.path.basename(folder), 'to',
      os.path.basename(destination))
