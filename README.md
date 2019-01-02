# Facebook-CollegePage-Scrapper
Using selenium webautomation tool, various informations of a facebook page is scrapped and stored in a csv file.
How to execute:
1.Use pip to install all the dependencies from requirment.txt
    pip install selenium
    pip install more-itertools
2.Download and install Chrome latest version.
3.Download latest chromedriver(in my case 2.45)
4.Add chromedriver to the PATH by copying the chromedriver.exe file in /usr/bin or /usr/local/bin or change the executable path like as your own:
    browser=webdriver.Chrome(executable_path='home/Downloads/chromedriver')
5.Clone the repo and execute _init_.py
