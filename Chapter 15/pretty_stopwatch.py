#!/usr/bin/env python3

"""A stopwatch program with a prettier output and pyperclip functionality."""

import time
import pyperclip

# Display the programs instructions.
print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch.'
      'Press Ctrl-c to quit.')

input()
print('Started.')
start_time = time.time()
last_time = start_time
lap_num = 1

# Start tracking the lap times.
try:
    while True:
        input()
        lap_time = round(time.time() - last_time, 2)
        total_time = round(time.time() - start_time, 2)

        lap = 'lap # {} {} ({})'.format((str(lap_num)+ ':').ljust(3),
                                         str(total_time).rjust(5),
                                         str(lap_time).rjust(6))
        print(lap, end='')


        lap_num += 1
        last_time = time.time()   # Reset the last lap time.
        pyperclip.copy(lap)       # Copy latest lap to clipboard.
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    print('\nDone.')
