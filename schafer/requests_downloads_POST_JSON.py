
#! Request Web Pages, Download Images, POST Data, Read JSON, and More

# Request library allows us to make http requests to get info from websites

# Get info from websites
# Post info
# Download images
# Send authentication information
# Follow redirects

# Request library good for getting info, not good for parsing
# BeautifulSoup, requests.html

# pip install requests

# xkcd comic request

# https://xkcd.com/353

import requests

r = requests.get("https://xkcd.com/353")    # get xkcd page

print(r)    # print response of web page
# gets response object

#* Get Content from Web Page

import requests

r = requests.get("https://xkcd.com/353")

print(dir(r))   # get attributes/methods we can access within response object

# More info on attributes/methods

import requests

r = requests.get("https://xkcd.com/353")

print(help(r))

# Text
# Content of the response, in unicode

import requests

r = requests.get("https://xkcd.com/353")

print(r.text)
# get html of page

# Download Image
# https://imgs.xkcd.com/comics/python.png

r = requests.get("https://imgs.xkcd.com/comics/python.png")

print(r.content)    # for images
# prints out bytes from that image

# Take bytes and save them to file on our machine

r = requests.get("https://imgs.xkcd.com/comics/python.png")

with open('comic.png', 'wb') as f:   # wb -> write bytes
    f.write(r.content)
# writes png to new .png file
    
#* Check if we got a good response
# Write script to monitor website, want to make sure responses coming back alright

r = requests.get("https://imgs.xkcd.com/comics/python.png")

print(r.status_code)
# 200 -> success / 300 -> redirect / 400 -> client error / 500 -> server

# r.ok

r = requests.get("https://imgs.xkcd.com/comics/python.png")

print(r.ok)

#* In-Depth Response Information

r = requests.get("https://imgs.xkcd.com/comics/python.png")

print(r.headers)
# server, content type, dates/times

#* Advanced Features
# httpbin.org
    # Test methods, redirects, etc.

# Get request on route with some url parameters
# get.route
# responds with JSON information

payload = {'page': 2, 'count': 25}  # parameters for our request
r = requests.get("https://httbin.org/get", params=payload)

print(r.text)

# Get specific data/information
# URL

payload = {'page': 2, 'count': 25}  # parameters for our request
r = requests.get("https://httbin.org/get", params=payload)

print(r.url)    # get url

#* POST Data to URL

payload = {'username': 'sky', 'password': 'testing'}  # parameters for our request
r = requests.post("https://httbin.org/post", data=payload)  # changed from params to data, changed get to post

print(r.text)

# JSON responses are common

payload = {'username': 'sky', 'password': 'testing'}  # parameters for our request
r = requests.post("https://httbin.org/post", data=payload)  # changed from params to data, changed get to post

print(r.json())

# Authentication

r = requests.get('https://httpbin.org/basic-auth/sky/testing', auth=('sky', 'testing'))

print(r.text)

# Timeout
# If you don't set timeout, could wait and hang forever
# Add as additional parameter

r = requests.get('https://httbin.org/delay/1', timeout=3)

print(r)