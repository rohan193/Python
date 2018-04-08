#Author : Rohan M. Nanaware
#Date C.: 25th Oct 2017
#Date M.: 28th Oct 2017
#Purpose: Using python to access web data - code documentation

#Regular expressions
import re

text = "A Quick  1 Brown Fox 10 Inside A Box 20"
y = re.findall("[0-9]+", text)
print(y)
y = re.findall("[AEIOU]+", text)
print(y)

x = "From: the entire wordbase: "
y = re.findall("^F.+:", x)#greedy
print(y)
y = re.findall("^F.+?:", x)#non - greedy : Starts with F, any number 
#                           of characters, repeats one or more times,
#                           non-greedy, ends with colon
print(y)

x = "From abc.xyz@lmn.com sent you a mail "
y = re.findall("\S+@\S+", x)#Starts with non blank, repeats one or more times,
#                           Followed by @, ends with non-blank, repeats 1 or more times
print(y)
y = re.findall("^From (\S+@\S+)", x)#Match the whole  pattern but return pattern only in the paranthesis
print(y)
y = re.findall("^From .*@([^ ]*)", x)#Starts with From, followed by space, followed by
#                                   any character repeating zero or more times, 
#                                   followed by @, text  starting with anythng, 
#                                   followed by space
print(y)

#Week2 assignment

#Finding Numbers in a Haystack
#In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.

#test file - regex_sum_42.txt

import re

fname = input("Enter file name : ")
file = open(fname)#Enter - regex_sum_42.txt
sum_ = 0
for line in file:
    #print(line)
    regoutput = re.findall("[0-9]+",line)
    if len(regoutput) < 1: 
        continue
    else:
        for text in regoutput:
            sum_ = sum_ + int(text)

print(sum_)

################################ Week 3 #####################################
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org',80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()

#Assignment
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()

################################ Week 4 #####################################

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())

#Use beautiful soup to parse websites
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter url - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

#Eg. Retrieve all the anchor tags
a_tags = soup('a')
for tag in a_tags:
    print(tag.get('href', None))

#Assignment 1 - Scraping HTML Data with BeautifulSoup
#http://py4e-data.dr-chuck.net/comments_7543.html

from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error

url = 'http://py4e-data.dr-chuck.net/comments_42.html'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

sum = 0
#Retrieve all span tags
span_tags = soup('span')
for tag in span_tags:
    #print(tag)
    sum = sum + int(tag.contents[0])

print(sum)

#Assignment 2 - Following Links in HTML Using BeautifulSoup
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

################################# Week 5 #####################################

'''
The act of going from internal representation on one computer out to a interchange
format is called serialization.

       Serialization                        Deserialization
Python data >>> Serialized data format(XML, Json) >>> Java hashmap, etc.

eXtensible Markup Language(XML)

https://en.wikipedia.org/wiki/XML_schema

XSD XML Schema:

XSD strcuture has complex elements(element that can have children), simple elements, sequence

XSD constraints include number of occurences, data type in the node(datetime, string, numeric)

'''
import xml.etree.ElementTree as ET

data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
     +1 734 303 4456
   </phone>
   <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))


import xml.etree.ElementTree as ET

input = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count:', len(lst))

for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get("x"))


#Assignment 1:

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter location: ')#http://py4e-data.dr-chuck.net/comments_42.xml
print('Retrieving ',url)
data = urllib.request.urlopen(url).read()
data = ET.fromstring(data)

To make the code a little simpler, you can use an XPath selector string to look through the entire tree of XML
for any tag named 'comment' with the following line of code:

lst = data.findall('.//comment')
sum_ = 0

for node in lst:
    name = node.find('name').text
    count = int(node.find('count').text)
    sum_ = sum_ + count

print(sum_)

################################# Week 6 #####################################

'''

APIs

Google maps api
https://developers.google.com/maps/
https://developers.google.com/maps/documentation/geocoding/start

'''

import urllib.request, urllib.parse, urllib.error
import json

 Note that Google is increasingly requiring keys
 for this API
serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    url = serviceurl + urllib.parse.urlencode(
        {'address': address})

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)

#Assignment 1

import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter url :')
print('Retrieving ',url)
data = urllib.request.urlopen(url)
data = data.read().decode()

js = json.loads(data)

sum_ = 0
for item in js["comments"]:
    sum_ = sum_ + int(item["count"])

print(sum_)

#Assignment 2:

import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://py4e-data.dr-chuck.net/geojson?'

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    url = serviceurl + urllib.parse.urlencode(
        {'address': address})

    print('Retrieving', url)##Open this url in browser to view structure of the json
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(js['results'][0]['place_id'])

