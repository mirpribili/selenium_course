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


<span><h2>Классические фикстуры (fixtures)</h2>

<p>Важной составляющей в использовании PyTest является концепция фикстур. Фикстуры в контексте PyTest&nbsp;— это вспомогательные функции для наших тестов, которые не являются частью тестового сценария.</p>

<p>Назначение фикстур может быть самым разным. Одно из распространенных применений фикстур — это&nbsp;подготовка тестового окружения и&nbsp;очистка тестового окружения и данных после завершения теста. Но, вообще говоря,&nbsp;фикстуры&nbsp;можно использовать для самых разных целей:&nbsp;для подключения к базе&nbsp;данных,&nbsp;с которой работают тесты, создания тестовых файлов&nbsp;или подготовки данных в текущем окружении с помощью API-методов. Более подробно про фикстуры в широком смысле вы можете прочитать в <a href="https://en.wikipedia.org/wiki/Test_fixture#Software" rel="nofollow noopener noreferrer" target="_blank">Википедии</a>.</p>

<p>Классический способ работы с фикстурами — создание setup- и teardown-методов в файле с тестами (<a href="https://docs.pytest.org/en/latest/xunit_setup.html#module-level-setup-teardown" rel="nofollow noopener noreferrer" target="_blank">документация в PyTest</a>).</p>

<p>Можно создавать фикстуры для модулей, классов и отдельных функций. Давайте попробуем написать фикстуру для инициализации браузера, который мы затем сможем использовать в наших тестах. После окончания тестов мы будем автоматически закрывать браузер с помощью команды<strong> browser.quit()</strong>, чтобы в нашей системе не оказалось множество открытых окон браузера. Вынесем инициализацию и закрытие браузера&nbsp;в фикстуры, чтобы не писать этот код для каждого теста.</p>


# Когда определен метод setUp(), бегун теста будет выполнять этот метод перед каждым испытанием. Аналогично, если определен метод tearDown(), то Test runner будет вызывать этот метод после каждого теста.

<p>Будем сразу объединять наши тесты в тест-сьюты, роль тест-сьюта будут играть классы, в которых мы будем хранить наши тесты.</p>

<p>Рассмотрим два примера: создание экземпляра браузера и его закрытие только один раз для всех тестов первого тест-сьюта&nbsp;и создание браузера для каждого теста во втором тест-сьюте. Сохраните следующий код в файл<strong> test_fixture1.py </strong>&nbsp;и запустите его с помощью PyTest. Не забудьте указать параметр <strong>-s</strong>, чтобы увидеть текст, который выводится командой print().</p>

<pre><code class="language-python hljs">pytest -s test_fixture1.py</code></pre>

<p><strong>test_fixture1.py:</strong></p>

<pre><code class="language-python hljs"><span class="hljs-keyword"><span class="hljs-keyword">from</span></span> selenium <span class="hljs-keyword"><span class="hljs-keyword">import</span></span> webdriver

link = <span class="hljs-string"><span class="hljs-string">"http://selenium1py.pythonanywhere.com/"</span></span>


<span class="hljs-class"><span class="hljs-keyword"><span class="hljs-class"><span class="hljs-keyword">class</span></span></span><span class="hljs-class"> </span><span class="hljs-title"><span class="hljs-class"><span class="hljs-title">TestMainPage1</span></span></span><span class="hljs-params"><span class="hljs-class"><span class="hljs-params">()</span></span></span><span class="hljs-class">:</span></span>

<span class="hljs-meta"><span class="hljs-meta">    @classmethod</span></span>
    <span class="hljs-function"><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-keyword">def</span></span></span><span class="hljs-function"> </span><span class="hljs-title"><span class="hljs-function"><span class="hljs-title">setup_class</span></span></span><span class="hljs-params"><span class="hljs-function"><span class="hljs-params">(self)</span></span></span><span class="hljs-function">:</span></span>
        print(<span class="hljs-string"><span class="hljs-string">"\nstart browser for test suite.."</span></span>)
        self.browser = webdriver.Chrome()

<span class="hljs-meta"><span class="hljs-meta">    @classmethod</span></span>
    <span class="hljs-function"><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-keyword">def</span></span></span><span class="hljs-function"> </span><span class="hljs-title"><span class="hljs-function"><span class="hljs-title">teardown_class</span></span></span><span class="hljs-params"><span class="hljs-function"><span class="hljs-params">(self)</span></span></span><span class="hljs-function">:</span></span>
        print(<span class="hljs-string"><span class="hljs-string">"quit browser for test suite.."</span></span>)
        self.browser.quit()

    <span class="hljs-function"><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-keyword">def</span></span></span><span class="hljs-function"> </span><span class="hljs-title"><span class="hljs-function"><span class="hljs-title">test_guest_should_see_login_link</span></span></span><span class="hljs-params"><span class="hljs-function"><span class="hljs-params">(self)</span></span></span><span class="hljs-function">:</span></span>
        self.browser.get(link)
        self.browser.find_element_by_css_selector(<span class="hljs-string"><span class="hljs-string">"#login_link"</span></span>)

    <span class="hljs-function"><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-keyword">def</span></span></span><span class="hljs-function"> </span><span class="hljs-title"><span class="hljs-function"><span class="hljs-title">test_guest_should_see_basket_link_on_the_main_page</span></span></span><span class="hljs-params"><span class="hljs-function"><span class="hljs-params">(self)</span></span></span><span class="hljs-function">:</span></span>
        self.browser.get(link)
        self.browser.find_element_by_css_selector(<span class="hljs-string"><span class="hljs-string">".basket-mini .btn-group &gt; a"</span></span>)


