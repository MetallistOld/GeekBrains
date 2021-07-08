import shutil
import os

root_dir = 'my_project'  # Папка в которой ведем поиск шаблона
copyTo = 'my_project/templates'  # Папка в которую будет происходить копирование

if not os.path.isdir(copyTo):
    os.mkdir(copyTo)


def copy_tree(copy_from):
    shutil.copytree(copy_from, copyTo, copy_function=shutil.copy2, dirs_exist_ok=True)
    print(f'Шаблоны из {copy_from} скопированы в my_project\\templates')


for root, dirs, files in os.walk(root_dir):
    for dir in dirs:
        if dir == 'templates':
            rel_path = os.path.join(root, dir)
            if rel_path != 'my_project\\templates':  # Что бы не копировать папку templates в нее же
                copy_tree(rel_path)
