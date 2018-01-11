#!/usr/bin/env python3

"""Download jpg/png images from Imgur that match a user's search term(s)."""

import os
import requests
import bs4

def image_downloader(extension):
    """Search for and download all images of the argument type from Imgur."""
    url = 'http://imgur.com/search?q=' + search + ' ext:' + extension
    os.makedirs('/home/finners/Downloads/imgur', exist_ok=True)

    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    image_elem = soup.select('.post > .image-list-link img')

    for i, image in enumerate(image_elem):
        # Convert image URL from thumbnail size to fullsize version
        image_url_s = 'https:' + image_elem[i].get('src')
        image_url = image_url_s[: -5] + '.' + extension

        print('Downloading image {}'.format(image_url))
        res = requests.get(image_url)
        res.raise_for_status()
        image_file = open(os.path.join('/home/finners/Downloads/imgur',
                                        os.path.basename(image_url)), 'wb')
        for chunk in res.iter_content(1000000):
            image_file.write(chunk)
        image_file.close()

    return len(image_elem)


search = input('Enter desired search term(s): ')
downloaded = image_downloader('jpg') + image_downloader('png')

if downloaded == 0:
    print('No images found.')

else:
    print('All ' + str(downloaded) + ' files successfully downloaded.')
