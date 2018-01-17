#!/usr/bin/env python3

"""Check the weather forecast and text an umbrella reminder if it's raining."""

import requests
import bs4
from twilio.rest import TwilioRestClient

def rain_check():
    """Check weather.gov to see if it is likely to rain today."""
    url = 'https://weather.com/en-GB/'
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    weather_elem = soup.select('#styles-xz0ANuUJ_nowBlurb_17gst')
    weather = weather_elem[0].getText()

    if 'rain' in weather.lower():
        return True


account_sid = 'ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
auth_token  = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
my_number = '+15559998888'
twilo_number = '+15552225678'

def text_myself(message):
    """Use Twilo to text the message argument to your phone."""
    twilo_cli = TwilioRestClient(account_sid, auth_token)
    twilo_cli.messages.create(body=message, from_=twilo_number, to=my_number)


if rain_check():
    text_myself('Remember to take an umbrella.')
