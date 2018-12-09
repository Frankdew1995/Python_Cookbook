from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import os

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
'''

##### Driver Path Configuration
driver_path = os.path.abspath("chromedriver.exe")

##### Construct a Browser
browser = webdriver.Chrome(driver_path)

###### get the url
url = "https://accounts.google.com/signin/v2/identifier?continue=https%3A%\
2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin"

browser.get(url)

##### Maximize the window
browser.maximize_window()

########## Enter Email Acocount
WebDriverWait(browser, 45).until(EC.presence_of_element_located((By.XPATH,
                            '//*[@id="identifierId"]'))).send_keys("your email")

### Selenium hot keys list:
### https://selenium-python.readthedocs.io/api.html?highlight=keys#module-selenium.webdriver.common.keys

##### Click next
WebDriverWait(browser, 45).until(EC.presence_of_element_located((By.XPATH,
                            '//*[@id="identifierNext"]/content/span'))).click()

time.sleep(2)

##### Enter the password
WebDriverWait(browser, 45).until(EC.presence_of_element_located((By.XPATH,
                            '//*[@id="password"]/div[1]/div/div[1]/input'))).send_keys("yourpassword")
#### Click Next
WebDriverWait(browser, 45).until(EC.presence_of_element_located((By.XPATH,
                            '//*[@id="passwordNext"]/content/span'))).click()

time.sleep(4)

#### Click Dot
WebDriverWait(browser, 45).until(EC.presence_of_all_elements_located((By.CLASS_NAME,
                            'gb_af')))[0].click()

time.sleep(1.85)

### Click Drive
WebDriverWait(browser, 45).until(EC.presence_of_element_located((By.XPATH,
                            '//*[@id="gb49"]/span[1]'))).click()

######################### Tab Switch #########
#### window tab indexing
second_tab = browser.window_handles[1]

#### Switching now to the second tab
browser.switch_to.window(second_tab)

time.sleep(2.5)

############## Search file
file_name = "Wusthof"
WebDriverWait(browser, 45).until(EC.presence_of_element_located((By.XPATH,
                    '//*[@id="aso_search_form_anchor"]/div[2]/input'))).send_keys(file_name)

WebDriverWait(browser, 45).until(EC.presence_of_element_located((By.XPATH,
                    '//*[@id="aso_search_form_anchor"]/div[2]/input'))).send_keys(Keys.ENTER)


browser.close()



