import time

def test_feature_status_page_search(safari_driver):
    safari_driver.get("https://webkit.org/status/")
        
    # Enter "CSS" into the search box.
    # Ensures that at least one result appears in search
    search_box = safari_driver.find_element_by_id("search")
    search_box.send_keys("CSS")
    value = search_box.get_attribute("value")
    assert len(value) > 0, "value is missing"
    search_box.submit()
    time.sleep(1)
    # Count the visible results when filters are applied
    # so one result shows up in at most one filter
    feature_count = safari_driver.shown_feature_count()
    assert feature_count > 0, "value is missing"
    
def test_feature_status_page_filters(safari_driver):
    safari_driver.get("https://webkit.org/status/")
        
    time.sleep(1)
    filters = safari_driver.execute_script("return document.querySelectorAll('.filter-toggle')")
    assert (len(filters) == 7), "value is not 7"
    
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
