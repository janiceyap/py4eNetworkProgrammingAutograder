# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
position = input('Select Position - ')
iteration = input('How many times to repeat? ')

for count in range(int(iteration)):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all the anchor tags
    tags = soup('a')
    tag = tags[int(position)-1]
    url = tag.get('href', None)
    print(url)
    name = tag.contents[0]

print(name)