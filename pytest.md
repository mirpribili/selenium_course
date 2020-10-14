# PyTest&nbsp;— преимущества и недостатки

<p>Для написания данного урока мы вдохновлялись <a href="https://habr.com/post/269759/" rel="nofollow noopener noreferrer" target="_blank">статьёй</a> на Хабре, адаптировав ее к специфике тестирования веб-приложений с помощью Selenium WebDriver.</p>

## Рассмотрим преимущества использования PyTest:

<p>1) PyTest полностью обратно совместим с фреймворками unittest и nosetest. Это означает, что если изначально вы писали тесты, используя unittest, то перейти на PyTest можно буквально в ту же минуту. Для этого в вашем виртуальном окружении должен быть установлен пакет PyTest. Не забудьте активировать ваше виртуальное окружение&nbsp;и установите PyTest.</p>

<p><strong>Для Windows:</strong></p>

<pre><code class="hljs taggerscript">&gt; selenium_env<span class="hljs-symbol"><span class="hljs-symbol">\S</span></span>cripts<span class="hljs-symbol"><span class="hljs-symbol">\a</span></span>ctivate.bat 
(selenium_env) С:<span class="hljs-symbol"><span class="hljs-symbol">\U</span></span>sers<span class="hljs-symbol"><span class="hljs-symbol">\u</span></span>ser<span class="hljs-symbol"><span class="hljs-symbol">\e</span></span>nvironments&gt;  pip install pytest==5.1.1</code></pre>

<p><strong>Для Linux и macOS:</strong></p>

<pre><code class="hljs armasm">​​​​​​​$ source <span class="hljs-keyword"><span class="hljs-keyword">selenium_env/bin/activate </span></span>

(<span class="hljs-keyword"><span class="hljs-keyword">selenium_env) </span></span>$ pip install pytest=<span class="hljs-number"><span class="hljs-number">=5</span></span>.<span class="hljs-number"><span class="hljs-number">1</span></span>.<span class="hljs-number"><span class="hljs-number">1</span></span></code></pre>

<p>Теперь мы можем запустить тесты в нашем файле <em>test_abs_project.py </em>с помощью PyTest, не изменяя сам файл. PyTest сам найдёт тесты в папке, в которой вы их запускаете,&nbsp;и выполнит их:</p>

<pre><code class="language-bash hljs">pytest test_abs_project.py</code></pre>

<p>2) Подробный отчёт с поддержкой цветовых схем из коробки.</p>

<p>3) PyTest не требует написания дополнительных специфических конструкций в тестах, как того требует unittest (no boilerplate).</p>

<p>4) Для проверок используется стандартный assert из Python.</p>

<p>5) Возможность создания динамических фикстур (специальных функций, которые настраивают тестовые окружения и готовят тестовые данные).</p>

<p>6) Дополнительные возможности по настройке фикстур.</p>

<p>7) Параметризация тестов — для одного теста можно задать разные параметры (тест запустится несколько раз с разными тестовыми данными).</p>

<p>8) Наличие маркировок (marks), которые позволяют маркировать тесты для их выборочного запуска.</p>

<p>9) Возможность передавать дополнительные параметры через командную строку для настройки тестовых окружений.</p>

<p>10) Большое количество плагинов, которые расширяют возможности PyTest и позволяют решать узкоспециализированные проблемы, что может сэкономить много времени.</p>

## Рассмотрим&nbsp;минусы PyTest:

<p>1) PyTest требуется устанавливать дополнительно, так как&nbsp;он не входит в стандартный пакет библиотек Python, в отличие от unittest. Нужно не забывать об этом, когда вы будете настраивать автоматический запуск тестов с помощью CI-сервера.</p>

<p>
2) Использование PyTest требует более глубокого понимания языка Python, чтобы разобраться, как применять фикстуры, параметризацию и другие возможности PyTest.</p></span>



<span><h2><strong>PyTest: правила&nbsp;запуска тестов&nbsp;</strong></h2>

