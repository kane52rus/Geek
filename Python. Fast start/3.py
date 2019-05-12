import os
import psutil
import sys


name = input("Ваше имя? ")
print("hello, ", name)

work = input("Давайте поработаем? (Y/N) ")

if work == 'y':
    print("Let`s go! Я могу сделать: ")
    print("[1] Выведу список файлов ")
    print("[2] Выведу информацию о системе")
    print("[3] Выведу все процессы")
    do = int(input("Укажите, что для Вас сделать: "))

    if do == 1:
        print(os.listdir())
    elif do == 2:
        print('File system coding:', sys.getfilesystemencoding())
        print('Platform:', sys.platform)
        print('CPU number:', os.cpu_count())
        print('Login:', os.getlogin())
        print('Current directory:', os.getcwd())
    elif do == 3:
        print(psutil.pids())
    else:
        pass


elif work == 'n':
    print("Жаль!")
else:
    print("dont right")