###IMPORTING ADDITIONAL PACKAGES
from selenium import webdriver
from time import sleep
import csv
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from more_itertools import unique_everseen
from bs4 import BeautifulSoup

###IMPORTING SUPPORTING FILES
from .datascrape import scrape_data
from .findpages  import findpages

### Specifying incognito mode as you launch your browser[OPTIONAL]
option = webdriver.ChromeOptions()
option.add_argument("--incognito")
option.add_argument("--headless")
browser = webdriver.Chrome(executable_path='./chromedriver',options=option)

####Store the page links in url.csv file####
findpages()
####Open the url.csv file to begin scraping from pages and store the result in final.csv file####
scrape_data()
print("Its done.Check out the scrapped urls in url.csv and data in finaldata.csv!!")