<p>В этом шаге мы коротко обсудим важные особенности запуска тестов с помощью PyTest. Когда мы выполняем&nbsp;команду <strong>pytest</strong>, тест-раннер собирает все тесты для запуска по определенным правилам:</p>

<ul>
    <li>
    <p>если мы не передали никакого аргумента в команду, а написали просто pytest, тест-раннер начнёт поиск в текущей директории</p>
    </li>
    <li>
    <p>как аргумент можно передать&nbsp;файл, путь к директории или любую комбинацию директорий и файлов, например:&nbsp;</p>
    </li>
</ul>

<pre><code class="language-python hljs">pytest scripts/selenium_scripts
<span class="hljs-comment"><span class="hljs-comment"># найти все тесты в директории scripts/selenium_scripts</span></span>

pytest test_user_interface.py
<span class="hljs-comment"><span class="hljs-comment"># найти и выполнить все тесты в файле </span></span>

pytest scripts/drafts.py::test_register_new_user_parametrized
<span class="hljs-comment"><span class="hljs-comment"># найти тест с именем test_register_new_user_parametrized в указанном файле в указанной директории и выполнить </span></span>
</code></pre>

<ul>
    <li>
    <p>дальше происходит рекурсивный поиск: то есть PyTest обойдет все вложенные директории</p>
    </li>
    <li>
    <p>во всех директориях PyTest ищет файлы, которые удовлетворяют правилу &nbsp;<strong>test_*.py</strong> или <strong>*_test.py</strong> (то есть начинаются на test_ или заканчиваются _test и имеют расширение .py)</p>
    </li>
    <li>
    <p>внутри всех этих файлов находит тестовые функции по следующему правилу:</p>

    <ul>
        <li>
        <p>все тесты, название которых начинается с <strong>test</strong>, которые находятся вне классов</p>
        </li>
        <li>
        <p>все тесты, название&nbsp;которых начинается с <strong>test</strong>&nbsp;внутри классов, имя которых начинается с <strong>Test</strong>&nbsp;(и без метода __init__ внутри класса)</p>
        </li>
    </ul>
    </li>
</ul>

<p>Подробности:&nbsp;<a href="https://docs.pytest.org/en/latest/goodpractices.html#conventions-for-python-test-discovery" rel="noopener noreferrer nofollow" target="_blank">Conventions for Python test discovery</a></p></span>

<img alt="" src="/[img]/pytest.png" width="1023" height="1631">



<span><h2>PyTest&nbsp;— отчёты</h2>

<p>Вы могли заметить, что PyTest позволяет генерировать подробный отчёт с поддержкой цветовых схем&nbsp;и форматированием прямо из коробки.</p>

<p>Давайте еще раз запустим наши тесты с помощью unittest и PyTest, чтобы сравнить выводимый результат.</p>

<p>Мы видим, что в PyTest-отчёте упавший&nbsp;тест выделен красным шрифтом, что делает разбор логов более приятным занятием.</p>

<p><strong>unittest:</strong></p>

<p><img alt="" src="https://ucarecdn.com/7cb1723f-3a3b-4fb6-a6bd-6a2e1904d02f/"></p>

<p><strong>PyTest:&nbsp;</strong></p>

<p><img alt="" src="https://ucarecdn.com/81ceab3c-0d25-4beb-ab87-09d110294d63/"></p>

<p>Если запустить PyTest с параметром <strong>-v</strong> (<strong>verbose</strong>, то есть&nbsp;подробный), то в отчёт добавится дополнительная информация со списком тестов и статусом их прохождения:&nbsp;</p>

<p><img alt="" src="https://ucarecdn.com/6a53144b-e083-410f-92ef-404511fc6c07/"></p>

<p>Другие полезные команды для манипуляции выводом тестов PyTest можно найти по ссылке:&nbsp;<a href="https://gist.github.com/amatellanes/12136508b816469678c2" rel="noopener noreferrer nofollow" target="_blank">Useful py.test commands.</a></p></span>

<span><h2>PyTest&nbsp;— как пишут тесты</h2>

