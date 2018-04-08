#Scraping HTML Data with BeautifulSoup

from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error

url = 'http://py4e-data.dr-chuck.net/comments_7543.html'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

sum = 0
#Retrieve all span tags
span_tags = soup('span')
for tag in span_tags:
    #print(tag)
    sum = sum + int(tag.contents[0])

print(sum)
