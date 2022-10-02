from add import Add
from search import Searching
from delet import Deleting

def Click():
    print('1 - Добавить сотрудника')
    print('2 - Найти сотрудника')
    print('3 - Удалить сотрудника')

    doing = input('Выберите действие: ')

    if doing == '1': Add()
    elif doing == '2':Searching()
    elif doing == '3':Deleting()
    else: print('Ошибка')