<span class="hljs-class"><span class="hljs-keyword"><span class="hljs-class"><span class="hljs-keyword">class</span></span></span><span class="hljs-class"> </span><span class="hljs-title"><span class="hljs-class"><span class="hljs-title">TestMainPage2</span></span></span><span class="hljs-params"><span class="hljs-class"><span class="hljs-params">()</span></span></span><span class="hljs-class">:</span></span>

    <span class="hljs-function"><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-keyword">def</span></span></span><span class="hljs-function"> </span><span class="hljs-title"><span class="hljs-function"><span class="hljs-title">setup_method</span></span></span><span class="hljs-params"><span class="hljs-function"><span class="hljs-params">(self)</span></span></span><span class="hljs-function">:</span></span>
        print(<span class="hljs-string"><span class="hljs-string">"start browser for test.."</span></span>)
        self.browser = webdriver.Chrome()

    <span class="hljs-function"><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-keyword">def</span></span></span><span class="hljs-function"> </span><span class="hljs-title"><span class="hljs-function"><span class="hljs-title">teardown_method</span></span></span><span class="hljs-params"><span class="hljs-function"><span class="hljs-params">(self)</span></span></span><span class="hljs-function">:</span></span>
        print(<span class="hljs-string"><span class="hljs-string">"quit browser for test.."</span></span>)
        self.browser.quit()

    <span class="hljs-function"><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-keyword">def</span></span></span><span class="hljs-function"> </span><span class="hljs-title"><span class="hljs-function"><span class="hljs-title">test_guest_should_see_login_link</span></span></span><span class="hljs-params"><span class="hljs-function"><span class="hljs-params">(self)</span></span></span><span class="hljs-function">:</span></span>
        self.browser.get(link)
        self.browser.find_element_by_css_selector(<span class="hljs-string"><span class="hljs-string">"#login_link"</span></span>)

    <span class="hljs-function"><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-keyword">def</span></span></span><span class="hljs-function"> </span><span class="hljs-title"><span class="hljs-function"><span class="hljs-title">test_guest_should_see_basket_link_on_the_main_page</span></span></span><span class="hljs-params"><span class="hljs-function"><span class="hljs-params">(self)</span></span></span><span class="hljs-function">:</span></span>
        self.browser.get(link)
        self.browser.find_element_by_css_selector(<span class="hljs-string"><span class="hljs-string">".basket-mini .btn-group &gt; a"</span></span>)



</code></pre>

<p>В консоли видим:&nbsp;&nbsp;</p>

<p><img alt="" src="https://ucarecdn.com/e4d862f8-8d75-4a59-9387-f967790f8d09/"></p>

<p>Мы видим, что в первом тест-сьюте браузер запустился один раз, а во втором — два раза.</p>

<p>Данные и кэш, оставшиеся от запуска предыдущего теста, могут влиять на результаты выполнения следующего теста, поэтому лучше всего запускать отдельный браузер для каждого теста, чтобы тесты были стабильнее. К тому же если вдруг браузер зависнет в одном тесте, то другие тесты не пострадают, если они запускаются каждый в собственном браузере.</p>

<p>Минусы запуска браузера на каждый тест: каждый&nbsp;запуск и закрытие браузера занимают время, поэтому тесты будут идти дольше. Возможно, вы захотите оптимизировать время прогона тестов, но лучше это делать с помощью других инструментов, которые мы разберём в дальнейшем.</p>

<p>Обычно такие фикстуры переезжают вместе с тестами, написанными с помощью&nbsp;unittest, и приходится их поддерживать,&nbsp;но сейчас&nbsp;все пишут более гибкие&nbsp;фикстуры&nbsp;<strong>@pytest.fixture</strong>, которые мы рассмотрим в следующем шаге.&nbsp;</p></span>



<span><p>пока не сделал принт в каждом тесте чтобы с циферкой, не понял, что как работает, к тому же в коде из примера не видно где какой принт, они же одинаковые, так что я разделил их. Вот результат, надеюсь поможет кому)</p>

<pre><code class="language-python hljs"><span class="hljs-keyword"><span class="hljs-keyword">from</span></span> selenium <span class="hljs-keyword"><span class="hljs-keyword">import</span></span> webdriver

link = <span class="hljs-string"><span class="hljs-string">"http://selenium1py.pythonanywhere.com/"</span></span>


<span class="hljs-class"><span class="hljs-keyword"><span class="hljs-class"><span class="hljs-keyword">class</span></span></span><span class="hljs-class"> </span><span class="hljs-title"><span class="hljs-class"><span class="hljs-title">TestMainPage1</span></span></span><span class="hljs-params"><span class="hljs-class"><span class="hljs-params">()</span></span></span><span class="hljs-class">:</span></span>

