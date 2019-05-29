import os
import psutil
import sys
import shutil

def dupl(file):
    if os.path.isfile(file):
        newfile = file + '.dupl'
        shutil.copy(file, newfile)
        if os.path.exists(newfile):
            print("Файл ", newfile, " был успешно создан")
            return True
        else:
            print("Есть какие-то проблемы копирования")
            return False

def sysinfo():
    print('File system coding:', sys.getfilesystemencoding())
    print('Platform:', sys.platform)
    print('CPU number:', os.cpu_count())
    print('Login:', os.getlogin())
    print('Current directory:', os.getcwd())

def delete(file_list):
    success = 0
    for f in file_list:
            fullname = os.path.join(dirname, f)
            if fullname.endswith('.dupl'):
                os.remove(fullname)
                if not os.path.exists(fullname):
                    success += 1
                    print("Файл ", fullname, " был успешно удален")
    return success

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
            sysinfo()

        elif do == 3:
            print(psutil.pids())
        elif do == 4:
            file_list = os.listdir()
            i = 0
            while i < len(file_list):
                dupl(file_list[i])
                i += 1
            print()
        elif do == 5:
            file = input('Укажите имя файла')
            dupl(file)
        elif do == 6:
            dirname = input('Укажите имя директории')
            file_list = os.listdir(dirname)
            count = delete(file_list)
            print("Было удалено:", count)

        else:
            print('exiting')
    elif work == 'n':
        print("Жаль!")
    else:
        print("dont right")