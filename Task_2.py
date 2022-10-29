from random import *
b = []
c = []
def sportsmen(name):
    while True:
        for i in range(name):
            b.append(i)
        for k in range(name//2):
            n = randint(1, len(b))
            f = randint(n, len(b))
            h = [f"Пловец {n}: Пловец {f}"]
            c.append(h)
        break
    return c

print(sportsmen(int(input("Введите колво пловцов:\n"))))