<span class="hljs-meta"><span class="hljs-meta">    @classmethod</span></span>
    <span class="hljs-function"><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-keyword">def</span></span></span><span class="hljs-function"> </span><span class="hljs-title"><span class="hljs-function"><span class="hljs-title">setup_class</span></span></span><span class="hljs-params"><span class="hljs-function"><span class="hljs-params">(self)</span></span></span><span class="hljs-function">:</span></span>
        print(<span class="hljs-string"><span class="hljs-string">"\nstart browser for test suite 1 .."</span></span>)
        self.browser = webdriver.Chrome()

<span class="hljs-meta"><span class="hljs-meta">    @classmethod</span></span>
    <span class="hljs-function"><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-keyword">def</span></span></span><span class="hljs-function"> </span><span class="hljs-title"><span class="hljs-function"><span class="hljs-title">teardown_class</span></span></span><span class="hljs-params"><span class="hljs-function"><span class="hljs-params">(self)</span></span></span><span class="hljs-function">:</span></span>
        print(<span class="hljs-string"><span class="hljs-string">"quit browser for test suite 1 .."</span></span>)
        self.browser.quit()

    <span class="hljs-function"><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-keyword">def</span></span></span><span class="hljs-function"> </span><span class="hljs-title"><span class="hljs-function"><span class="hljs-title">test_guest_should_see_login_link</span></span></span><span class="hljs-params"><span class="hljs-function"><span class="hljs-params">(self)</span></span></span><span class="hljs-function">:</span></span>
        print(<span class="hljs-string"><span class="hljs-string">'start test link 1'</span></span>)
        self.browser.get(link)
        self.browser.find_element_by_css_selector(<span class="hljs-string"><span class="hljs-string">"#login_link"</span></span>)

    <span class="hljs-function"><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-keyword">def</span></span></span><span class="hljs-function"> </span><span class="hljs-title"><span class="hljs-function"><span class="hljs-title">test_guest_should_see_basket_link_on_the_main_page</span></span></span><span class="hljs-params"><span class="hljs-function"><span class="hljs-params">(self)</span></span></span><span class="hljs-function">:</span></span>
        print(<span class="hljs-string"><span class="hljs-string">'start test basket 1'</span></span>)
        self.browser.get(link)
        self.browser.find_element_by_css_selector(<span class="hljs-string"><span class="hljs-string">".basket-mini .btn-group &gt; a"</span></span>)


<span class="hljs-class"><span class="hljs-keyword"><span class="hljs-class"><span class="hljs-keyword">class</span></span></span><span class="hljs-class"> </span><span class="hljs-title"><span class="hljs-class"><span class="hljs-title">TestMainPage2</span></span></span><span class="hljs-params"><span class="hljs-class"><span class="hljs-params">()</span></span></span><span class="hljs-class">:</span></span>

    <span class="hljs-function"><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-keyword">def</span></span></span><span class="hljs-function"> </span><span class="hljs-title"><span class="hljs-function"><span class="hljs-title">setup_method</span></span></span><span class="hljs-params"><span class="hljs-function"><span class="hljs-params">(self)</span></span></span><span class="hljs-function">:</span></span>
        print(<span class="hljs-string"><span class="hljs-string">"start browser for test 2.."</span></span>)
        self.browser = webdriver.Chrome()

    <span class="hljs-function"><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-keyword">def</span></span></span><span class="hljs-function"> </span><span class="hljs-title"><span class="hljs-function"><span class="hljs-title">teardown_method</span></span></span><span class="hljs-params"><span class="hljs-function"><span class="hljs-params">(self)</span></span></span><span class="hljs-function">:</span></span>
        print(<span class="hljs-string"><span class="hljs-string">"quit browser for test 2.."</span></span>)
        self.browser.quit()

    <span class="hljs-function"><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-keyword">def</span></span></span><span class="hljs-function"> </span><span class="hljs-title"><span class="hljs-function"><span class="hljs-title">test_guest_should_see_login_link</span></span></span><span class="hljs-params"><span class="hljs-function"><span class="hljs-params">(self)</span></span></span><span class="hljs-function">:</span></span>
        print(<span class="hljs-string"><span class="hljs-string">'start test link 2'</span></span>)
        self.browser.get(link)
        self.browser.find_element_by_css_selector(<span class="hljs-string"><span class="hljs-string">"#login_link"</span></span>)

    <span class="hljs-function"><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-keyword">def</span></span></span><span class="hljs-function"> </span><span class="hljs-title"><span class="hljs-function"><span class="hljs-title">test_guest_should_see_basket_link_on_the_main_page</span></span></span><span class="hljs-params"><span class="hljs-function"><span class="hljs-params">(self)</span></span></span><span class="hljs-function">:</span></span>
        print(<span class="hljs-string"><span class="hljs-string">'start test basket 2'</span></span>)
        self.browser.get(link)
        self.browser.find_element_by_css_selector(<span class="hljs-string"><span class="hljs-string">".basket-mini .btn-group &gt; a"</span></span>)</code></pre>

<p><img alt="" src="https://ucarecdn.com/2c70073d-e3b6-4b7d-96e1-3ff09782c524/"></p></span>



<span><h2>Фикстуры, возвращающие значение</h2>

