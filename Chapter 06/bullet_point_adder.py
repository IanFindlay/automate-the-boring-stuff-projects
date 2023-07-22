#! python3
# bullet_point_adder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip
text = pyperclip.paste()

# Separate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)):    # loop through all indexes in the "lines" list
    lines[i] = '* ' + lines[i] # add star to each string in "lines" list

text = '\n'.join(lines)    

pyperclip.copy(text)

"""
When this program is run, it replaces the text on the clipboard with text that has stars at the start of each line. 
Now the program is complete, and you can try running it with text copied to the clipboard.
Even if you don’t need to automate this specific task, you might want to automate some other kind of text manipulation, such as removing trailing spaces from the end of lines or converting text to uppercase or lowercase. 
Whatever your needs, you can use the clipboard for input and output.
"""

"""
AlSweigart

You need to run "py.exe -m", which is basically telling python to run the pip module as an app. 
This is just how I'm running pip for python 3.10: py -m pip install pyperclip instead of pip install pyperclip.
They're the same, it's just that I know that on my system py.exe is running Python 3.10, so I don't accidentally run pip for the wrong version of python.
Also, be sure you're running the 3.10 version of IDLE.
"""
