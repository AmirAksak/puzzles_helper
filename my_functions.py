NAME = 'my_functions'

import os


def get_files_list(dir):
    """
    Функция get_files_list возвращает список
    всех файлов указанного каталога, включая
    дочерние подкаталоги, в формате
    [[path1, file1] ... [pathN, fileN]]
    """
    files_list = []
    rez = list(os.walk(dir))
    for i in rez:
        f_list = i[2]
        if f_list:
            for a in f_list:
                files_list.append([i[0], a])
    return files_list