<p>Мы рассмотрели базовый подход к созданию фикстур, когда тестовые данные задаются и очищаются в setup и teardown методах. PyTest предлагает продвинутый подход к фикстурам, когда фикстуры можно задавать глобально, передавать их в тестовые методы как параметры, а также имеет набор встроенных фикстур. Это более гибкий и удобный способ работы со вспомогательными функциями, и сейчас вы сами увидите&nbsp;почему.&nbsp;</p>

<p><strong>Возвращаемое значение</strong></p>

<p>Фикстуры могут возвращать значение, которое затем&nbsp;можно использовать в тестах. Давайте перепишем наш предыдущий пример с использованием PyTest фикстур. Мы создадим фикстуру <strong>browser</strong>, которая будет создавать объект WebDriver. Этот объект мы сможем использовать в тестах для взаимодействия с браузером. Для этого мы напишем метод browser и укажем, что он является фикстурой с помощью&nbsp;декоратора&nbsp;<strong>@pytest.fixture</strong>. После этого мы можем вызывать фикстуру в тестах, передав ее как параметр. По умолчанию фикстура будет создаваться для каждого тестового метода, то есть&nbsp;для каждого теста запустится свой экземпляр браузера.</p>

<pre><code class="language-python hljs">pytest -s -v test_fixture2.py</code></pre>

<p><strong>test_fixture2.py:</strong></p>

<pre><code class="language-python hljs"><span class="hljs-keyword"><span class="hljs-keyword">import</span></span> pytest
<span class="hljs-keyword"><span class="hljs-keyword">from</span></span> selenium <span class="hljs-keyword"><span class="hljs-keyword">import</span></span> webdriver

link = <span class="hljs-string"><span class="hljs-string">"http://selenium1py.pythonanywhere.com/"</span></span>


<span class="hljs-meta"><span class="hljs-meta">@pytest.fixture</span></span>
<span class="hljs-function"><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-keyword">def</span></span></span><span class="hljs-function"> </span><span class="hljs-title"><span class="hljs-function"><span class="hljs-title">browser</span></span></span><span class="hljs-params"><span class="hljs-function"><span class="hljs-params">()</span></span></span><span class="hljs-function">:</span></span>
    print(<span class="hljs-string"><span class="hljs-string">"\nstart browser for test.."</span></span>)
    browser = webdriver.Chrome()
    <span class="hljs-keyword"><span class="hljs-keyword">return</span></span> browser


<span class="hljs-class"><span class="hljs-keyword"><span class="hljs-class"><span class="hljs-keyword">class</span></span></span><span class="hljs-class"> </span><span class="hljs-title"><span class="hljs-class"><span class="hljs-title">TestMainPage1</span></span></span><span class="hljs-params"><span class="hljs-class"><span class="hljs-params">()</span></span></span><span class="hljs-class">:</span></span>
    <span class="hljs-comment"><span class="hljs-comment"># вызываем фикстуру в тесте, передав ее как параметр</span></span>
    <span class="hljs-function"><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-keyword">def</span></span></span><span class="hljs-function"> </span><span class="hljs-title"><span class="hljs-function"><span class="hljs-title">test_guest_should_see_login_link</span></span></span><span class="hljs-params"><span class="hljs-function"><span class="hljs-params">(self, browser)</span></span></span><span class="hljs-function">:</span></span>
        browser.get(link)
        browser.find_element_by_css_selector(<span class="hljs-string"><span class="hljs-string">"#login_link"</span></span>)

    <span class="hljs-function"><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-keyword">def</span></span></span><span class="hljs-function"> </span><span class="hljs-title"><span class="hljs-function"><span class="hljs-title">test_guest_should_see_basket_link_on_the_main_page</span></span></span><span class="hljs-params"><span class="hljs-function"><span class="hljs-params">(self, browser)</span></span></span><span class="hljs-function">:</span></span>
        browser.get(link)
        browser.find_element_by_css_selector(<span class="hljs-string"><span class="hljs-string">".basket-mini .btn-group &gt; a"</span></span>)
</code></pre></span>



<span><p>Чтобы лучше понять, что такое фикстура разберитесь с таким понятием в питоне как Декоратор</p>

<p>Декоратор — это функция, которая позволяет обернуть другую функцию для расширения её функциональности без непосредственного изменения её кода.</p>

<p>Пример</p>

<pre><code class="hljs python"><span class="hljs-function"><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-keyword">def</span></span></span><span class="hljs-function"> </span><span class="hljs-title"><span class="hljs-function"><span class="hljs-title">decorator_function</span></span></span><span class="hljs-params"><span class="hljs-function"><span class="hljs-params">(func)</span></span></span><span class="hljs-function">:</span></span>
    <span class="hljs-function"><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-keyword">def</span></span></span><span class="hljs-function"> </span><span class="hljs-title"><span class="hljs-function"><span class="hljs-title">wrapper</span></span></span><span class="hljs-params"><span class="hljs-function"><span class="hljs-params">()</span></span></span><span class="hljs-function">:</span></span>
        print(<span class="hljs-string"><span class="hljs-string">'Функция-обёртка!'</span></span>)
        print(<span class="hljs-string"><span class="hljs-string">'Оборачиваемая функция: {}'</span></span>.format(func))
        print(<span class="hljs-string"><span class="hljs-string">'Выполняем обёрнутую функцию...'</span></span>)
        func()
        print(<span class="hljs-string"><span class="hljs-string">'Выходим из обёртки'</span></span>)
    <span class="hljs-keyword"><span class="hljs-keyword">return</span></span> wrapper

