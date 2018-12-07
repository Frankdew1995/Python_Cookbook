from selenium import webdriver

import time




def browser(keyword):

    ##### Construct a browser
    browser = webdriver.Chrome("chromedriver.exe")

    ###### get the url
    url = "https://www.google.com/"
    browser.get(url)

    ##### Maximize the window
    browser.maximize_window()

    ##### wait for 3 seconds
    # time.sleep(600)

    ##### This is an xpath expression

    ########## Enter Search key word
    browser.find_element_by_xpath('//*[@id="tsf"]/div[2]/div/div[1]/div/div[1]/input').send_keys(keyword)

    ########## Selenium hot keys list:
    ########## https://selenium-python.readthedocs.io/api.html?highlight=keys#module-selenium.webdriver.common.keys

    ##### Press "Enter"
    browser.find_element_by_xpath('//*[@id="tsf"]/div[2]/div/div[3]/center/input[1]').send_keys(u'\ue007')

    ###### Close window
    # 1.
    browser.close()



browser(keyword="Google Inc")



'''
Selenium:
Selenium is a portable software-testing framework for web applications.
Selenium provides a playback (formerly also recording) tool for authoring
tests without the need to learn a test scripting language (Selenium IDE).
'''

'''
Prerequisites:
1. & pip install selenium
2. & Have slenium ChromeDriver downloaded into local. Download url: 
https://chromedriver.storage.googleapis.com/index.html?path=2.44/
3. (at least) Have ChromeDriver and .py in the same foler
'''