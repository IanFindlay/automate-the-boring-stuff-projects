#!/usr/bin/env python3

"""Checks for emailed Magnet links and begins downloading them."""

import time
import subprocess
import imapclient
import pyzmail

def magnet_check():
    """Checks Gmail for Magnet links from verified address and returns them."""
    imap_obj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
    imap_obj.login(BOT_EMAIL, BOT_PASS)
    imap_obj.select_folder('INBOX')
    unique_ids = imap_obj.search(['FROM ' + VERIFIED_EMAIL])

    magnets = []
    if unique_ids:
        for identifier in unique_ids:
            raw_message = imap_obj.fetch([identifier], ['BODY[]', 'FLAGS'])
            message = pyzmail.PyzMessage.factory(raw_message[identifier][b'BODY[]'])
            text = message.text_part.get_payload().decode(message.text_part.charset)

            if VERIFICATION_PASS in text:
                html = message.html_part.get_payload().decode(message.html_part.charset)
                magnets.append(html)

        imap_obj.delete_messages(unique_ids)
        imap_obj.expunge()

    imap_obj.logout()

    return magnets


TORRENT_CLIENT = 'usr/share/applications/qbittorent'
BOT_EMAIL = 'R@bot.com'
BOT_PASS = 'aasjhgf8970875/asfa#'
VERIFIED_EMAIL = 'Allowed@Email.com'
VERIFICATION_PASS = 'verify-this!'

while True:
    magnet_links = magnet_check()
    for link in magnet_links:
        subprocess.Popen(TORRENT_CLIENT + ' ' + link)

    time.sleep(60 * 15)