<span class="hljs-meta"><span class="hljs-meta">@decorator_function</span></span>
<span class="hljs-function"><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-keyword">def</span></span></span><span class="hljs-function"> </span><span class="hljs-title"><span class="hljs-function"><span class="hljs-title">hello_world</span></span></span><span class="hljs-params"><span class="hljs-function"><span class="hljs-params">()</span></span></span><span class="hljs-function">:</span></span>
    print(<span class="hljs-string"><span class="hljs-string">'Hello world!'</span></span>)

hello_world()</code></pre></span>


<span><h2>Финализаторы — закрываем браузер</h2>

<p>Вероятно, вы заметили, что мы не использовали в этом примере команду <strong>browser.quit()</strong>. Это привело к тому, что несколько окон браузера оставались открыты после окончания тестов, а закрылись только после завершения всех тестов. Закрытие браузеров произошло благодаря встроенной фикстуре — сборщику мусора. Но если бы количество тестов насчитывало&nbsp;больше нескольких десятков, то открытые окна браузеров&nbsp;могли привести к тому, что оперативная память закончилась бы очень быстро. Поэтому надо явно закрывать браузеры после каждого теста. Для этого мы можем воспользоваться <strong>финализаторами</strong>. Один из вариантов финализатора — использование ключевого слова Python: <strong>yield</strong>. После завершения теста, который вызывал фикстуру, выполнение фикстуры продолжится со строки, следующей за строкой со словом <strong>yield</strong>:</p>

<p>test_fixture3.py</p>

<pre><code class="language-python hljs"><span class="hljs-keyword"><span class="hljs-keyword">import</span></span> pytest
<span class="hljs-keyword"><span class="hljs-keyword">from</span></span> selenium <span class="hljs-keyword"><span class="hljs-keyword">import</span></span> webdriver

link = <span class="hljs-string"><span class="hljs-string">"http://selenium1py.pythonanywhere.com/"</span></span>


<span class="hljs-meta"><span class="hljs-meta">@pytest.fixture</span></span>
<span class="hljs-function"><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-keyword">def</span></span></span><span class="hljs-function"> </span><span class="hljs-title"><span class="hljs-function"><span class="hljs-title">browser</span></span></span><span class="hljs-params"><span class="hljs-function"><span class="hljs-params">()</span></span></span><span class="hljs-function">:</span></span>
    print(<span class="hljs-string"><span class="hljs-string">"\nstart browser for test.."</span></span>)
    browser = webdriver.Chrome()
    <span class="hljs-keyword"><span class="hljs-keyword">yield</span></span> browser
    <span class="hljs-comment"><span class="hljs-comment"># этот код выполнится после завершения теста</span></span>
    print(<span class="hljs-string"><span class="hljs-string">"\nquit browser.."</span></span>)
    browser.quit()


<span class="hljs-class"><span class="hljs-keyword"><span class="hljs-class"><span class="hljs-keyword">class</span></span></span><span class="hljs-class"> </span><span class="hljs-title"><span class="hljs-class"><span class="hljs-title">TestMainPage1</span></span></span><span class="hljs-params"><span class="hljs-class"><span class="hljs-params">()</span></span></span><span class="hljs-class">:</span></span>
    <span class="hljs-comment"><span class="hljs-comment"># вызываем фикстуру в тесте, передав ее как параметр</span></span>
    <span class="hljs-function"><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-keyword">def</span></span></span><span class="hljs-function"> </span><span class="hljs-title"><span class="hljs-function"><span class="hljs-title">test_guest_should_see_login_link</span></span></span><span class="hljs-params"><span class="hljs-function"><span class="hljs-params">(self, browser)</span></span></span><span class="hljs-function">:</span></span>
        browser.get(link)
        browser.find_element_by_css_selector(<span class="hljs-string"><span class="hljs-string">"#login_link"</span></span>)

    <span class="hljs-function"><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-keyword">def</span></span></span><span class="hljs-function"> </span><span class="hljs-title"><span class="hljs-function"><span class="hljs-title">test_guest_should_see_basket_link_on_the_main_page</span></span></span><span class="hljs-params"><span class="hljs-function"><span class="hljs-params">(self, browser)</span></span></span><span class="hljs-function">:</span></span>
        browser.get(link)
        browser.find_element_by_css_selector(<span class="hljs-string"><span class="hljs-string">".basket-mini .btn-group &gt; a"</span></span>)
</code></pre>

<p>Есть альтернативный способ вызова teardown кода с помощью встроенной фикстуры <strong>request</strong> и ее метода <strong>addfinalizer</strong>. Можете изучить его сами по документации <a href="https://docs.pytest.org/en/latest/fixture.html#fixture-finalization-executing-teardown-code" rel="nofollow noopener noreferrer" target="_blank">PyTest</a>.&nbsp;</p>

<p>Рекомендуем также&nbsp;выносить очистку данных и памяти в фикстуру, вместо того чтобы писать это в шагах теста: финализатор выполнится даже в ситуации, когда тест упал с ошибкой.&nbsp;</p></span>




