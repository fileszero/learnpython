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

config = configparser.ConfigParser(allow_no_value=True)


def loginSite(driver: webdriver):
    site = None
    for section in config.sections():  # find section
        if driver.current_url.startswith(section):
            site = config[section]
            break
    if site is None:
        return

    wait = WebDriverWait(driver, 1)
    user_id = driver.find_element(By.CSS_SELECTOR, site["user_field"])
    user_id.send_keys(site["user"])
    time.sleep(1)
    user_next = site.get("user_next")
    if user_next is not None:
        time.sleep(2)
        nextButton = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, user_next)))
        nextButton.click()

    password = driver.find_element(By.CSS_SELECTOR, site["password_field"])
    password.send_keys(site["password"])
    time.sleep(1)

    password_next = site.get("password_next")
    if password_next is not None:
        time.sleep(2)
        nextButton = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, password_next)))
        nextButton.click()
        time.sleep(1)

    remember_next = site.get("remember_next")
    if remember_next is not None:
        time.sleep(2)
        nextButton = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, remember_next)))
        nextButton.click()


def gotoUrl(driver: webdriver, url: str, wait_sec: int):
    try:
        driver.get(url)
    except Exception as e:
        print(e)

    for var in range(0, wait_sec):
        try:
            cur_url = driver.current_url
            print(cur_url)
            if cur_url.startswith(url) or url.startswith(cur_url):
                break
            time.sleep(1)
            loginSite(driver)
        except Exception as e:
            print(e)


base = os.path.dirname(os.path.abspath(__file__))
config_file = os.path.normpath(os.path.join(base, "../var/config.ini"))
print("config file=" + config_file)
config.read(config_file)

options = Options()
options.binary_location = '/usr/bin/google-chrome'
# options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1280,1024')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(options=options)
# driver.set_page_load_timeout(3)
# driver.implicitly_wait(3)

gotoUrl(driver, 'https://www.google.co.jp', 10)
print(driver.title)  #=> Google
driver.save_screenshot('/usr/src/app/var/Google.png')
