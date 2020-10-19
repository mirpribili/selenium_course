# Stepik---selenium-python-course

This is a repository for saving the codes from the course on learning python test automation by Selenium [link](https://stepik.org/lesson/187065/step/7?unit=161976)

## How to start in mitn OS
### View another page
- **[help selenium](/Help_Selenium.md)**
- **[help testing](/testing.md)**
- **[story](/story.md)**
- **[help pytest](/pytest.md)**
- **[help freez](/freez.md)**

#### STEP 1
- conda deactivate
- conda activate

- sudo apt-get update && sudo apt-get upgrade
- sudo apt-get install python3.7
- python3.7 --version
- nano ~/.bashrc
- - add string
- - - alias python3=python3.7
- source ~/.bashrc
- conda deactivate
- python3 -m pip install pip
- IF ERROR
- sudo apt install python3-pip
- sudo apt-get install -y python3.7-venv
- cd $HOME
- mkdir enviroments
- cd enviroments
- python3 -m venv selenium_env
- source selenium_env/bin/activate
- - deactivate
-
- source selenium_env/bin/activate
- python
- print("Hello, Selenium!")
- exit()
- cd $HOME/enviroments;source selenium_env/bin/activate
- $HOME/enviroments/selenium_env/bin/python3.7 -m pip install --upgrade pip
- pip install selenium==3.14.0
- pip list

#### STEP 2
- cd $HOME/enviroments/selenium_env/chromedriver86
- sudo mv chromedriver /usr/local/bin/chromedriver
- sudo chown root:root /usr/local/bin/chromedriver
- sudo chmod +x /usr/local/bin/chromedriver
- chromedriver
- 
- mkdir ~/selenium_course
-  mv  ~/Загрузки/get_method.py ~/selenium_course
- python  ~/selenium_course/get_method.py
- - IF --> Current browser version is 83.0.4103.106 with binary path /usr/bin/google-chrome
- - - https://sites.google.com/a/chromium.org/chromedriver/downloads --> https://chromedriver.storage.googleapis.com/index.html?path=83.0.4103.14/
- - - GO TO STEP 2
- 
- cd $HOME/enviroments/selenium_env/chromedriver83
- sudo cp chromedriver /usr/local/bin/chromedriver
- sudo chown root:root /usr/local/bin/chromedriver
- sudo chmod +x /usr/local/bin/chromedriver
- chromedriver
- - ctrl+c

#### STEP 3
- cd $HOME
- git --version
- **git clone https://github.com/mirpribili/selenium_course.git**
- cd $HOME/selenium_course
- git status
- git remote set-url origin git@github.com:mirpribili/selenium_course.git
- git remote -v
- git status
- git add .
- git commit -m "test ssh Version 1.0"
- git push origin

#### STEP 4
- git add .;git commit -m "Add help Selentium.md";git push origin
- 
- conda deactivate; source $HOME/enviroments/selenium_env/bin/activate
- python  ~/selenium_course/lesson6_step4.py ~

#### STEP 5
- **cd $HOME/selenium_course;python  ~/selenium_course/lesson2_item2_step8.py**
- **conda deactivate; source $HOME/enviroments/selenium_env/bin/activate; cd $HOME/selenium_course;python  ~/selenium_course/lesson2_item2_step8.py**
- **cd $HOME/selenium_course;git add .;git commit -m "Add help Selentium.md";git push origin**
- 

#### STEP 6
- cd $HOME/selenium_course;python  ~/selenium_course/os_mint.py
- **cd $HOME/selenium_course;sudo python os_mint.py**

#### STEP 7
- pip install pytest==5.1.1
- 

#### STEP 8
- pip freeze > requirements.txt
- - *Эта команда сохранит все версии пакетов в специальный файл requirements.txt.
Как их оттуда достать? Попробуйте создать новое виртуальное окружение (если нужно, вернитесь в модуль 1 за инструкциями) и активировать. После чего выполните команду:*
- pip install -r requirements.txt

#### STEP9
- cd $HOME
- **git clone https://github.com/mirpribili/selenium_course__pytest_language.git**
- cd selenium_course__pytest_language
- git --version
- git status
- git remote set-url origin git@github.com:mirpribili/selenium_course__pytest_language.git
- git remote -v
- git status
- git add .;git commit -m "add readme";git push origin



##### Пример хороших сообщений:  

- "add readme"
- "initial commit"
- "simple test case added"
- "homework from previous module"

##### Пример плохих сообщений:

- "commit message"
- "commit1"
- "asdasdads"
- "something"



##### OFF TOP
- NO
- - sudo apt install dsniff
- - sudo tcpkill -i enp0s29f7u2 port 80
- - sudo tcpkill -i enp0s29f7u2 host www.ya.ru
- OK [source](http://itisgood.ru/2018/10/02/kak-perezagruzit-set-v-ubuntu/)
- - sudo service network-manager restart
- - - ping -c 1 homeserver >/dev/null && echo 'Successfully pinged device!'
- - - ping 8.8.8.8 -i 2 >/dev/null && echo 'Successfully pinged device!'
- - - ping -c 1 127.0.0.1 &> /dev/null && echo success || echo fail
- - ping -c 1 8.8.8.8 &> /dev/null && echo success || sudo service network-manager restart

##### LINK TEST AND RELOAD
- 
- sudo apt  install nmap
- nmap -sn -oG status.txt -v 192.168.1.0/24

>	_ ▲		◄--		_ |		--►
>	_ |		_ _		_ ▼		_ _

>	◄--		_ ▲		--►		▲ _		◄--		_ |		--►		| _		◄--
>	─ ─		_ |		_ _		| _		_ _		_ ▼		_ _		▼ _		_ _



