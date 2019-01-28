###IMPORTING SUPPORTING FILES
from datascrape import scrape_data
from findpages  import findpages

####Store the page links in url.csv file####
findpages()
####Open the url.csv file to begin scraping from pages and store the result in final.csv file####
scrape_data()
print("Its done.Check out the scrapped urls in url.csv and data in data.csv!!")
