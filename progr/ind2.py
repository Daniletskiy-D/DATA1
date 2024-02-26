#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def remove_comments(source_file, dest_file):
    """
    Функция для удаления комментариев
    """
    try:
        with open(source_file, 'r') as f_src, open(dest_file, 'w') as f_dest:
            for line in f_src:
                if '#' in line:
                    index = line.index('#')
                    f_dest.write(line[:index] + '\n')
                else:
                    f_dest.write(line)
        print("Комментарии успешно удалены!")
    except FileNotFoundError:
        print("Ошибка: Не удалось найти указанный файл.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == '__main__':
    source_file = input("Введите имя исходного файла: ")
    dest_file = input("Введите имя файла назначения: ")

    remove_comments(source_file, dest_file)