def scrape_data():
    with open('url.csv') as csvfile:
        urlreader = csv.reader(csvfile, delimiter=',', quotechar=',',quoting=csv.QUOTE_MINIMAL)
        with open('data.csv', 'w') as File:
            filewriter = csv.writer(File, delimiter=',',quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow(['College Name','College Address','College Contact','College Rating','College Likes','College Follow'])
            for row in urlreader:
                browser.get(row[0])
                sleep(10)
                try:
                    rating=browser.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div[1]/div/div/div[2]/div/div[1]/a/span').get_attribute("innerText")
                except NoSuchElementException:
                    rating="pattern error"
                try:
                    likes=browser.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div[1]/div/div/div[3]/div/div[1]/div[2]/div/div[2]/div').get_attribute("innerText")
                except NoSuchElementException:
                    likes="pattern error"
                try:
                    follow=browser.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div[1]/div/div/div[3]/div/div[1]/div[3]/div/div[2]/div').get_attribute("innerText")
                except NoSuchElementException:
                    follow="pattern error"
                try:
                    address=browser.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div[1]/div/div/div[3]/div/div[2]/div[3]/div/div[2]/div[1]').get_attribute("innerText")
                except NoSuchElementException:
                    address="pattern error"
                try:
                    contact=browser.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div[1]/div/div/div[3]/div/div[2]/div[4]/div/div[2]/div').get_attribute("innerText")
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

    
