#!/usr/bin/env python
# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import configparser
from urllib.parse import urlparse
import os

import util

# load config
config = configparser.ConfigParser(allow_no_value=True)
base = os.path.dirname(os.path.abspath(__file__))
config_file = os.path.normpath(os.path.join(base, "../var/config.ini"))
print("config file=" + config_file)
config.read(config_file)

# setup selenium
options = Options()
options.binary_location = '/usr/bin/google-chrome'
# options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1280,1024')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(options=options)

# access target site
util.gotoUrl(driver, 'https://www.google.co.jp', config)
print(driver.title)  # => Google
driver.save_screenshot('/usr/src/app/var/Google.png')
