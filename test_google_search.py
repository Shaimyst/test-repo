def test_google_search(chrome_driver):
    chrome_driver.get("http://google.com")

    # enter search words
    search_field = chrome_driver.find_elemenet_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
    search_field.sendkeys("critical role")

    # press search button
    search_button = chrome_driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]")
    search_button.click()