<span><p>Мне для осознания примера помогла вот эта&nbsp;статья:&nbsp;<a href="https://medium.com/@dmrlx/%D0%B2%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5-%D0%B2-pytest-cc6175c7d0dc" rel="noopener noreferrer nofollow" target="_blank">Статья целиком</a></p>

<p>Кратко из статьи:</p>

<p>Фикстурами в PyTest'е называют функции, которые выполняются с различным scope-ом и возвращают какое-то значение либо выполняют какие-то действия.</p>

<p>Пример:&nbsp;</p>

<pre><code class="language-python hljs"><span class="hljs-keyword"><span class="hljs-keyword">import</span></span> time
<span class="hljs-keyword"><span class="hljs-keyword">import</span></span> pytest

<span class="hljs-meta"><span class="hljs-meta">@pytest.fixture(scope='class', autouse=True)</span></span>
<span class="hljs-function"><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-keyword">def</span></span></span><span class="hljs-function"> </span><span class="hljs-title"><span class="hljs-function"><span class="hljs-title">suite_data</span></span></span><span class="hljs-params"><span class="hljs-function"><span class="hljs-params">()</span></span></span><span class="hljs-function">:</span></span>
&nbsp; &nbsp; print(<span class="hljs-string"><span class="hljs-string">"\n&gt; Suite setup"</span></span>)
&nbsp; &nbsp; <span class="hljs-keyword"><span class="hljs-keyword">yield</span></span>
&nbsp; &nbsp; print(<span class="hljs-string"><span class="hljs-string">"&gt; Suite teardown"</span></span>)</code></pre>

<p>&nbsp;&nbsp; &nbsp;<br>
В данном примере “@pytest.fixture” — декоратор, указывающий, что функция ниже является фикстурой, “scope=’…’” указывает на “очерёдность” выполнения, а “autouse=True” говорит о том, что фикстура будет применена для каждого сьюта в тестовом фреймворке</p>

<p>Очерёдность выполнения - их четыре: “session”, “module”, “class” и “function”. Выполняются они в такой же последовательности.</p>

<p>Из фикстуры можно передать значение в сьют с помощью оператора yield. При этом после yield можно добавить ещё код, который будет выполнен после кейса. Таким образом можно сказать, что <u><strong>всё, что идёт до оператора yield является “setup”</strong></u>, а <strong><u>всё, что после — “teardown” </u></strong>(yield, к слову, может ничего и не возвращать, а просто будет разделителем, отделяющим сетап от тирдауна).</p></span>


<span><p><strong>@Pavel_Vasin</strong>, генератор выполняется до тех пор пока не встретит yield, после этого он останавливает выполнение и возвращает значение, потом можно снова вызвать генератор и он продолжит свое выполнение до тех пор пока не дойдет до конца кода генератора, если код не скрывать и я все правильно понимаю, то это нечто следующее:</p>

<pre><code class="language-python hljs"><span class="hljs-function"><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-keyword">def</span></span></span><span class="hljs-function"> </span><span class="hljs-title"><span class="hljs-function"><span class="hljs-title">simple_generator</span></span></span><span class="hljs-params"><span class="hljs-function"><span class="hljs-params">()</span></span></span><span class="hljs-function">:</span></span>
     print(<span class="hljs-string"><span class="hljs-string">'generator starts working'</span></span>)
     <span class="hljs-keyword"><span class="hljs-keyword">yield</span></span> <span class="hljs-number"><span class="hljs-number">42</span></span>
     print(<span class="hljs-string"><span class="hljs-string">'generator stopped working'</span></span>)

gen = simple_generator()
value = next(gen)
print(value)

<span class="hljs-comment"><span class="hljs-comment"># Тут появится исключение StopIteration и генератор закончит свое выполнение, кроме того, если</span></span>
<span class="hljs-comment"><span class="hljs-comment"># захотим снова использовать генератор, то придется создавать новый объект генератора, потому что # прошлый истощился</span></span>
next(gen)

<span class="hljs-comment"><span class="hljs-comment"># Из-за возникновения StopIteration генераторы можно использовать в цикле for и тут </span></span>
<span class="hljs-comment"><span class="hljs-comment"># StopIteration будет скрыт циклом</span></span>
<span class="hljs-keyword"><span class="hljs-keyword">for</span></span> i <span class="hljs-keyword"><span class="hljs-keyword">in</span></span> simple_generator(): <span class="hljs-keyword"><span class="hljs-keyword">pass</span></span></code></pre>

<p>И yield может быть несколько, не обязательно один и каждый раз работа его будет приостанавливаться</p></span>


<span><h2>Область видимости scope</h2>

<p>Для фикстур можно задавать область покрытия фикстур. Допустимые значения: “<strong>function</strong>”, “<strong>class</strong>”, “<strong>module</strong>”, “<strong>session</strong>”. Соответственно, фикстура будет вызываться один раз для тестового метода, один раз для класса, один раз для модуля или один раз для всех тестов, запущенных в данной сессии.&nbsp;</p>

<p>Запустим все наши тесты из класса <strong>TestMainPage1</strong> в одном браузере для экономии времени, задав scope="class" в фикстуре browser:</p>

<p>test_fixture5.py</p>

