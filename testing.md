# Тестирование web-приложений и тестовые фреймворки

Далее мы рассмотрим, как использовать Selenium Webdriver для написания автоматических тестов. 

### Почему мы еще не можем назвать тестами скрипты, которые мы писали в предыдущих модулях?

Для этого нам придётся познакомиться с тестовыми фреймворками **unittest и PyTest**, которые позволяют создавать легко читаемые проверки ожидаемых результатов в тестах, удобно настраивать запуск большого количества тестов в нужных окружениях, организовывать хранение тестов и генерацию отчётов для последующего анализа.

В качестве основы для данного урока мы адаптировали руководство про [написание юнит-тестов в Python](https://realpython.com/python-testing/)


# Юнит-тесты и интеграционные тесты

- Юнит-тесты проверяют очень маленький кусок кода, обычно конкретную функцию, и чаще всего их пишут разработчики, которые хорошо понимают возможные крайние случаи для своего стека технологий.
- Интеграционные тесты проверяют взаимодействие сразу нескольких систем. Они могут создаваться и поддерживаться как разработчиками и тестировщиками, так и аналитиками (если для них разработан удобный фреймворк для написания тестов).

- **Юнит-тесты всегда автоматизированы**, так как проверяют непосредственно работу кода. 
- Интеграционные тесты могут быть ручными и автоматизированными. 
- Иногда выделяют **отдельную категорию end-to-end (е2е) тестов**, которые проверяют полный стек технологий приложения и пользовательский сценарий взаимодействия с приложением как с черным ящиком. *Если говорить про UI-тесты, которые азрабатываются с помощью Selenium, то их стоит отнести к разряду end-to-end тестов*, так как они проверяют совместную работу всех систем web-продукта: работу frontend и backend, работу базы данных, дополнительные сервисы, такие как аналитика, платежные системы и так далее. 


## пирамида тестирования

<img alt="" src="/[img]/pyramid.png" width="593" height="251">


# Структура теста

Любой тест должен содержать:

- Входные данные.
- Тестовый сценарий, то есть набор шагов, которые надо выполнить для получения результата.
- Проверка ожидаемого результата


# Проверка ожидаемого результата

**Как можно проверить ожидаемый результат?** Для этого используется встроенная в **Python инструкция assert**, которая проверяет истинность утверждений. 
**assert True не приводит к выводу дополнительных сообщений**, а вот **assert False вызовет исключение AssertionError**.

Рассмотрим работу **assert на примере встроенной функции abs()**, которая возвращает абсолютное значение числа по модулю. Для этого активируйте созданное ранее виртуальное окружение и запустите интерпретатор Python. Например, для Linux выполните:
```python
source selenium_env/bin/activate

python
```
Теперь будем вводить приведенные ниже команды и смотреть на результат их выполнения.

Если значение выражения истинно, то в консоли не должно появиться дополнительных сообщений. Выполним:

>>> assert abs(-42) == 42

Если условие не выполнено, то в консоли выводится лог ошибки с названием файла и номером строчки, в которой произошла ошибка, а также тип ошибки AssertionError:


>>> assert abs(-42) == -42

```python
Traceback (most recent call last):

  File "<stdin>", line 1, in <module>

AssertionError
```
Простое сообщение AssertionError не очень информативно. Когда тестов становится много, бывает сложно вспомнить, что именно мы проверяем в данном тесте. Для добавления дополнительного сообщения можно при вызове assert через запятую написать нужное сообщение, которое будет выведено в случае ошибки проверки результата:


>>> assert abs(-42) == -42, "Should be absolute value of a number"

```python
Traceback (most recent call last):

  File "<stdin>", line 1, in <module>

AssertionError: Should be absolute value of a number
```