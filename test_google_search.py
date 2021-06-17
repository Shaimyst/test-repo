
from constants import GOOGLE_URL, GOOGLE_SEARCH_BUTTON_XPATH

def test_google_search(chrome_driver):
    chrome_driver.get(GOOGLE_URL)

    # accept cookies
    cookies_button = chrome_driver.find_element_by_id("L2AGLb")
    cookies_button.click()
    # enter search words
    search_field = chrome_driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
    search_field.send_keys("critical role")

    # press search button
    search_button = chrome_driver.find_element_by_xpath(GOOGLE_SEARCH_BUTTON_XPATH)
    search_button.submit()

    # assert search commenced
    assert chrome_driver.current_url != GOOGLE_URL, "didn't search"
