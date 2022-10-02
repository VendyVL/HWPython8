from logging import Logging

def Searching():
    dict = open('employees.txt', 'r', encoding='utf-8')

    a = input('Кого ищем? ')

    for line in dict:
        if a in line:
            print (line)
            Logging('Поиск', a)
    dict.close