from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os


## Setup chrome options
options = Options()
options.add_experimental_option("detach", True)

# Set path to chromedriver as per your configuration
homedir = os.path.expanduser("~")
chrome_service = Service(f"{homedir}/chromedriver/stable/chromedriver")

# Choose Chrome Browser
chrome_driver = webdriver.Chrome(service=chrome_service, options=options)

chrome_driver.maximize_window()