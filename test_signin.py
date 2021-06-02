import os
from selenium import webdriver
import time
import pytest

chromedriver = "/usr/local/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("http://imdb.com")

def test_signin_button():
    signin_button = driver.find_element_by_link_text("Sign In")
    signin_button.click()

    # wait
    time.sleep(2)

    # find create account button
    new_account_button = driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[2]/div[1]/div[1]/div/div[2]/a")

    # click create account button
    new_account_button.click()

    # fill in information
    name_field = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/form/div/div/div[1]/input")
    name_field.send_keys("Jessica")
    
    email_field = driver.find_element_by_id("ap_email")
    email_field.send_keys("test@gmail.com")

    password_field = driver.find_element_by_id("ap_password")
    password_field.send_keys("mypassword")

    reenter_password_field = driver.find_element_by_id("ap_password_check")
    reenter_password_field.send_keys("mypassword")

    # submit information
    submit_button = driver.find_element_by_id("a-autoid-0")
    submit_button.click()

def test_close_down():
    # close browser
    driver.quit()