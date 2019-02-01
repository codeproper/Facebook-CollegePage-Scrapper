###IMPORTING PACKAGES
import csv
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep
import urllib.request
from bs4 import BeautifulSoup
from more_itertools import unique_everseen
import argparse
from selenium.common.exceptions import NoSuchElementException
import time
import os


###DEFINE OPTIONS AND PATHS

option = webdriver.ChromeOptions()
option.add_argument("--incognito")
parser = argparse.ArgumentParser()
parser.add_argument('--headless', help='for headless argument', action="store_true")
args = parser.parse_args()
if args.headless:
    print("HEADLESS IS ENABLED.... SCRAPPING IN BACKGROUND...")
    option.add_argument('headless')
else:
    print("HEADLESS IS DISABLED...To enable headless, type python scrape.py --headless ")

###INITIATE CHROME WEBDRIVER###
browser = webdriver.Chrome(executable_path='/bin/chromedriver', options=option)

###FUNCTION BLOCK STARTS ####


def find_current_timestamp():
    timestamp = time.time()
    timestamp = str(timestamp)
    return timestamp


def create_test_folder():
    file_path= r'./test'
    if not os.path.exists(file_path):
        os.makedirs(file_path)
        print("Created a test file...")
    else:
        print("test file already exist...")


def scroll_action(counter, browser): ### Scroll to the bottom of the page
    for m in range(counter):
        browser.find_element_by_tag_name('html').send_keys(Keys.END)
        sleep(3)


def opens_page(browser, url): ### Opens a page url in browser
    browser.get(url)
    sleep(3)


def scrape_page_url(browser): ### Scrape url from the page
    try:
        with open('./test/url.csv', 'w') as url_file:
            filewriter = csv.writer(url_file, delimiter=',',quoting=csv.QUOTE_MINIMAL)
            scroll_num = 15 #more scroll_num makes more pages visible to scrape
            scroll_action(scroll_num, browser)
            url_links = browser.find_elements_by_class_name('_32mo')
            for i in range(len(url_links)):
                url_link = url_links[i].get_attribute("href")
                filewriter.writerow([url_link])
    except:
        print("Error in scrapping url")


def find_clg_data(browser, soup): ### Scrape college information from the pages

    def find_rating(browser):
        try:
            rating = browser.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div[1]/div/div/div[2]/div/div[1]/a/span').get_attribute("innerText")
        except NoSuchElementException:
            rating="Not Found"
        return rating

    def find_clg_name(browser):
        try:
            clgname=browser.find_element_by_class_name('_64-f').get_attribute("innerText")
        except NoSuchElementException:
            clgname="Not Found"
        return clgname

    def find_clg_address(soup):
        try:
            address_icon=soup.find("img", {"src" : "https://static.xx.fbcdn.net/rsrc.php/v3/y5/r/b1oBucHUO1S.png"})
            address=address_icon.findNext('div').text #finds address icon then looks for next sibling for adress
            address = address.replace("Get Directions", "")#remove unwanted text by replacing them with whitespaces
        except:
            address="Not Found"
        return address

    def find_clg_likes(soup):
        try:
            like_icon=soup.find("img", {"src" : "https://static.xx.fbcdn.net/rsrc.php/v3/yJ/r/yLtEhZl0QOJ.png"})
            like=like_icon.findNext('div').text
            like=like.replace("people like this", "")
        except:
            like="Not Found"
        return like

    def find_clg_follows(soup):
            try:
                follow_icon=soup.find("img", {"src" : "https://static.xx.fbcdn.net/rsrc.php/v3/y5/r/dsGlZIZMa30.png"})
                follow=follow_icon.findNext('div').text
                follow=follow.replace("people follow this", "")
            except:
                follow="Not Found"
            return follow

    def find_clg_contact(soup):
            try:
                contact_icon=soup.find("img", {"src" : "https://static.xx.fbcdn.net/rsrc.php/v3/yz/r/oXiCJHPgn3c.png"})
                contact=contact_icon.findNext('div').text
            except:
                contact="Not Found"
            return contact

    def find_clg_website(soup):
            try:
                website_icon=soup.find("img", {"src" : "https://static.xx.fbcdn.net/rsrc.php/v3/yU/r/ZBnKG6mAW8D.png"})
                website=website_icon.findNext('div').text
            except:
                website="Not Found"
            return website

    def find_clg_type(soup):
            try:
                clgtype_icon=soup.find("img", {"src" : "https://static.xx.fbcdn.net/rsrc.php/v3/y_/r/On-c9iceH4S.png"})
                clgtype=clgtype_icon.findNext('div').text
            except:
                clgtype="Not Found"
            return clgtype

    def find_opentime(soup):
            try:
                opentime_icon=soup.find("img", {"src" : "https://static.xx.fbcdn.net/rsrc.php/v3/yU/r/3qMMM3KK_wt.png"})
                opentime=opentime_icon.findNext('div').text
                opentime = opentime.replace("Hours", "")
                opentime = opentime.replace("Now", "")
                opentime = opentime.replace("Open", "")
                opentime = opentime.replace("Closed", "")
            except:
                opentime="Not Found"
            return opentime

    return find_rating(browser), find_clg_name(browser), find_clg_type(soup), find_opentime(soup), find_clg_likes(soup), find_clg_address(soup),find_clg_follows(soup), find_clg_website(soup), find_clg_contact(soup)


