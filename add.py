from logging import Logging

def Add():
    w = open('employees.txt', 'a')
    a = input("ID (А000): ")
    for line in w:
        if a not in line:# Это на случай, если у меня будет два Иванова и я захочу потом одного удалить
            w.write(f"ID: " + {a} + "; ")
            w.write(f"Фамилия: " + input("Фамилия: ") + "; ")
            w.write(f"Имя: " + input("Имя: ") + "; ")
            w.write(f"Отчество: " + input("Отчество:: ") + "; ")
            w.write(f"Должность: " + input("Должность: ") + "; ")
            w.write(f"Номер телефона: " + input("Номер телефона: ") + ";")
            w.write(f"Зарплата: " + input("Зарплата: ") + "\n") 
            # Было бы интересно сделать отдельные документы для зарплаты, личных данных и остального с доступом по ID, но навигация путанная
            Logging('Добавление', a)
        else:  print('Такой ID уже существует') 
    w.close