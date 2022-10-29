import random
from random import *

def zabeg(num):
    zabeg1 = []
    zabeg2 = []
    while True:
        num = input("Ваш номер: ")
        n = randint(1, 2)
        if n == 1:
            zabeg1.append(num)
        else:
            zabeg2.append(num)
        if num == '':
            break
    return f'Команда 1: {zabeg1}\nКоманда 2: {zabeg2}'

print(zabeg(input("")))
