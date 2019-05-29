import os
import psutil
import sys
import shutil

name = input("Ваше имя? ")
print("hello, ", name)

work = ''
while work != 'q':
    work = input("Давайте поработаем? (Y/N/q) ")
    if work == 'y':
        print("Let`s go! Я могу сделать: ")
        print("[1] Выведу список файлов ")
        print("[2] Выведу информацию о системе")
        print("[3] Выведу все процессы")
        print("[4] Бэкап данных директории")
        print("[5] Бэкап выбранного файла")
        print("[6] Удаление выбранного скопированного файла")
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
        elif do == 4:
            file_list = os.listdir()
            i = 0
            while i < len(file_list):
                newfile = file_list[i] + '.dupl'
                shutil.copy(file_list[i], newfile)
                i += 1
            print()
        elif do == 5:
            file = input('Укажите имя файла')
            if os.path.isfile(file):
                newfile = file + '.dupl'
                shutil.copy(file, newfile)
        elif do == 6:
            dirname = input('Укажите имя директории')
            file_list = os.listdir(dirname)
            i = 0
            while i < len(file_list):
                fullname = os.path.join(dirname, file_list[i])
                if fullname.endswith('.dupl'):
                    os.remove(fullname)
                i += 1
        else:
            print('exiting')
    elif work == 'n':
        print("Жаль!")
    else:
        print("dont right")