from selenium import webdriver
from time import sleep
import csv
import urllib.request
from bs4 import BeautifulSoup
from  more_itertools import unique_everseen
import re
#from selenium.common.exceptions import NoSuchElementException
option = webdriver.ChromeOptions()
option.add_argument("--incognito")
#option.add_argument("--headless")
browser = webdriver.Chrome(executable_path='/bin/chromedriver', options=option)

def scrape_data():

    with open('url.csv') as csvfile:
        urlreader = csv.reader(csvfile, delimiter=',', quotechar=',',quoting=csv.QUOTE_MINIMAL)
        for row in urlreader:
            review_url=row[0]+"reviews"
            html= urllib.request.urlopen(review_url).read()
            soup= BeautifulSoup(html,"lxml")

            browser.get(review_url)
            #data=browser.find_elements_by_id('fwb')#.get_attribute("href")
            data= soup.find_all("span", attrs={"class":"fcg"})
            reviews= soup.find_all("p")
            text_data=[]
            review_data=[]

            for u in range(len(data)):
                rere= data[u].text
                text_data.append(rere)
            data1=list(unique_everseen(text_data))
            for i in range(len(reviews)):
                fefe = reviews[i].text
                review_data.append(fefe)
            a= 0
            b= 1
            for f in range(len(data1)):

                if a<len(data1):
                    try:
                        jj = data1[a].split("reviewed")
                        reviewer_name=jj[0]
                        gg=jj[1].split("—")
                        review_clg=gg[0]
                        review_rating=gg[1]

                        review_date = data1[b]
                        print(reviewer_name)
                        print(review_clg)
                        print(review_rating)
                        print(review_date)
                        a=a+2
                        b=b+2
                    except:
                        continue
                else:
                    break


            for o in range(len(review_data)):
                print(review_data[o])


scrape_data()

