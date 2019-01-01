from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import csv
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from more_itertools import unique_everseen

# Specifying incognito mode as you launch your browser[OPTIONAL]
option = webdriver.ChromeOptions()
option.add_argument("--incognito")
browser = webdriver.Chrome(executable_path='./chromedriver')

#####username and password can be defined here to automate the process
print("A dummy fb id may be suitable for this purpose")
Username=input("Enter the username:")
Userpass=input("Enter the password:")
##Handles login and page search for list of colleges
link_list,num_pages=findpages(Username,Userpass)
###Store the page urls in csv file####
scrape_urls(link_list,num_pages)
####Open the url.csv file to begin scraping from pages####
datascrape()
print("A dummy fb id may be suitable for this purpose")
Username=input("Enter the username:")
Userpass=input("Enter the password:")
login(Username,Userpass) 
