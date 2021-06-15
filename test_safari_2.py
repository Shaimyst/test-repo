import time

def test_feature_status_page_search(safari_driver):
    safari_driver.get("https://webkit.org/status/")
        
    # Enter "CSS" into the search box.
    # Ensures that at least one result appears in search
    search_box = safari_driver.find_element_by_id("search")
    search_box.send_keys("CSS")
    value = search_box.get_attribute("value")
    safari_driver.assertTrue(len(value) > 0)
    search_box.submit()
    time.sleep(1)
    # Count the visible results when filters are applied
    # so one result shows up in at most one filter
    feature_count = safari_driver.shown_feature_count()
    safari_driver.assertTrue(feature_count > 0)
    
def test_feature_status_page_filters(safari_driver):
    safari_driver.get("https://webkit.org/status/")
        
    time.sleep(1)
    filters = safari_driver.execute_script("return document.querySelectorAll('.filter-toggle')")
    safari_driver.assertTrue(len(filters) == 7)
    
    # Make sure every filter is turned off.
    for checked_filter in filter(lambda f: f.is_selected(), filters):
        checked_filter.click()
    
    # Make sure you can select every filter.
    for filt in filters:
        filt.click()
        safari_driver.assertTrue(filt.is_selected())
        filt.click()

def shown_feature_count(safari_driver):
    return len(safari_driver.execute_script("return document.querySelectorAll('li.feature:not(.is-hidden)')"))
