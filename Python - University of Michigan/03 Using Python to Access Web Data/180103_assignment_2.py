#Following Links in HTML Using BeautifulSoup

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url - ')
count = int(input('Enter count - '))
position = int(input('Enter position - '))

c = 0
word = []
while c < count:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    tags_ = []
    list_ = []
    for tag in tags:
        list_.append(tag.get('href', None))
        tags_.append(tag)        
    url = list_[position-1]
    word = tags_[position-1].contents[0]
    print("Retrieving - ",url)
    #print("Retrieving - Friends of ",word)
    c = c+1
    
print(word)
