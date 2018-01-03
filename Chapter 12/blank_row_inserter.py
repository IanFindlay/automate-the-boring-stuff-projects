#!/usr/bin/env python3

"""Replicate a spreadsheet in CWD but with N blank rows inserted at chosen place.

Usage: blank_row_inserter.py takes 3 arguments
<Name> - Name of the spreadsheet to add blank rows to
<Start> - The row to start inserting the blank lines
<Number> - The number of blank lines to insert

e.g. python blank_row_inserter.py test.xlsx 3 2
     Would Insert 2 blank rows starting at row 3 into a copy of 'test.xlxs'
"""

import sys
import openpyxl

NAME = sys.argv[1]
B_START = int(sys.argv[2])
B_LENGTH = int(sys.argv[3])

WB = openpyxl.load_workbook(NAME)
SHEET = WB.active

# Read the data from spreadsheet and get list of row data lists
print('Reading spreadsheet data...')
rows = []
MAX_ROW = SHEET.max_row
MAX_COLUMN = SHEET.max_column
for row in range(1, MAX_ROW + 1):
    data = []
    for cell in range(1, MAX_COLUMN + 1):
        cell_value = SHEET.cell(row=row, column=cell).value
        data.append(cell_value)
    rows.append(data)

#print(sheet_data)

WB = openpyxl.Workbook()
SHEET = WB.active

# Write rows prior to into new spreadsheet with blank lines inserted
print('Inserting blanks...')
for row in range(1, B_START):
    for cell in range(1, MAX_COLUMN + 1):
        SHEET.cell(row=row, column=cell).value = rows[row - 1][cell - 1]

# Write remaining rows after the blank gap
for row in range(B_START + B_LENGTH, MAX_ROW + B_LENGTH + 1):
    for cell in range(1, MAX_COLUMN + 1):
        SHEET.cell(row=row, column=cell).value = rows[row - B_LENGTH - 1][cell - 1]

WB.save('blanked-' + NAME)

print("A copy of the spreadsheet with blanks inserted has been saved"
      " as 'blanked-spreadsheet_name]'. It can be found in the same"
      " directory as the original.")
