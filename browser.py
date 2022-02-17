# Allows for selenium to communicate with your OS
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
#  From webdrivermanager import ChromeDriverManager <---this was causing the browser to open and close upon code exe
# This is needed for the specific browser being used
from selenium.webdriver.chrome.options import Options
#  Module for selenium to type keys on website
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
#  Allow browser window to remain open after code is exe. Would close otherwise.
chrome_options.add_experimental_option("detach", True)

# This var uses the selenium web driver to connect to the path of driver
# Create function that will retrieve the PATH on someones machine or device
#
driver = webdriver.Chrome(r"C:\Program Files (x86)\chromedriver.exe") #<---at this time, you need to modify this for your path
#os.environ['PATH'] += r"C:\Program Files (x86)\chromedriver.exe" <---for some reason this didn't work but w.e - above was solution

#  Var with .get("<target website>") to open a website
#
#  Create function for driver.get that will accept a user input for desired item
#
driver.get("https://www.twitter.com")
driver.implicitly_wait(5)
#  .implicityly_wait set an amount of time in seconds for the site elements to load 
#  before doing something
driver.implicitly_wait(5)

#  Var finds HTML elements on a page based on diff attributes which you set
#item = driver.find_element_by_xpath('')
#  .click will "click" just as a person will on above defined element
#item.click()
  

