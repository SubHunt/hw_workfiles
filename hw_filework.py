import copy
import os

import pprint
from collections import OrderedDict
#
# ''' cook_book =
#     {blish_name: [{ingredient_name:'', quantity:'', measure:''}
#                   {ingredient_name:'', quantity:'', measure:''}
#                   {ingredient_name:'', quantity:'', measure:''}]
#     }
#     '''
# # task_1
cur_path = os.getcwd()
dir_name = 'files'
file_name = 'recipes.txt'
full_path = os.path.join(cur_path, dir_name, file_name)
cook_book = {}

with open(full_path, 'rt', encoding='utf8') as file:
    for line in file:
        ingredients = []
        blish_name = line.strip()  # Берем первую строку - название блюда
        cook_book[blish_name] = ingredients  # Создаем словарь с ключом название блюда и списком со словарем
        ingredients_count = file.readline()  # Считываем кол-во ингридиентов в каждом блюде
        for qty_ingr in range(int(ingredients_count)):  # кол-во итераций равно кол-ву ингредиентов в каждом блюде
            ingr = file.readline()  # Считываем очередной ингредиент
            # распаковали строку в список на данные ингредиента
            ingredient_name, quantity, measure = ingr.strip().split(' | ')
            ingredients.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
        blank_line = file.readline()
pprint.pprint(cook_book, width=100, sort_dicts=True)

# task_2


def get_shop_list_by_dishes(dishes, person_count):
    # Создаем копию словаря, чтобы не изменять данные в исходном
    cook_book2 = copy.deepcopy(cook_book)
    # Проходим по каждому блюду
    for dishe in dishes:
        print(f'Заказали "{dishe}", в количестве - {person_count} порций')
        # Перебираем каждый ингредиент блюда
        for ingredient in cook_book2[dishe]:
            # Умножаем вес ингредиента на кол-во порций
            ingredient['quantity'] = int(ingredient['quantity']) * person_count
            # Создаем итоговоый словарь с полученным кол-вом ингредиентов
            total_ingr = {'measure': measure, 'quantity': ingredient['quantity']}
            print(ingredient['ingredient_name'], total_ingr)


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
# Проверяем, что наш исходный словарь не изменился, прогоняем еще раз  такой же заказ
# get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

# task_3


def length_file(name_file):
    """Функция принимает путь к файлу, создаем словарь с ключом имя файла и его значение кол-во строк"""
    dict_files[os.path.basename(name_file)] = len(open(name_file, encoding='utf-8').readlines())


# Файлы для чтения/записи хранятся в подпапке files, поэтому создаем к ней относительный путь
full_path_1 = os.path.join(cur_path, dir_name, '1.txt')
full_path_2 = os.path.join(cur_path, dir_name, '2.txt')
full_path_3 = os.path.join(cur_path, dir_name, '3.txt')
full_path_out = os.path.join(cur_path, dir_name, 'out.txt')
dict_files = {}
a = []

'''По очереди прогоняем каждый файл в функции, для подсчета кол-во строк'''
length_file(full_path_1)
length_file(full_path_2)
length_file(full_path_3)
'''Сортируем словарь по значению по возрастанию'''
dict_sort_files = OrderedDict(sorted(dict_files.items(), key=lambda t: t[1]))
for some_file in dict_sort_files:  # Перебираем отсортированные ключи по кол-ву строк от меньшего к большему
    some_path = os.path.join(cur_path, dir_name, some_file)  # Получаем путь к нужному файлу
    with open(some_path, 'r', encoding='utf-8') as file:  # Открываем нужный файл для чтения
        a += file.readlines()  # Считываем с очередного файла разом все строки
        a.append('\n')  # Добавляем переход на новую строку между файлами
with open(full_path_out, 'w', encoding='utf-8') as file:  # Записываем общий результат в новый файл out.txt
    file.writelines(a)
