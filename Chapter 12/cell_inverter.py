#!/usr/bin/env python3

"""Invert the rows and columns of a spreadsheet."""

import re
import openpyxl

print('Enter the absolute path to the spreadsheet file:')
FILE_PATH = input()

PATH_REGEX = re.compile(r'(.*/)(.*)(\.xlsx)$')
PATH_SPLIT = PATH_REGEX.search(FILE_PATH)
PATH = PATH_SPLIT.group(1)
NAME = PATH_SPLIT.group(2)

wb = openpyxl.load_workbook(FILE_PATH)
sheet = wb.active

# Make nested list of spreadsheet data (row by row)
rows = []
MAX_ROW = sheet.max_row
MAX_COLUMN = sheet.max_column
for row in range(1, MAX_ROW + 1):
    data = []
    for cell in range(1, MAX_COLUMN + 1):
        cell_value = sheet.cell(row=row, column=cell).value
        data.append(cell_value)
    rows.append(data)

# Open new spreadsheet and populate with above data but inverted
wb = openpyxl.Workbook()
sheet = wb.active

column_num = 1
for row in rows:
    row_num = 1
    for cell in row:
        sheet.cell(row=row_num, column=column_num).value = cell
        row_num += 1
    column_num += 1

wb.save(PATH + NAME + '(inverted).xlsx')
print('Spreadsheet data inverted and saved to ' + NAME + '(inverted).xlsx.')
