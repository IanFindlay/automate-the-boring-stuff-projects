#!/usr/bin/env python3

"""A Regex version of the Strip Function."""

import re


def strip(text, remove=''):
    """Perform string.strip-like functions but using regexes."""
    # Removes whitespace from either end of the string
    if remove == '':
        space_regex = re.compile(r'^(\s*)(.*)(\s)*$')
        trimmed = space_regex.search(text)
        return trimmed.group(2)

    # Removes character inputted as 2nd argument from ends of string
    else:
        remove_start = re.compile(r'^([%s]+)' % remove)
        remove_end = re.compile(r'([%s]+)$' % remove)
        start = remove_start.search(text)
        end = remove_end.search(text)
        # Allows function to strip even if only one side has remove characters
        try:
            return text[len(start.group()):len(text) - len(end.group())]
        except AttributeError:
            error_avoid = remove + text + remove
            return strip(error_avoid, remove)


# Get function arguments from user then print stripped string
user_text = input('Enter the text you would like stripped here: ')
user_remove = input('Enter the character you want stripped here'
                    ' (Removes Space as Default): ')

print(strip(user_text, user_remove))