<p>PyTest не требует написания дополнительных специфических конструкций в тестах, как того требует unittest.</p>

<p>Мы уже увидели, что PyTest может запускать тесты, написанные в unittest-стиле. Перепишем наши тесты из <strong>test_abs_project.py</strong> в более простом формате, который также понимает PyTest. Назовём новый файл test_abs.py:</p>

<pre><code class="language-python hljs"><span class="hljs-function"><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-keyword">def</span></span></span><span class="hljs-function"> </span><span class="hljs-title"><span class="hljs-function"><span class="hljs-title">test_abs1</span></span></span><span class="hljs-params"><span class="hljs-function"><span class="hljs-params">()</span></span></span><span class="hljs-function">:</span></span>
    <span class="hljs-keyword"><span class="hljs-keyword">assert</span></span> abs(<span class="hljs-number"><span class="hljs-number">-42</span></span>) == <span class="hljs-number"><span class="hljs-number">42</span></span>, <span class="hljs-string"><span class="hljs-string">"Should be absolute value of a number"</span></span>

<span class="hljs-function"><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-keyword">def</span></span></span><span class="hljs-function"> </span><span class="hljs-title"><span class="hljs-function"><span class="hljs-title">test_abs2</span></span></span><span class="hljs-params"><span class="hljs-function"><span class="hljs-params">()</span></span></span><span class="hljs-function">:</span></span>
    <span class="hljs-keyword"><span class="hljs-keyword">assert</span></span> abs(<span class="hljs-number"><span class="hljs-number">-42</span></span>) == <span class="hljs-number"><span class="hljs-number">-42</span></span>, <span class="hljs-string"><span class="hljs-string">"Should be absolute value of a number"</span></span>

</code></pre>

<p>Запустим тесты в этом файле:</p>

<pre><code class="language-python hljs">pytest test_abs.py</code></pre>

<p>Код тестов стал короче и&nbsp;читабельнее.</p></span>

<span><h2>PyTest&nbsp;— проверка ожидаемого результата (assert)</h2>

<p>Если вы используете unittest, то для проверки ожидаемых результатов в тестах вам нужно знать и использовать большой набор assert-методов, например, таких: assertEqual, assertNotEqual, assertTrue, assertFalse и <a href="https://docs.python.org/3/library/unittest.html#assert-methods﻿" rel="nofollow noopener noreferrer" target="_blank">другие</a>.</p>

<p>В PyTest используется стандартный assert метод из языка Python, что делает код более очевидным.</p>

<p>Давайте сравним два подхода. Проверим, что две переменные равны друг другу.</p>

<p><strong>unittest:</strong></p>

<pre><code class="hljs stylus">self.assertEqual(<span class="hljs-selector-tag"><span class="hljs-selector-tag">a</span></span>, <span class="hljs-selector-tag"><span class="hljs-selector-tag">b</span></span>, msg=<span class="hljs-string"><span class="hljs-string">"Значения разные"</span></span>)</code></pre>

<p><strong>PyTest:</strong></p>

<pre><code class="hljs stylus">assert <span class="hljs-selector-tag"><span class="hljs-selector-tag">a</span></span> == <span class="hljs-selector-tag"><span class="hljs-selector-tag">b</span></span>, <span class="hljs-string"><span class="hljs-string">"Значения разные"</span></span></code></pre>

<p>С помощью assert можно проверять любую конструкцию, которая возвращает True/False. Это может быть проверка равенства, неравенства, содержания подстроки в строке&nbsp;или любая другая вспомогательная функция, которую вы опишете самостоятельно. Все это делает код проверок приятным и понятным для чтения:&nbsp;</p>

<pre><code class="hljs ceylon"><span class="hljs-keyword"><span class="hljs-keyword">assert</span></span> user<span class="hljs-number"><span class="hljs-number">_</span></span><span class="hljs-keyword"><span class="hljs-keyword">is</span></span><span class="hljs-number"><span class="hljs-number">_</span></span>authorised(), <span class="hljs-string"><span class="hljs-string">"User is guest"</span></span></code></pre>

