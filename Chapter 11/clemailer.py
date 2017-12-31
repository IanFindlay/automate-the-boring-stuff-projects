#!/usr/bin/env/ python3

"""Write and send emails from the Command Line."""

import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

RECIPIENT = sys.argv[1]
SUBJECT = sys.argv[2]
MESSAGE = sys.argv[3]

# Username Login
browser = webdriver.Firefox()
browser.get('https://accounts.google.com/signin/v2/identifier?service=mail')
id_elem = browser.find_element_by_name('identifier')
id_elem.send_keys('email@gmail.com')
id_elem.send_keys(Keys.ENTER)
time.sleep(3)

# Password Login
pass_elem = browser.find_element_by_name('password')
pass_elem.send_keys('password')
pass_elem.send_keys(Keys.ENTER)
time.sleep(5)

# Click Compose
compose_elem = browser.find_element_by_class_name('z0')
compose_elem.click()
time.sleep(5)

# Recipient
to_elem = browser.find_element_by_name('to')
to_elem.send_keys(RECIPIENT)

# Subject
subject_elem = browser.find_element_by_name('subjectbox')
subject_elem.send_keys(SUBJECT)

# Messge
message_elem = browser.find_element_by_id(':cf')
message_elem.send_keys(MESSAGE)

# Click Send
send_elem = browser.find_element_by_id(':b4')
send_elem.click()
