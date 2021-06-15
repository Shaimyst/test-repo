import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def input_value():
   input = 39
   return input

@pytest.fixture(scope="session")
def chrome_driver():
   driver = webdriver.Chrome(ChromeDriverManager().install())
   yield driver
   driver.quit()

@pytest.fixture(scope="session")
def safari_driver():
   driver = webdriver.Safari()
   yield driver
   driver.quit()