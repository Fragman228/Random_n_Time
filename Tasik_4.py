from time import *

def punishment(seconds):
    print(f'Вы были удалены на {seconds} минут')
    sleep(seconds)
    return "Возвращайтесь на поле!"

print(punishment(int(input("Удалить с поля?  "))))