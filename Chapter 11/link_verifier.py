#! /usr/bin/env Python

"""Download all linked pages from a given URL and note any 404's."""

import requests
import bs4

URL = input('Enter the URL that you would like to verify the links for: ')
RES = requests.get(URL)
RES.raise_for_status()

SOUP = bs4.BeautifulSoup(RES.text, 'html.parser')
LINKS = SOUP.select('a')
fof = []   # List of links that lead to a 404 page

for link in LINKS:
    try:
        unmade_url = link['href']
        if unmade_url.startswith('http'):
            to_check = unmade_url

        elif unmade_url.startswith('//'):
            to_check = 'https:' + unmade_url

        elif unmade_url.startswith('#'):
            to_check = URL + unmade_url

        result = requests.get(to_check)

        if result.status_code == 404:
            fof.append(to_check)

    except:
        pass

print('Links processed these ' + str(len(fof)) + ' returned error 404:')
print('\n'.join(fof))
