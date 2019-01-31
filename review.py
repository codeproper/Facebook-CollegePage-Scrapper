from selenium import webdriver
from time import sleep
import csv
import urllib.request
from bs4 import BeautifulSoup
from  more_itertools import unique_everseen
option = webdriver.ChromeOptions()
option.add_argument("--incognito")
#option.add_argument("--headless")
browser = webdriver.Chrome(executable_path='/bin/chromedriver', options=option)

def review_data():

    with open('url.csv') as csvfile:
        urlreader = csv.reader(csvfile, delimiter=',', quotechar=',',quoting=csv.QUOTE_MINIMAL)
        for row in urlreader:
            review_url=row[0]+"reviews"
            html= urllib.request.urlopen(review_url).read()
            soup= BeautifulSoup(html,"lxml")

            browser.get(review_url)
            #data=browser.find_elements_by_id('fwb')#.get_attribute("href")
            review_data= soup.find_all("span", attrs={"class":"fcg"})
            reviews= soup.find_all("p")
            unique_review_data=[]
            review_text=[]
            temp_review_data=[]

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
                            review_text = "No Review"
                        print(reviewer_name)
                        print(review_clg)
                        print(review_rating)
                        print(review_date)
                        print(review_text)
                        name_index = name_index+2
                        date_index = date_index+2
                    except:
                        continue
                else:
                    break

review_data()

