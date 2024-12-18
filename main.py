f = open("receipes.txt")
print(type(f))
data = f.read()
print(data, type(data))
f.close()

def create_dict_from_file(file_name):
    # """"""Функция чтения файла + создание словаря нужного формата""""""
    cook_dict = {}
    with open(file_name, encoding='utf8') as file_work:
        for line in file_work:
            dish_name = ''
            print(line.lower().strip())
            counter = int(file_work.readline())
            list_of_ingridient = []
            for i in range(counter):
                temp_dict = {}
                print(file_work.readline().lower())
                list_of_ingridient.append(temp_dict)
            cook_dict[dish_name] = list_of_ingridient
            file_work.readline()
    return cook_dict

#Задача 2
def get_shop_list_by_dishes(dishes, person_count):
    cook_book = {}
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingridient, info in cook_book[dish].items():
                total_quantity = info["quantity"] * person_count
                if ingridient in shop_list:
                    shop_list[ingridient]["quantity"] += total_quantity
                else:
                    shop_list[ingredient] = {
                        'measure': info['measure'],
                        'quantity': total_quantity
                    }
    
    return shop_list
result = get_shop_list_by_dishes
print(result)

#Задача 3
import os

def combine_files(file_list, output_file):
    file_info = []
    for file in file_list:
        with open(file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            line_count = len(lines)
            file_info.append((file, line_count, lines))
            file_info.sort(key=lambda x: x[1])

with open('output.txt', 'w', encoding='utf-8') as outfile:
    for f in ['file_1.txt', 'file_2.txt','file_3.txt']:
        with open(f, 'r') as infile:
            for line in infile:
                outfile.write(line)