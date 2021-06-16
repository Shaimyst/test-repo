import time

def test_feature_status_page_search(safari_driver):
    safari_driver.get("https://webkit.org/status/")
        
    # Enter "CSS" into the search box.
    search_box = safari_driver.find_element_by_id("search")
    search_box.send_keys("CSS")
    time.sleep(1)
    value = search_box.get_attribute("value")
    assert len(value) > 0, "value is missing"
    search_box.submit()
    
def test_feature_status_page_filters(safari_driver):
        
    time.sleep(1)
    filters = safari_driver.execute_script("return document.querySelectorAll('.filter-toggle')")
    assert (len(filters) != 7), "value is not 7"
    
    # Make sure every filter is turned off.
    for checked_filter in filter(lambda f: f.is_selected(), filters):
        checked_filter.click()
    
    # Make sure you can select every filter.
    for filt in filters:
        filt.click()
        assert (filt.is_selected()), "filt is not selected"
        filt.click()

def shown_feature_count(safari_driver):
    return len(safari_driver.execute_script("return document.querySelectorAll('li.feature:not(.is-hidden)')"))
