from selenium import webdriver
try:
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get("http://suninjuly.github.io/registration1.html")
    browser.find_element_by_xpath('.//label[text()=\'First name*\']/following-sibling::input').send_keys("pasha")
    browser.find_element_by_xpath('.//label[text()=\'Last name*\']/following-sibling::input').send_keys("zzzz")
    browser.find_element_by_xpath('.//label[text()=\'Email*\']/following-sibling::input').send_keys("pasha@ya.ru")
    browser.find_element_by_xpath(".//button[text()='Submit']").click()

finally:
    time.sleep(10)
    browser.close()
    browser.quit()