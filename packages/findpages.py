def findpages(username,password):
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
    print("Stop all running browser before starting...")
    scroll_num=input("How many time to scroll the page[More scroll= More pages]:")
    scroll_num=int(scroll_num)
    for m in range(scroll_num):
         browser.find_element_by_tag_name('html').send_keys(Keys.END)
         sleep(3)
    link_list=browser.find_elements_by_class_name('_32mo')
    num_pages=len(link_list)
    return link_list,num_pages