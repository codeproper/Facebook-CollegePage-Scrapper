def scrape_urls(num_pages,link_list):
    with open('url.csv', 'w') as csvfile:
        urlwriter = csv.writer(csvfile, delimiter=',',quoting=csv.QUOTE_MINIMAL)
        print("Storing the page url")
        for i in range(num_pages):
            urls=link_list[i].get_attribute('href')
            urlwriter.writerow([urls])
            print("Wrote url"+urls)
        print("Stored "+str(num_pages)+" urls in csv file")

    
