"""Prints a nicely aligned table from a list of strings."""

table_data = [['apples', 'oranges', 'cherries', 'banana'],
			  ['Alice', 'Bob', 'Carol', 'David'],
			  ['dogs', 'cats', 'moose', 'goose']]


def print_table(table):
	"""Print a formatted, properly aligned table version of a list."""
	# Create list with zeroes equal to the length of input list
	col_widths = [0] * len(table)

    # Finds longest word in each sublists and sets col_width[x] to value
	for item in range(len(table)):
		for word in table[item]:
			if col_widths[item] < len(word):
				col_widths[item] = len(word)
	
	# Finds the longest sublist in the table
	length = 0
	for i in range(len(table)):
		if length < len(table[i]):
			length = len(table[i])

    # Iterates over lists taking nth element from each
    # and printing it with the other nth subitems
    # right aligned according to the corresponding col_width value

	for word in range(length):
		for item in range(len(table)):
			try:
				print(table[item][word].rjust(col_widths[item]), end=' ')
			except IndexError:
				print(' '.rjust(col_widths[item]), end =' ')
		print()


print_table(table_data)
