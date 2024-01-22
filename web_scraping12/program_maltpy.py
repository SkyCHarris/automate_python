
#! Web Scraping

# Web Scraping is the term for using a program to download and process content from the web
# Google runs web scraping programs to index web pages for its search engine

# Modules for web scraping:

# webbrowser -> Built-in, opens browser to a specific page
# requests -> Downloads files and web pages from the internet
# bs4 -> Parses HTML
# selenium -> Launches and controls a web browser. Able to fill in forms and simulate mouse clicks

#! Project: mapIt.py with the webbrowser Module

# webbrowser module's open() function can launch a new browser to a specified URL

import webbrowser

webbrowser.open('http://inventwithpython.com/')

# Web browser tab opens to the URL
# This is about all it can do

# Tedious to copy a street addres to the clipboard and bring up a map of it on Google Maps
# Instead, write a script to launch the map in your browser using the contents of your clipboard

# Program:

# 1. Get street address from the command line arguments or clipboard
# 2. Open web browser to Google Maps page for the address

# Code should:

# 1. Read the command line arguments from sys.argv
# 2. Read the clipboard contents
# 3. Call the webbrowser.open() function to open the web browser

#? Step 1: Figure out the URL