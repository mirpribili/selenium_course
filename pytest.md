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


