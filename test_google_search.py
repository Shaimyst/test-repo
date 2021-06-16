def test_google_search(chrome_driver):
    chrome_driver.get("http://google.com")

    # accept cookies
    cookies_button = chrome_driver.find_element_by_id("L2AGLb")
    cookies_button.click()
    # enter search words
    search_field = chrome_driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
    search_field.send_keys("critical role")

    # press search button
    search_button = chrome_driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]")
    search_button.submit()

    # assert search commenced
    assert chrome_driver.current_url != "http://google.com", "didn't search"
