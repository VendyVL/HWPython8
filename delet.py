import os
from logging import Logging

def Deleting():
    dict = open('employees.txt', 'w', encoding='utf-8')
    tem = open('temp.txt', 'w', encoding='utf-8')
    a = input('Введите ID сотрудника ')
    for line in dict:
        if a not in line:
             tem.write(line, + '/n')
    tem.close         
    dict.close
    os.remove(dict)
    os.rename(tem, dict)
    Logging('Удаление', a)