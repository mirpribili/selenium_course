# How to start

## mint CMD

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
- 
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
- 
#### STEP 3
- cd $HOME
- git --version
- git clone https://github.com/mirpribili/selenium_course.git
- cd $HOME/selenium_course
- git status
- git remote set-url origin git@github.com:mirpribili/selenium_course.git
- git remote -v
- git status
- git add .
- git commit -m "test ssh Version 1.0"
- git push origin
- 
#### STEP 4
- git add .;git commit -m "Add help Selentium.md";git push origin
- 
- conda deactivate; source $HOME/enviroments/selenium_env/bin/activate
- python  ~/selenium_course/lesson6_step4.py
- 
- 
- 
- 
- 
- 
- 
- 
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