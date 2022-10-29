from time import *

def chess(step):
    tm = time()
    while True:
        step = input()
        b = time()
        f = round(b - tm, 2)
        if step == "off":
            break
        print(f"Оставшееся время: {1800 - f}")
        if f == 1800:
            break
    return 'Игра окончена'


print(chess((input("Введите ваш ход:\n"))))
