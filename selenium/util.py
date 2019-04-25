#!/usr/bin/env python
# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import configparser


def loginSite(driver: webdriver, config: configparser.ConfigParser):
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
        nextButton = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, user_next)))
        nextButton.click()

    password = driver.find_element(By.CSS_SELECTOR, site["password_field"])
    password.send_keys(site["password"])
    time.sleep(1)

    password_next = site.get("password_next")
    if password_next is not None:
        time.sleep(2)
        nextButton = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, password_next)))
        nextButton.click()
        time.sleep(1)

    remember_next = site.get("remember_next")
    if remember_next is not None:
        time.sleep(2)
        nextButton = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, remember_next)))
        nextButton.click()


def gotoUrl(driver: webdriver, url: str, config: configparser.ConfigParser):
    try:
        driver.get(url)
    except Exception as e:
        print(e)

    for var in range(0, config.getint("gotoUrl", "retry")):
        try:
            cur_url = driver.current_url
            print(cur_url)
            if cur_url.startswith(url) or url.startswith(cur_url):
                break
            time.sleep(1)
            loginSite(driver, config)
        except Exception as e:
            print(e)
