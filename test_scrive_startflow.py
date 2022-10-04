import os
import time
import pytest
from webdriver_manager import driver

def test_signin_button(chrome_driver):
    chrome_driver.get("http://staging.scrive.com")
    time.sleep(10)