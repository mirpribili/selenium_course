from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    name = browser.find_element_by_css_selector("body > div > form > div.first_block > div.form-group.first_class > input")
    name.send_keys("Ivan")
    sname = browser.find_element_by_css_selector("body > div > form > div.first_block > div.form-group.second_class > input")
    sname.send_keys("Petrov")
    email = browser.find_element_by_css_selector("body > div > form > div.first_block > div.form-group.third_class > input")
    email.send_keys("sss@sss.com")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    