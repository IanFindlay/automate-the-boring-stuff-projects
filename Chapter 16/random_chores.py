#!/usr/bin/env python3

"""Assign randomised chores to people and email them their appointed task."""

import random
import smtplib

def get_chore(email, last_chore):
    """Randomly selects a chore that isn't the 'last_chore the person had."""
    chore_list = chores[:]
    try:
        chore_list.remove(last_chore)
    except ValueError:
        pass
    if chore_list:
        new_chore = random.choice(chore_list)
        chore_assignments[email] = new_chore
        chores.remove(new_chore)
    else:
        print('Reshuffling as a chore would have to have been repeated.')


def send_chore(email, chosen_chore):
    """Emails the address with chore details."""
    smtp_obj.sendmail('Example@Email.com', email, 'Subject: This Weeks Chore.'
                      '/n You have been randomly assigned ' + chosen_chore
                      + '. You will not receive this chore next time.')


with open('last_chores.txt') as f:
    last_chores = f.readlines()

EMAILS = ['Recipient1@email.com', 'Recipient2@email.com',
          'Recipient3@email.com', 'Recipient4@email.com']

chore_assignments = {}

while len(chore_assignments) < 4:
    chores = ['dishes', 'bathroom', 'vacuum', 'walk dog']
    get_chore(EMAILS[0], last_chores[0].strip())
    get_chore(EMAILS[1], last_chores[1].strip())
    get_chore(EMAILS[2], last_chores[2].strip())
    get_chore(EMAILS[3], last_chores[3].strip())


smtp_obj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
smtp_obj.ehlo()
smtp_obj.login('Example@Email.com', 'Password')

for address, chore in chore_assignments.items():
    send_chore(address, chore)

smtp_obj.quit()

with open('last_chores.txt', 'w') as f:
    f.write(chore_assignments[EMAILS[0]] + '\n')
    f.write(chore_assignments[EMAILS[1]] + '\n')
    f.write(chore_assignments[EMAILS[2]] + '\n')
    f.write(chore_assignments[EMAILS[3]] + '\n')

print('Everyone has been emailed their latest chore - Program will now close.')
