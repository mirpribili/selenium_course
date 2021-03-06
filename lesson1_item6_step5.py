from selenium import webdriver
import time 
import math

link = "http://suninjuly.github.io/find_link_text"

value1 ="input"
value2 ="last_name"
value3 ="city"
value4 ="country"


try:
    browser = webdriver.Chrome()
    #link = "http://suninjuly.github.io/simple_form_find_task.html"
    #browser = webdriver.Chrome(executable_path=r"C:\chromedriver.exe")  # <- Путь до файла хромдрайвера

    browser.get(link)


    # Если хотим найти элемент по полному соответствию текста, то нам подойдет такой код: 
    link = browser.find_element_by_link_text(str(str(math.ceil(math.pow(math.pi, math.e)*10000))))
    link.click()

    # А если хотим найти элемент со ссылкой по подстроке, то нужно написать следующий код: 

    # link = browser.find_element_by_partial_link_text("examples")
    # link.click()

    time.sleep(1)


    input1 = browser.find_element_by_tag_name(value1)
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name(value2)
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name(value3)
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id(value4)
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    #find_element_by_css_selector()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций

    browser.close()
    time.sleep(2)
    browser.quit()

# не забываем оставить пустую строку в конце файла