<pre><code class="language-python hljs"><span class="hljs-keyword"><span class="hljs-keyword">import</span></span> pytest
<span class="hljs-keyword"><span class="hljs-keyword">from</span></span> selenium <span class="hljs-keyword"><span class="hljs-keyword">import</span></span> webdriver

link = <span class="hljs-string"><span class="hljs-string">"http://selenium1py.pythonanywhere.com/"</span></span>


<span class="hljs-meta"><span class="hljs-meta">@pytest.fixture(scope="class")</span></span>
<span class="hljs-function"><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-keyword">def</span></span></span><span class="hljs-function"> </span><span class="hljs-title"><span class="hljs-function"><span class="hljs-title">browser</span></span></span><span class="hljs-params"><span class="hljs-function"><span class="hljs-params">()</span></span></span><span class="hljs-function">:</span></span>
    print(<span class="hljs-string"><span class="hljs-string">"\nstart browser for test.."</span></span>)
    browser = webdriver.Chrome()
    <span class="hljs-keyword"><span class="hljs-keyword">yield</span></span> browser
    print(<span class="hljs-string"><span class="hljs-string">"\nquit browser.."</span></span>)
    browser.quit()


<span class="hljs-class"><span class="hljs-keyword"><span class="hljs-class"><span class="hljs-keyword">class</span></span></span><span class="hljs-class"> </span><span class="hljs-title"><span class="hljs-class"><span class="hljs-title">TestMainPage1</span></span></span><span class="hljs-params"><span class="hljs-class"><span class="hljs-params">()</span></span></span><span class="hljs-class">:</span></span>

    <span class="hljs-comment"><span class="hljs-comment"># вызываем фикстуру&nbsp;в&nbsp;тесте,&nbsp;передав&nbsp;ее&nbsp;как&nbsp;параметр</span></span>
    <span class="hljs-function"><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-keyword">def</span></span></span><span class="hljs-function"> </span><span class="hljs-title"><span class="hljs-function"><span class="hljs-title">test_guest_should_see_login_link</span></span></span><span class="hljs-params"><span class="hljs-function"><span class="hljs-params">(self, browser)</span></span></span><span class="hljs-function">:</span></span>
        print(<span class="hljs-string"><span class="hljs-string">"start test1"</span></span>)
        browser.get(link)
        browser.find_element_by_css_selector(<span class="hljs-string"><span class="hljs-string">"#login_link"</span></span>)
        print(<span class="hljs-string"><span class="hljs-string">"finish test1"</span></span>)

    <span class="hljs-function"><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-keyword">def</span></span></span><span class="hljs-function"> </span><span class="hljs-title"><span class="hljs-function"><span class="hljs-title">test_guest_should_see_basket_link_on_the_main_page</span></span></span><span class="hljs-params"><span class="hljs-function"><span class="hljs-params">(self, browser)</span></span></span><span class="hljs-function">:</span></span>
        print(<span class="hljs-string"><span class="hljs-string">"start test2"</span></span>)
        browser.get(link)
        browser.find_element_by_css_selector(<span class="hljs-string"><span class="hljs-string">".basket-mini .btn-group &gt; a"</span></span>)
        print(<span class="hljs-string"><span class="hljs-string">"finish test2"</span></span>)
</code></pre>

<p>Мы видим, что в данном примере браузер открылся один раз&nbsp;и тесты последовательно выполнились в этом браузере. Здесь мы проделали это в качестве примера, но мы крайне рекомендуем всё же запускать отдельный экземпляр браузера для каждого теста, чтобы повысить стабильность тестов. Фикстуры, которые занимают много времени для запуска и ресурсов (обычно это работа с базами данных), можно вызывать и один раз за сессию запуска тестов.</p></span>




<span><p>Для тех кто хочет более подробно разобраться в работе&nbsp;<a href="https://habr.com/ru/post/132554/" rel="noopener noreferrer nofollow" target="_blank">yield</a></p></span>


<span><p><br>
Олег Молчанов про yield <a href="https://www.youtube.com/watch?v=ZjaVrzOkpZk" rel="noopener noreferrer nofollow" target="_blank">https://www.youtube.com/watch?v=ZjaVrzOkpZk</a><br>
Ну и Лутца читайте</p></span>

<span><p>Вот ещё одна интересная и понятная статься по основам&nbsp;<a href="https://medium.com/@dmrlx/%D0%B2%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5-%D0%B2-pytest-cc6175c7d0dc" rel="noopener noreferrer nofollow" target="_blank">PyTest</a></p></span>



<span><h2>Автоиспользование фикстур</h2>

<p>При описании фикстуры можно указать дополнительный параметр <strong>autouse=True,</strong> который укажет, что фикстуру нужно запустить для каждого теста&nbsp;даже без явного вызова:&nbsp;</p>

<p>test_fixture_autouse.py</p>

<pre><code class="language-python hljs"><span class="hljs-keyword"><span class="hljs-keyword">import</span></span> pytest
<span class="hljs-keyword"><span class="hljs-keyword">from</span></span> selenium <span class="hljs-keyword"><span class="hljs-keyword">import</span></span> webdriver

link = <span class="hljs-string"><span class="hljs-string">"http://selenium1py.pythonanywhere.com/"</span></span>


