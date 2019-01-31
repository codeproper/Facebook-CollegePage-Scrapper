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
ts = time.time()
ts = str(ts)

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
    print("HEADLESS IS DISABLED...To enable headless, type python scrape.py --headless to go ")

browser = webdriver.Chrome(executable_path='/bin/chromedriver',options=option)


####Store the page links in url.csv file####
browser.get('https://www.facebook.com/public?query=colleges%20nepal&type=pages&init=dir&nomc=0')
with open('./test/url.csv', 'w') as File:
    filewriter = csv.writer(File, delimiter=',',quoting=csv.QUOTE_MINIMAL)
    scroll_num = 10
    for m in range(scroll_num):
        browser.find_element_by_tag_name('html').send_keys(Keys.END)
        sleep(3)
    links=browser.find_elements_by_class_name('_32mo')
    for i in range(len(links)):
        link=links[i].get_attribute("href")
        filewriter.writerow([link])
print("Done writing urls in url.csv file.. ")

####Open the url.csv file to begin scraping from pages and store the result in data.csv file####

with open('url.csv') as csvfile:
    urlreader = csv.reader(csvfile, delimiter=',', quotechar=',',quoting=csv.QUOTE_MINIMAL)
    with open('./test/data_'+ts+'.csv', 'w') as File:
        filewriter = csv.writer(File, delimiter=',',quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['College Name','College Address','College Contact','College Rating','College Likes','College Follow','College Website','College Type','Open Hours'])
        for row in urlreader:
            browser.get(row[0])
            sleep(3)
            html=browser.page_source
            soup=BeautifulSoup(html,'html.parser')
            try:
                rating=browser.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div[1]/div/div/div[2]/div/div[1]/a/span').get_attribute("innerText")
            except NoSuchElementException:
                rating="Not Found"
            try:
                clgname=browser.find_element_by_class_name('_64-f').get_attribute("innerText")
            except NoSuchElementException:
                clgname="Not Found"
            try:
                address_icon=soup.find("img", {"src" : "https://static.xx.fbcdn.net/rsrc.php/v3/y5/r/b1oBucHUO1S.png"})
                address=address_icon.findNext('div').text
                address = address.replace("Get Directions", "")
            except:
                address="Not Found"
            try:
                like_icon=soup.find("img", {"src" : "https://static.xx.fbcdn.net/rsrc.php/v3/yJ/r/yLtEhZl0QOJ.png"})
                like=like_icon.findNext('div').text
                like=like.replace("people like this", "")
            except:
                like="Not Found"
            try:
                follow_icon=soup.find("img", {"src" : "https://static.xx.fbcdn.net/rsrc.php/v3/y5/r/dsGlZIZMa30.png"})
                follow=follow_icon.findNext('div').text
                follow=follow.replace("people follow this", "")
            except:
                follow="Not Found"
            try:
                contact_icon=soup.find("img", {"src" : "https://static.xx.fbcdn.net/rsrc.php/v3/yz/r/oXiCJHPgn3c.png"})
                contact=contact_icon.findNext('div').text
            except:
                contact="Not Found"
            try:
                website_icon=soup.find("img", {"src" : "https://static.xx.fbcdn.net/rsrc.php/v3/yU/r/ZBnKG6mAW8D.png"})
                website=website_icon.findNext('div').text
            except:
                website="Not Found"
            try:
                clgtype_icon=soup.find("img", {"src" : "https://static.xx.fbcdn.net/rsrc.php/v3/y_/r/On-c9iceH4S.png"})
                clgtype=clgtype_icon.findNext('div').text
            except:
                clgtype="Not Found"
            try:
                opentime_icon=soup.find("img", {"src" : "https://static.xx.fbcdn.net/rsrc.php/v3/yU/r/3qMMM3KK_wt.png"})
                opentime=opentime_icon.findNext('div').text
                opentime = opentime.replace("Hours", "")
                opentime = opentime.replace("Now", "")
                opentime = opentime.replace("Open", "")
                opentime = opentime.replace("Closed", "")
            except:
                opentime="Not Found"

            filewriter.writerow([clgname,address,contact,rating,like,follow,website,clgtype,opentime])
            print("Data scrapped from "+ clgname +" in csv file")
print("Its done.Check out the scrapped urls in url.csv and data in data.csv!!")

print("But wait... There is more...")

sleep(3)

print("Scrapping reviews from the pages..")

sleep(3)

#######Open the url.csv file to begin scraping reviews and store the result in review.csv file####

with open('./test/url.csv') as csvfile:
    urlreader = csv.reader(csvfile, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
    with open('./test/review_'+ts+'.csv', 'w') as File:
        filewriter = csv.writer(File, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['Reviewed College', 'Reviewer Name', 'Review', 'Reviewer Rating', 'Reviewed Date'])
        for row in urlreader:
            review_url = row[0]+"reviews"
            html = urllib.request.urlopen(review_url).read()
            soup = BeautifulSoup(html, "lxml")
            browser.get(review_url)
            review_data = soup.find_all("span", attrs={"class": "fcg"})
            reviews = soup.find_all("p")
            unique_review_data = []
            review_text = []
            temp_review_data = []
            for u in range(len(review_data)):
                rere = review_data[u].text
                temp_review_data.append(rere)
            unique_review_data = list(unique_everseen(temp_review_data))
            for f in range(len(reviews)):
                fefe = reviews[f].text
                review_text.append(fefe)
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
                        print("Wrote reviews from"+review_clg+"in review.csv file")
                        filewriter.writerow([review_clg, reviewer_name, review_text, review_rating, review_date])
                        name_index = name_index+2
                        date_index = date_index+2
                    except:
                        continue
                else:
                    break
print("Finally over. Checkout the csv files in tests folder for scrapped data...")

browser.quit


