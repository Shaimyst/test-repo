import os
import time
import pytest
from webdriver_manager import driver

def test_signin_button(chrome_driver):
    chrome_driver.get("http://staging.scrive.com")
    time.sleep(10)

# login: jessica.sadler+contacts@scrive.com
# password: 'qqqqqq'
# 
# sign in or save credentials
#
# steps:
# go to home page
# start a flow with creator and 2nd signing party and 2 docs
# start signing process
# sign and complete flow
# 
# assert completion
# 
