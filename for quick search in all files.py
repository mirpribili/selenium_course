"""
https://coursehunter.net/course/python-razrabotchik
https://coursehunter.net/course/full-stack-delaem-klon-airbnb-s-python-django-tailwind
DOPOLNITELNO https://coursehunter.net/course/python-django-dev-to-deployment
https://coursehunter.net/course/izuchite-python-i-eticheskiy-vzlom-s-nulya
https://coursehunter.net/course/fullstack-flask-sozdayte-prilozhenie-saas-s-pomoshchyu-flask
https://coursehunter.net/course/rest-apis-s-flask-i-python
"""

import os
from os.path import abspath

name_file = os.path.basename(__file__)
len_name = len(name_file)

directory = abspath(__file__)
directory = directory[0:-len_name]

print("*"+directory)

files = os.listdir(directory)
print("files:", files)

py = filter(lambda x: x.endswith('.py'), files)
print(" -"*25)


name_file_result = name_file[0:-3]+'_RESULT.py'
all_texts = ""

for p in py:
	if p != name_file_result:
		print(p)

		f = open(p)
		#print(f.read())
		all_texts += "\n############ " + p + "\n"
		all_texts += f.read()
		all_texts += "\n#" + "- "*100

		f.close()

#print(all_texts)

f = open(name_file_result, 'w')
f.write(all_texts + '\n')
f.close()

print("OK")
