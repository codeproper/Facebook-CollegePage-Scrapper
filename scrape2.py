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

def login(username,password):
    browser.get("https://www.facebook.com")
    print ("Opened facebook...")
    sleep(1)
    browser.find_element_by_id('email').send_keys(username)
    browser.find_element_by_name('pass').send_keys(password)
    browser.find_element_by_id('loginbutton').click()
    print ("Logged in FB...")
    sleep(3)
    print("Opening page of colleges nepal...")
    browser.get("https://www.facebook.com/search/pages/?q=colleges%20nepal&epa=SERP_TAB")
    print("I think its wise to close running browser before starting")
    print("---------------")
    scroll_num=input("How many time to scroll the page[More scroll= More pages]:")
    scroll_num=int(scroll_num)
    for m in range(scroll_num):
         browser.find_element_by_tag_name('html').send_keys(Keys.END)
         sleep(3)
    link_list=browser.find_elements_by_class_name('_32mo')
    num_pages=len(link_list)

    ###Store the page urls in csv file####
    with open('url.csv', 'w') as csvfile:
        urlwriter = csv.writer(csvfile, delimiter=',',quoting=csv.QUOTE_MINIMAL)
        print("Storing the page url")
        for i in range(num_pages):
            urls=link_list[i].get_attribute('href')
            urlwriter.writerow([urls])
            print("Wrote url"+urls)
        print("Stored "+str(num_pages)+" urls in csv file")

    ####Open the csv file to begin scraping####
    with open('url.csv') as csvfile:
        urlreader = csv.reader(csvfile, delimiter=',', quotechar=',',quoting=csv.QUOTE_MINIMAL)
        with open('data.csv', 'w') as File:
            filewriter = csv.writer(File, delimiter=',',quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow(['College Name','College Address','College Contact','College Rating','College Likes','College Follow'])
            for row in urlreader:
                browser.get(row[0])
                sleep(10)
                try:
                    rating=browser.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div[1]/div/div/div[1]/div/a/div/div[2]/div/span[1]').get_attribute("innerText")
                except NoSuchElementException:
		    rating="pattern error"
		try:	
		    likes=browser.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div[1]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div').get_attribute("innerText")
		except NoSuchElementException:
		    likes="pattern error"
		try:
		    follow=browser.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[2]/div').get_attribute("innerText")
                except NoSuchElementException:
		    follow="pattren error"
		try:	
		    address=browser.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div[1]/div/div/div[2]/div/div[2]/div[3]/div/div[2]/div[1]').get_attribute("innerText")
                except NoSuchElementException:    
		    address="pattern error"
		try:	
		    contact=browser.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div[1]/div/div/div[2]/div/div[2]/div[4]/div/div[2]/div').get_attribute("innerText")
                except NoSuchElementException:    
		    contact="pattern error"
		try:
		    clgname=browser.find_element_by_class_name('_64-f').get_attribute("innerText")
                except NoSuchElementException:
                    clgname="pattern error"
                filewriter.writerow([clgname,address,contact,rating,likes,follow])
                print("Data scrapped from "+ clgname +" in csv file")

        ###Removing some repeated rows
        with open('data.csv','r') as orginalfile, open('finaldata.csv','w') as uniquefile:
            uniquefile.writelines(unique_everseen(orginalfile))

    print("Its all done. Checkout the url.csv for the urls and finaldata.csv for scrapped data")

print("A dummy fb id may be suitable for this purpose")
Username=input("Enter the username:")
Userpass=input("Enter the password:")
login(Username,Userpass)
