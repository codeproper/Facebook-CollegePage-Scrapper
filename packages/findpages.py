def findpages():
    browser.get('https://www.facebook.com/public?query=colleges%20nepal&type=pages&init=dir&nomc=0')
    with open('url.csv', 'w') as File:
        filewriter = csv.writer(File, delimiter=',',quoting=csv.QUOTE_MINIMAL)
        scroll_num=input("How many time to scroll the page[More scroll= More pages]:")
    #### To automate the process just define value of scroll num
    #scroll_num=
        scroll_num=int  (scroll_num)

        for m in range(scroll_num):
            browser.find_element_by_tag_name('html').send_keys(Keys.END)
            sleep(3)
        links=browser.find_elements_by_class_name('_32mo')#.get_attribute("href")
        for i in range(len(links)):
            link=links[i].get_attribute("href")
            filewriter.writerow([link])
        print("Done writing urls in url.csv file.. ")

    
