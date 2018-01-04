#!/usr/bin/env python3

"""Takes each column of a spreadsheet and saves it to a seperate text file."""

import re
import openpyxl

print('Enter the absolute path of the spreasheet you wish to split:')
FILE_PATH = input()

PATH_REGEX = re.compile(r'(.*/)(.*)(\.xlsx)$')
PATH_SPLIT = PATH_REGEX.search(FILE_PATH)
PATH = PATH_SPLIT.group(1)
NAME = PATH_SPLIT.group(2)

WB = openpyxl.load_workbook(FILE_PATH)
SHEET = WB.active

col_num = 1
for column in range(1, SHEET.max_column + 1):

    col_data = []
    for cell in range(1, SHEET.max_row + 1):
        if SHEET.cell(row=cell, column=col_num).value != None:
            col_data.append(SHEET.cell(row=cell, column=col_num).value)

    file = open('/' + PATH + 'col-' + str(col_num) + '-' + NAME + '.txt', 'w')
    for line in col_data:
        file.write(line + '\n')
    file.close()

    col_num += 1
