from random import randint
from time import sleep

first_dice = 0
second_dice = 0

while True:
    Start = input("Напишите старт чтобы бросить кубики:  ")
    if Start == "старт":
        print("Бросаю кубики")
        first_dice = randint(1, 6)
        second_dice = randint(1, 6)
        sleep(2)
        print(f"Выпало на Первом кубике: {first_dice}, на Втором кубике: {second_dice}")
    else:
        break
