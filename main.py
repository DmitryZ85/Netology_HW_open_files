# ДЗ Чтение файлов
# Книга рецептов
# и добавил тут же слияние файлов в один

import os

def file_name():
    name = input('Введите имя файла с расширением: ')
    return name


def open_file():
    open_file_name = file_name()
    file_directory = os.path.join(os.getcwd(), open_file_name)
    cook_book = {}

    with open(file_directory, encoding='utf-8') as file_book:
        meal = file_book.readline().strip()
        for line in file_book:
            number = int(line.strip())
            ingredients = []
            for ingred in range(number):
                item = file_book.readline().strip().split(' | ')
                ingredients.append({'ingredient_name': item[0], 'quantity': item[1], 'measure': item[2]})
            cook_book[meal] = ingredients
            file_book.readline().strip()
            meal = file_book.readline().strip()
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = open_file()
    ingred_book = {}
    for dish in dishes:
        if dish in cook_book.keys():
            for ingred in cook_book[dish]:
                ingredient = ingred['ingredient_name']
                quantity = int(ingred['quantity']) * person_count
                measure = ingred['measure']
                if ingredient not in ingred_book.keys():
                   ingred_book[ingredient] = {'quantity': quantity, 'measure': measure}
                else:
                    ingred_book[ingredient]['quantity'] += quantity
        else:
            print(f'Такого блюда - {dish} - нет среди доступных')
    return ingred_book


def get_result_file():
    INIT_PATH = os.getcwd()
    FILES_DIR_NAME = 'files_for_3HW'
    file_directory = os.path.join(INIT_PATH, FILES_DIR_NAME)
    files_list = os.listdir(file_directory)
    file_len = {}

    for file in files_list:
        with open(os.path.join(file_directory, file), encoding='utf-8') as file_to_read:
            quantity = len(file_to_read.readlines())
            if quantity not in file_len.keys():
                file_len[quantity] = file
            else:
                file_len[quantity].append(file)
            sort_file_len = sorted(file_len.keys())
            sorted_file_dict = {i: file_len[i] for i in sort_file_len}

    with open(os.path.join(file_directory, 'result.txt'), 'w', encoding='utf-8') as result:
        for quantity_ln, file_nm in sorted_file_dict.items():
            result.write(str(file_nm) + '\n')
            result.write(str(quantity_ln) + '\n')
            with open(os.path.join(file_directory, file_nm), encoding='utf-8') as read_file:
                for i in range(quantity_ln):
                    result.write(read_file.readline())
            result.write('\n')


print(get_shop_list_by_dishes(["Омлет", 'Фахитос', 'Фахитос'], 2))
get_result_file()