import random

import pendulum


'''
1. Configure a Python interpreter in PyCharm:

a. Windows: File > Settings > Project: your project name > project interpreter > select one interpreter from 
dropdown list. If no interpreters existing, select a Python interpreter and create a (virtual) env. 

b.
'''


'''
2. PyCharm Env uses a different prompt called "Terminal".  Shortcut windows: alt + F12
'''

'''
3.
Installation:
& pip install module_name
e.g. pip install pendulum


Uninstallation:
& pip uninstall module_name
e.g. pip uninstall pendulum

Install a specific version of a module:
& pip install module_name==version No. (if error, return a list of versions. )
e.g. pip install pendulum==2.0.0

Upgrade:
& pip install module_name --upgrade
e.g. pip install pendulum --upgrade

'''


lst = [1, 2, 3, 4, 5, 6]
dice = random.choice(lst)
print(dice)
