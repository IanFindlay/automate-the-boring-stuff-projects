#!/usr/bin/env python3

"""Create custom invitations from a guest list with flowery decorations."""

import os
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def create_card(name):
    """Creates a personalised invitation card with the provided name on it."""
    card = Image.new('RGBA', (360, 288), 'white')
    flower = Image.open('flower.png')
    card.paste(flower, (10, 40), flower)
    cut_guide = Image.new('RGBA', (364, 292), 'black')
    cut_guide.paste(card, (2, 2))

    draw_obj = ImageDraw.Draw(cut_guide)
    fonts_folder = 'usr/share/fonts/TTF'
    custom_font = ImageFont.truetype(os.path.join(fonts_folder,
                                                  'DejaVuSerif.ttf'), 72)
    draw_obj.text((120, 100), name, fill='blue', font=custom_font)

    cut_guide.save('{}-invite.png'.format(name))


with open('guests.txt') as f:
    guests = f.readlines()

for guest in guests:
    create_card(guest)

print('All invitations personalised and saved to the CWD - enjoy the dinner.')
