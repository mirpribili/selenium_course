
'''

    Возьмите тесты из шага — https://stepik.org/lesson/138920/step/11?unit=196194
    Создайте новый файл
    Создайте в нем класс с тестами, который должен наследоваться от unittest.TestCase по аналогии с предыдущим шагом
    Перепишите в стиле unittest тест для страницы http://suninjuly.github.io/registration1.html
    Перепишите в стиле unittest второй тест для страницы http://suninjuly.github.io/registration2.html
    Оформите финальные проверки в тестах в стиле unittest, например, используя проверочный метод assertEqual
    Запустите получившиеся тесты из файла 
    Просмотрите отчёт о запуске и найдите последнюю строчку 
    Отправьте эту строчку в качестве ответа на это задание 



    Как и прежде загружаем модуль selenium и пользуемся им, как и в задаче - предке;
    
    Создаем класс в названии которого фигурирует "test_class_name";
    
    Наследуем (unittest.TestCase);
    
    Создаем две функции внутри класса, у меня они получились идентичными, за исключением содержимого переменной URL (ссылка на веб страницу);
    
    В функциях из предыдущего шага не используем конструкции try, except, finally и assert, используем только: self.assertEqual('что должно быть', 'что есть', 'что произошло');
    
    Добавляем в код: if __name__ == "__main__": unittest.main()
    
    Тест, очевидно, проваливается на втором линке, ищем одну короткую строку, которая нам об этом говорит. 

'''

def test_substring(full_string, substring):
    # ваша реализация, напишите assert и сообщение об ошибке
    assert substring in full_string, f"expected '{substring}' to be substring of '{full_string}'"
    


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
