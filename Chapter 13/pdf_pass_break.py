#!/usr/bin/env python3

"""Carries out a brute-force password attack on an encrypted PDF."""

import PyPDF2

print('Enter the absolute directory of the PDF you wish to break:')
FILE = input()

with open('/home/finners/Downloads/dictionary.txt') as f:
    WORDS = f.readlines()

    PDF_READER = PyPDF2.PdfFileReader(open(FILE, 'rb'))

    for word in WORDS:
        word = word.strip()
        lower = word.lower()
        upper = word.upper()
        if PDF_READER.decrypt(lower) == 1:
            print('Password = ' + lower)
            break
        elif PDF_READER.decrypt(upper) == 1:
            print('Password = ' + upper)
            break
