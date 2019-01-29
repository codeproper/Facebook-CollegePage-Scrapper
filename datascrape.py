from selenium import webdriver
from time import sleep
import csv
from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException
option = webdriver.ChromeOptions()
option.add_argument("--incognito")
option.add_argument("--headless")
browser = webdriver.Chrome(executable_path='/bin/chromedriver',options=option)

def scrape_data():
    with open('url.csv') as csvfile:
        urlreader = csv.reader(csvfile, delimiter=',', quotechar=',',quoting=csv.QUOTE_MINIMAL)
        with open('data.csv', 'w') as File:
            filewriter = csv.writer(File, delimiter=',',quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow(['College Name','College Address','College Contact','College Rating','College Likes','College Follow','College Website','College Type','Open Hours'])
            for row in urlreader:
                browser.get(row[0])
                sleep(5)
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
                except:
                    address="Not Found"
                try:
                    like_icon=soup.find("img", {"src" : "https://static.xx.fbcdn.net/rsrc.php/v3/yJ/r/yLtEhZl0QOJ.png"})
                    like=like_icon.findNext('div').text
                except:
                    like="Not Found"
                try:
                    follow_icon=soup.find("img", {"src" : "https://static.xx.fbcdn.net/rsrc.php/v3/y5/r/dsGlZIZMa30.png"})
                    follow=follow_icon.findNext('div').text
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
                except:
                    opentime="Not Found"

                filewriter.writerow([clgname,address,contact,rating,like,follow,website,clgtype,opentime])

                print("Data scrapped from "+ clgname +" in csv file")

