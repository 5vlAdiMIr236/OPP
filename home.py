# Запросить у пользователя ввод имени и возраста
name = input("Введите ваше имя: ")
age = input("Введите ваш возраст: ")
# Вывести сообщение с именем и возрастом пользователя
print("Привет," + name + "! Тебе " + age )

age = int(input("Введите ваш возраст: "))
if age >= 18:
    print("Вход разрешён")
else:
    print("Вход запрещён")

import random
secret = random.randint(1, 10)
attempts = 0
while True:
    guess = int(input("Введите число: "))
    attempts += 1
    if guess < secret:
        print("Число меньше, чем нужно. Попробуйте ещё раз!")
    elif guess > secret:
        print("Число больше, чем нужно. Попробуйте ещё раз!")
    else:
        print("Вы угадали! Число попыток:", attempts)
        break
