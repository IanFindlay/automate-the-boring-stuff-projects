#!/usr/bin/env python3

"""Sends out a message to a selected group of Google Hangouts contacts."""

import time
import pyautogui


def auto_message(name, message):
    """Searches for friend on Google Hangouts and messages them."""
    print("Make sure the Google Hangout 'Conversations' page is visible and "
          "your cursor is not currently on the page.")
    time.sleep(3)

    search_bar = pyautogui.locateOnScreen('search.png')
    pyautogui.click(search_bar)
    pyautogui.typewrite(name)
    time.sleep(1)

    online_select = pyautogui.locateOnScreen('online-friend.png')
    if online_select is None:
        print('Friend not found or currently offline.')
        return
    else:
        pyautogui.doubleClick(online_select)

    attempts = 3
    while attempts > 0:
        message_box = pyautogui.locateOnScreen('message.png')
        pyautogui.click(message_box)
        pyautogui.typewrite(message)

        # If it can no longer be found it is because the message was entered.
        if pyautogui.locateOnScreen('message.png') is None:
            pyautogui.press('enter')
            pyautogui.press('esc')
            print('Message sent to {}'.format(name))
            break
        else:
            if attempts == 1:
                print('Unable to send message to {}.'.format(name))
                pyautogui.press('esc')

            else:
                print('Sending message to {} failed. Another {} attempts will '
                      'be made before moving on.'.format(name, attempts))

            attempts -= 1


print('Enter the contacts you wish to send a message to (e.g. Bob, Bill):')
send_to = input().split(',')

print('Enter the message you wish to send out to them:')
to_send = input()

for contact in send_to:
    user = contact.strip()
    auto_message(user, to_send)
