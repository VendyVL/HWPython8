from time import time


def Logging(a,b):
    t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    log = open('log.txt', 'w', encoding='utf-8')
    log.write(f'{t}: {a}: {b}')
