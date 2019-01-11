# facebook-college-page-scrapper
Using selenium webautomation tool, various informations of a facebook page is scrapped and stored in a csv file.

# How to execute

1.Use pip to install all the dependencies from requirments.txt
    
    pip install -r requirements.txt
    
2.Download and install latest version of chrome browser.

3.Download latest chromedriver(in my case 2.45)

4.Add chromedriver to the PATH by copying the chromedriver.exe file in /usr/bin or /usr/local/bin or change the executable path like:
    
    browser=webdriver.Chrome(executable_path='pathofchromedriver')

5.For headless option in Chrome
                   
    option = webdriver.ChromeOptions()
    option.add_argument("--headless")
    browser = webdriver.Chrome(executable_path='pathofchromedriver',options=option)


5.Clone the repo, open the terminal in same directory and run init.py

    python init.py