<span class="hljs-meta"><span class="hljs-meta">@pytest.fixture</span></span>
<span class="hljs-function"><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-keyword">def</span></span></span><span class="hljs-function"> </span><span class="hljs-title"><span class="hljs-function"><span class="hljs-title">browser</span></span></span><span class="hljs-params"><span class="hljs-function"><span class="hljs-params">()</span></span></span><span class="hljs-function">:</span></span>
    print(<span class="hljs-string"><span class="hljs-string">"\nstart browser for test.."</span></span>)
    browser = webdriver.Chrome()
    <span class="hljs-keyword"><span class="hljs-keyword">yield</span></span> browser
    print(<span class="hljs-string"><span class="hljs-string">"\nquit browser.."</span></span>)
    browser.quit()

<span class="hljs-meta"><span class="hljs-meta">@pytest.fixture(autouse=True)</span></span>
<span class="hljs-function"><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-keyword">def</span></span></span><span class="hljs-function"> </span><span class="hljs-title"><span class="hljs-function"><span class="hljs-title">prepare_data</span></span></span><span class="hljs-params"><span class="hljs-function"><span class="hljs-params">()</span></span></span><span class="hljs-function">:</span></span>
    print()
    print(<span class="hljs-string"><span class="hljs-string">"preparing some critical data for every test"</span></span>)


<span class="hljs-class"><span class="hljs-keyword"><span class="hljs-class"><span class="hljs-keyword">class</span></span></span><span class="hljs-class"> </span><span class="hljs-title"><span class="hljs-class"><span class="hljs-title">TestMainPage1</span></span></span><span class="hljs-params"><span class="hljs-class"><span class="hljs-params">()</span></span></span><span class="hljs-class">:</span></span>
    <span class="hljs-function"><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-keyword">def</span></span></span><span class="hljs-function"> </span><span class="hljs-title"><span class="hljs-function"><span class="hljs-title">test_guest_should_see_login_link</span></span></span><span class="hljs-params"><span class="hljs-function"><span class="hljs-params">(self, browser)</span></span></span><span class="hljs-function">:</span></span>
        <span class="hljs-comment"><span class="hljs-comment"># не передаём как параметр фикстуру prepare_data, но она все равно выполняется</span></span>
        browser.get(link)
        browser.find_element_by_css_selector(<span class="hljs-string"><span class="hljs-string">"#login_link"</span></span>)

    <span class="hljs-function"><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-keyword">def</span></span></span><span class="hljs-function"> </span><span class="hljs-title"><span class="hljs-function"><span class="hljs-title">test_guest_should_see_basket_link_on_the_main_page</span></span></span><span class="hljs-params"><span class="hljs-function"><span class="hljs-params">(self, browser)</span></span></span><span class="hljs-function">:</span></span>
        browser.get(link)
        browser.find_element_by_css_selector(<span class="hljs-string"><span class="hljs-string">".basket-mini .btn-group &gt; a"</span></span>)
</code></pre>

<p><img alt="" src="https://ucarecdn.com/0b70e723-548a-4b94-b01c-f5ff19ae3bfb/"></p>

<p>Попробуйте запустить этот код и увидите, что для каждого теста&nbsp;фикстура подготовки данных выполнилась без явного вызова. Нужно быть аккуратнее с этим параметром, потому что фикстура выполняется для всех тестов. Без явной необходимости автоиспользованием фикстур лучше не пользоваться.&nbsp;</p>

<p><strong>Итог</strong></p>

<p>Вспомогательные функции — это очень мощная штука, которая решает много проблем при работе с автотестами. Основной плюс в том, что их удобно использовать в любых тестах без дублирования лишнего кода.&nbsp;</p>

<p>Дополнительные материалы про&nbsp;фикстуры, которые мы настоятельно советуем почитать, приведены ниже:</p>

<p><a href="https://habr.com/ru/company/yandex/blog/242795/" rel="noopener noreferrer nofollow" target="_blank">https://habr.com/ru/company/yandex/blog/242795/</a></p>

<p><a href="https://docs.pytest.org/en/latest/fixture.html" rel="noopener noreferrer nofollow" target="_blank">https://docs.pytest.org/en/latest/fixture.html</a></p></span>



<span><p>Для тех, кто всё прочёл-выучил начал писать тесты и понял, что чего-то не понял (читай таких, как я) и для тех, кто понятия не имеет как использовать классы в python&nbsp;я подготовил шпаргалку об использовании фикстур и классов. Мб кому пригодится)&nbsp;<a href="https://github.com/JakUi/stepik-auto-tests-course/blob/master/%D0%A4%D0%B8%D0%BA%D1%81%D1%82%D1%83%D1%80%D1%8B%20%D0%B8%20%D0%BA%D0%BB%D0%B0%D1%81%D1%81%D1%8B.txt" rel="noopener noreferrer nofollow" target="_blank">https://github.com/JakUi/stepik-auto-tests-course/blob/master/%D0%A4%D0%B8%D0%BA%D1%81%D1%82%D1%83%D1%80%D1%8B%20%D0%B8%20%D0%BA%D0%BB%D0%B0%D1%81%D1%81%D1%8B.txt</a></p></span>


<span><p>Вот здесь хорошая документация:&nbsp;<a href="https://habr.com/ru/post/426699/" rel="noopener noreferrer nofollow" target="_blank">https://habr.com/ru/post/426699/</a></p></span>