def scrape_page_data(browser, timestamp):  ### Write the college information in csv file
    with open('./test/url.csv') as csvfile:
        urlreader = csv.reader(csvfile, delimiter=',', quotechar=',',quoting=csv.QUOTE_MINIMAL)
        with open('./test/clg_data_'+timestamp+'.csv', 'w') as File:
            filewriter = csv.writer(File, delimiter=',',quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow(['College Name','College Address','College Contact','College Rating','College Likes','College Follow','College Website','College Type','Open Hours'])
            for row in urlreader:
                opens_page(browser, row[0])
                page_html = browser.page_source
                soup = BeautifulSoup(page_html, 'html.parser')
                rating, clgname, clgtype, opentime, like,address, follow, website, contact = find_clg_data(browser, soup)
                filewriter.writerow([clgname, address, contact, rating, like, follow, website, clgtype, opentime])
                print("Data scrapped from "+ clgname +" in csv file")


def scrape_review_data(timestamp): ### Scrape and write reviews from in csv file
    with open('./test/url.csv') as csvfile:
        urlreader = csv.reader(csvfile, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
        with open('./test/review_data_'+timestamp+'.csv', 'w') as File:
            filewriter = csv.writer(File, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow(['Reviewed College', 'Reviewer Name', 'Review', 'Reviewer Rating', 'Reviewed Date'])
            for row in urlreader:
                review_url = row[0]+"reviews"
                page_html = urllib.request.urlopen(review_url).read()
                soup = BeautifulSoup(page_html, "html.parser")
                review_data = soup.find_all("span", attrs={"class": "fcg"})
                reviews = soup.find_all("p")
                unique_review_data = []
                review_text = []
                temp_review_data = []
                for u in range(len(review_data)):
                    temp_review_data.append(review_data[u].text)
                unique_review_data = list(unique_everseen(temp_review_data))
                for f in range(len(reviews)):
                    review_text.append(reviews[f].text)
                name_index = 0
                date_index = 1
                for o in range(len(unique_review_data)):
                    if name_index < len(unique_review_data):
                        try:
                            jj = unique_review_data[name_index].split("reviewed")
                            reviewer_name = jj[0]
                            gg = jj[1].split("—")
                            review_clg = gg[0]
                            review_rating = gg[1]
                            review_date = unique_review_data[date_index]
                            try:
                                review_text = reviews[o].text
                            except:
                                review_text = "No Review from this reviewer"
                            print("Reviews collected from"+review_clg)
                            filewriter.writerow([review_clg, reviewer_name, review_text, review_rating, review_date])
                            name_index = name_index+2
                            date_index = date_index+2
                        except:
                            continue
                    else:
                        break


def main(browser):
    create_test_folder()
    opens_page(browser, 'https://www.facebook.com/public?query=colleges%20nepal&type=pages&init=dir&nomc=0')
    sleep(1)
    print("Scrolling and scrapping college page url...")
    scrape_page_url(browser)
    print("Checkout url.csv inside test file to get page url")
    print("Preparing to scrape college information...")
    timestamp = find_current_timestamp()
    scrape_page_data(browser, timestamp)
    print("Finished scrapping. Checkout the clg_data_"+timestamp+".csv inside test folder.")
    sleep(2)
    print("Preparing to scrape the reviews...")
    sleep(3)
    scrape_review_data(timestamp)
    print("Finished scrapping. Checkout the reviews in review_data_"+timestamp+".csv inside test folder")
    browser.quit

#### FUNCTION BLOCK ENDS ####


if __name__ == "__main__":
    main(browser)




























