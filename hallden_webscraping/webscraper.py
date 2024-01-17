
# Create file using Windows terminal:
    # start notepad <filename>

from selenium import webdriver

url = "https://cryptocurrencyjobs.co/"
browser = webdriver.Chrome()
browser.get(url)

# REMOVED in Selenium 4.3 -> browser.find_element_by_xpath('//*[@id="find-a-job"]').click

# Also not working -> webdriver.find_element("xpath", '//*[@id="find-a-job"]')

browser.find_element("xpath", '//*[@id="find-a-job"]')
# Works! (I think)