<p>Если&nbsp;нужно проверить, что тест вызывает ожидаемое исключение (довольно редкая ситуация для UI-тестов, и вам этот способ, скорее всего, никогда не пригодится),&nbsp;мы можем использовать специальную конструкцию <strong>with pytest.raises()</strong>. Например, можно проверить, что на странице сайта не должен отображаться какой-то элемент:</p>

<pre><code class="language-python hljs"><span class="hljs-keyword"><span class="hljs-keyword">import</span></span> pytest

<span class="hljs-keyword"><span class="hljs-keyword">from</span></span> selenium <span class="hljs-keyword"><span class="hljs-keyword">import</span></span> webdriver
<span class="hljs-keyword"><span class="hljs-keyword">from</span></span> selenium.common.exceptions <span class="hljs-keyword"><span class="hljs-keyword">import</span></span> NoSuchElementException


<span class="hljs-function"><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-keyword">def</span></span></span><span class="hljs-function"> </span><span class="hljs-title"><span class="hljs-function"><span class="hljs-title">test_exception1</span></span></span><span class="hljs-params"><span class="hljs-function"><span class="hljs-params">()</span></span></span><span class="hljs-function">:</span></span>
    <span class="hljs-keyword"><span class="hljs-keyword">try</span></span>:
        browser = webdriver.Chrome()
        browser.get(<span class="hljs-string"><span class="hljs-string">"http://selenium1py.pythonanywhere.com/"</span></span>)
        <span class="hljs-keyword"><span class="hljs-keyword">with</span></span> pytest.raises(NoSuchElementException):
            browser.find_element_by_css_selector(<span class="hljs-string"><span class="hljs-string">"button.btn"</span></span>)
            pytest.fail(<span class="hljs-string"><span class="hljs-string">"Не должно быть кнопки Отправить"</span></span>)
    <span class="hljs-keyword"><span class="hljs-keyword">finally</span></span>: 
        browser.quit()

<span class="hljs-function"><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-keyword">def</span></span></span><span class="hljs-function"> </span><span class="hljs-title"><span class="hljs-function"><span class="hljs-title">test_exception2</span></span></span><span class="hljs-params"><span class="hljs-function"><span class="hljs-params">()</span></span></span><span class="hljs-function">:</span></span>
    <span class="hljs-keyword"><span class="hljs-keyword">try</span></span>:
        browser = webdriver.Chrome()
        browser.get(<span class="hljs-string"><span class="hljs-string">"http://selenium1py.pythonanywhere.com/"</span></span>)
        <span class="hljs-keyword"><span class="hljs-keyword">with</span></span> pytest.raises(NoSuchElementException):
            browser.find_element_by_css_selector(<span class="hljs-string"><span class="hljs-string">"no_such_button.btn"</span></span>)
            pytest.fail(<span class="hljs-string"><span class="hljs-string">"Не должно быть кнопки Отправить"</span></span>)
    <span class="hljs-keyword"><span class="hljs-keyword">finally</span></span>: 
        browser.quit()</code></pre>

<p>В первом тесте&nbsp;элемент будет найден, поэтому ошибка <strong>NoSuchElementException</strong>, которую ожидает контекстный менеджер pytest.raises, не возникнет, и тест упадёт.</p>

<pre><code class="hljs css"><span class="hljs-selector-tag"><span class="hljs-selector-tag">test_3_3_9_pytest_raises</span></span><span class="hljs-selector-class"><span class="hljs-selector-class">.py</span></span><span class="hljs-selector-pseudo"><span class="hljs-selector-pseudo">:8</span></span> (<span class="hljs-selector-tag"><span class="hljs-selector-tag">test_exception1</span></span>)
<span class="hljs-selector-tag"><span class="hljs-selector-tag">E</span></span>   <span class="hljs-selector-tag"><span class="hljs-selector-tag">Failed</span></span>: Не должно быть кнопки Отправить</code></pre>

<p>Во втором тесте, как мы и ожидали, кнопка не будет найдена, и тест пройдет.&nbsp;</p></span>

