import os
import time
import pytest
from webdriver_manager import driver

def test_signin_button(chrome_driver):
    chrome_driver.get("http://imdb.com")
    signin_button = chrome_driver.find_element_by_link_text("Sign In")
    signin_button.click()

    # wait
    time.sleep(2)

    # find create account button
    new_account_button = chrome_driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[2]/div[1]/div[1]/div/div[2]/a")

    # click create account button
    new_account_button.click()

    # fill in information
    name_field = chrome_driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/form/div/div/div[1]/input")
    name_field.send_keys("Jessica")
    
    email_field = chrome_driver.find_element_by_id("ap_email")
    email_field.send_keys("test@gmail.com")

    password_field = chrome_driver.find_element_by_id("ap_password")
    password_field.send_keys("mypassword")

    reenter_password_field = chrome_driver.find_element_by_id("ap_password_check")
    reenter_password_field.send_keys("mypassword")

    # submit information
    submit_button = chrome_driver.find_element_by_id("a-autoid-0")
    submit_button.click()