###IMPORTING ADDITIONAL PACKAGES
from selenium import webdriver
from time import sleep
import csv
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from more_itertools import unique_everseen

###IMPORTING SUPPORTING FILES
from .datascrape import scrape_data
from .findpages  import findpages
from .urlscrape import scrape_urls


### Specifying incognito mode as you launch your browser[OPTIONAL]
option = webdriver.ChromeOptions()
option.add_argument("--incognito")
browser = webdriver.Chrome(executable_path='./chromedriver')

#####username and password can be defined here to automate the process
#Username=""
#Userpass=""

print("A dummy fb id may be suitable for this purpose")
Username=input("Enter the username:")
Userpass=input("Enter the password:")
####Handles login and page search for list of colleges
link_list,num_pages=findpages(Username,Userpass)
####Store the page urls in csv file####
scrape_urls(link_list,num_pages)
####Open the url.csv file to begin scraping from pages and stores the result in final.csv file####
datascrape()
print("Its done.Check out the scrapped urls in url.csv and data in finaldata.csv!!")
