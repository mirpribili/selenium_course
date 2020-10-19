homework = '''
    Инопланетяне оставляют загадочные сообщения на Stepik в фидбеке задач на правильное решение. Мы смогли локализовать несколько url-адресов задач, где появляются кусочки сообщений. Ваша задача — реализовать автотест со следующим сценарием действий: 

        открыть страницу 
        ввести правильный ответ 
        нажать кнопку "Отправить" 
        дождаться фидбека о том, что ответ правильный 
        проверить, что текст в опциональном фидбеке полностью совпадает с "Correct!"

    Опциональный фидбек — это текст в черном поле, как показано на скриншоте: 


    Правильным ответом на задачу в заданных шагах является число:

    import time
    import math

    answer = math.log(int(time.time()))

    Используйте маркировку pytest для параметризации и передайте в тест список ссылок в качестве параметров: 

    https://stepik.org/lesson/236895/step/1
    https://stepik.org/lesson/236896/step/1
    https://stepik.org/lesson/236897/step/1
    https://stepik.org/lesson/236898/step/1
    https://stepik.org/lesson/236899/step/1
    https://stepik.org/lesson/236903/step/1
    https://stepik.org/lesson/236904/step/1
    https://stepik.org/lesson/236905/step/1

    Используйте осмысленное сообщение об ошибке в проверке текста, а также настройте нужные ожидания, чтобы тесты работали стабильно. 

    В упавших тестах найдите кусочки послания. Тест должен падать, если текст в опциональном фидбеке не совпадает со строкой "Correct!" Соберите кусочки текста в одно предложение и отправьте в качестве ответа на это задание. 

    Важно! Чтобы пройти это задание, дополнительно убедитесь в том, что у вас установлено правильное локальное время (https://time.is/ru/). Ответ для каждой задачи нужно пересчитывать отдельно, иначе они устаревают. 
'''

import math
import time

import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

correct_answer_text = "Correct!"

# Создаем кортеж со списком url
url_check = ("https://stepik.org/lesson/236895/step/1",
             "https://stepik.org/lesson/236896/step/1",
             "https://stepik.org/lesson/236897/step/1",
             "https://stepik.org/lesson/236898/step/1",
             "https://stepik.org/lesson/236899/step/1",
             "https://stepik.org/lesson/236903/step/1",
             "https://stepik.org/lesson/236904/step/1",
             "https://stepik.org/lesson/236905/step/1")


@pytest.fixture(scope="function")  # Создаем фикустуру для запуска браузера
def browser():
    print("\n Start browser...")
    browser = webdriver.Chrome()
    yield browser
    print("\n Quit browser..")
    browser.quit()


@pytest.mark.parametrize('url', url_check)
def test_hidden_message(browser, url):
    link = f'{url}'
    browser.get(link)

    # Ждем появления текстового поля на странице в течении 10 сек
    # Находим поле ввода ответа на странице, и вставляем туда ответ math.log(int(time.time())
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "textarea.textarea"))
    )
    text_field = browser.find_element_by_css_selector("textarea.textarea")
    text_field.send_keys(str(math.log(int(time.time()))))  # Хорошо читается :/

    # Находим кнопку "Submit"
    # Нажимаем на нее
    submit_btn = browser.find_element_by_css_selector("button.submit-submission")
    submit_btn.click()

    # Ждем появления элемента "дополнительного фидбека" в течении 5 сек
    # Находим параметр text у найденого элемента
    # Сверяем text с искомым нами (correct_answer_text)
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "pre.smart-hints__hint"))
    )
    find_answer_text = browser.find_element_by_css_selector("pre.smart-hints__hint")
    answer_text = find_answer_text.text

    try:
        assert answer_text == correct_answer_text, 'Text is not: "Correct!"'

    except Exception:
        raise AssertionError('Error! Text does not match')
    finally:
        print("----> " + answer_text + " <----")

# Смотриться лучше, но без assertError  не падает, браузер открыт всю сессию
# #from selenium import webdriver
# import pytest
# import time
# import math
#
# final = ''
#
#
# @pytest.fixture(scope="session")
# def browser():
#     br = webdriver.Chrome()
#     yield br
#     br.quit()
#     print(final)  # напечатать ответ про Сов в конце всей сессии
#
#
# @pytest.mark.parametrize('lesson', ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905'])
# def test_find_hidden_text(browser, lesson):
#     global final
#     link = f'https://stepik.org/lesson/{lesson}/step/1'
#     browser.implicitly_wait(10)
#     browser.get(link)
#     answer = math.log(int(time.time()))
#     browser.find_element_by_css_selector('textarea').send_keys(str(answer))
#     browser.find_element_by_css_selector('.submit-submission ').click()
#     check_text = browser.find_element_by_css_selector('.smart-hints__hint').text
#     try:
#         assert 'Correct!' == check_text
#     except AssertionError:
#         final += check_text  # собираем ответ про Сов с каждой ошибкой

#pytest -v  lesson3_item6_step3.py

answer = '''

E           AssertionError: Text is not: "Correct!"
E           assert 'The owls ' == 'Correct!'
E             - The owls 
E             + Correct!
E           AssertionError: Error! Text does not match
E           AssertionError: Text is not: "Correct!"
E           assert 'are not ' == 'Correct!'
E             - are not 
E             + Correct!
E           AssertionError: Error! Text does not match
E           AssertionError: Text is not: "Correct!"
E           assert 'what they seem! OvO' == 'Correct!'
E             - what they seem! OvO
E             + Correct!
E           AssertionError: Error! Text does not match


The owls are not what they seem! OvO
'''
