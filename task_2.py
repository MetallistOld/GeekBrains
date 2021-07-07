import shutil
import os

# Папки из которой и в которую будет происходить копирование
copyFrom = "my_project"
copyTo = "my_project/templates"


def copy_tree():
    try:
        shutil.copytree(copyFrom, copyTo, copy_function=shutil.copy2)
        print('Структура папок скопирована в templates')
    except FileExistsError:
        print('Папка уже существует')


if __name__ == "__main__":
    copy_tree()
