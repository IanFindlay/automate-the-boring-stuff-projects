#!/usr/bin/env python3

"""Downloads any web comics that have been updated since it was last run."""

import os
import datetime
import requests
import bs4


def check_xkcd(last_url):
    """Download all XKCD comics released after the given URL."""
    url = 'https://xkcd.com'
    # Get latest comics URL with comic number for comparison/file update
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    prev_link = soup.select('a[rel="prev"]')[0]
    href = prev_link.get('href')
    number = href.strip('/')
    url = 'https://xkcd.com/{}/'.format(str(int(number) + 1))
    latest_url = url

    if url == last_url:
        print('No new XKCD comics have been published since last check')
    else:
        while url != last_url:
            res = requests.get(url)
            res.raise_for_status()

            soup = bs4.BeautifulSoup(res.text, 'lxml')

            comic_elem = soup.select('#comic img')
            if comic_elem == []:
                print('could not find comic image.')
            else:
                try:
                    comic_url = 'https:' + comic_elem[0].get('src')
                    # Download the image.
                    print('Downloading image {}'.format(comic_url))
                    res = requests.get(comic_url)
                    res.raise_for_status()
                except requests.exceptions.MissingSchema:
                    # Skip this comic.
                    prev_link = soup.select('a[rel="prev"]')[0]
                    url = 'https://xkcd.com' + prev_link.get('href')
                    continue

                # Save the image to ./xkcd.
                image = open(os.path.join('Web Comics', os.path.basename(comic_url)), 'wb')
                for chunk in res.iter_content(100000):
                    image.write(chunk)
                image.close()

            # Get the Prev button's url.
            prev_link = soup.select('a[rel="prev"]')[0]
            url = 'https://xkcd.com' + prev_link.get('href')

    return latest_url


def check_smbc(last_url):
    """Download all SMBC comics released after the given URL."""
    url = 'https://www.smbc-comics.com/'
    # Get latest comics actual name for comparison/update
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    name_elem = soup.select('input[value]')
    home_url = name_elem[0].get('value')
    url_check = 'https://www.' + home_url[7:]
    latest_url = url_check

    if url_check == last_url:
        print('No new SMBC comics have been published since last check')
    else:
        while url != last_url:
            res = requests.get(url)
            res.raise_for_status()
            soup = bs4.BeautifulSoup(res.text, 'lxml')
            comic_elem = soup.select('#cc-comic')

            if comic_elem == []:
                print('Could not find comic image.')
            else:
                try:
                    comic_url = ('https://www.smbc-comics.com/'
                                 + comic_elem[0].get('src'))
                    print('Downloading image {}'.format(comic_url))
                    res = requests.get(comic_url)
                    res.raise_for_status()
                except requests.exceptions.MissingSchema:
                    prev_link = soup.select('a[rel="prev"]')[0]
                    url = prev_link
                    continue

                image = open(os.path.join('Web Comics', os.path.basename(comic_url)), 'wb')
                for chunk in res.iter_content(100000):
                    image.write(chunk)
                image.close()

                prev_link = soup.select('a[rel="prev"]')[0]
                url = prev_link.get('href')

    return latest_url


os.makedirs('Web Comics', exist_ok=True)

# File containing latest comic URL checked
with open('/Web Comics/last_downloaded.txt') as f:
    info = f.read().splitlines()
    date = info[0]
    last_xkcd = info[1]
    last_smbc = info[2]

date = datetime.datetime.now().strftime('%H:%M:%S on %d/%m/%Y')
print('Last comic check = ' + date)

# Run functions and rewrite file with 'new' URLs
xkcd_url = check_xkcd(last_xkcd)
smbc_url = check_smbc(last_smbc)

with open('/Web Comics/last_downloaded.txt', 'w') as f:
    f.write(date + '\n')
    f.write(xkcd_url + '\n')
    f.write(smbc_url + '\n')

print('Finished.')
