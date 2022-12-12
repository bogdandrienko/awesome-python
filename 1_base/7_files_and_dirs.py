########################################################################################################################
# TODO работа с текстовыми файлами

import json
import os
import shutil

# open('имя_и_расширение_файла', 'режим_открытия')
# режимы: w r a wb rb w+ r+

# ручное закрытие файла
file1 = open('z_new.txt', 'w')  # если файл в папке 'data' - open('data/z_new.txt', 'w')
file1.write("Python is awesome!123\n\thi")
file1.close()

# контекстный менеджер
with open('z_new.txt', 'r') as file2:
    line1 = file2.read()
    print(line1)

    lines1 = file2.readlines()
    print(lines1)
    # внутри контекстного менеджера

# снаружи контекстного менеджера


########################################################################################################################

########################################################################################################################
# TODO работа с JSON - файлами


# Serialize obj as a JSON formatted (де-факто стандарт для веба)
# сериализация obj (Python) => JSON
# де сериализация JSON => obj (Python)

dict1 = {"name": "Bogdan"}
# запись
with open('data/new.json', 'w') as file1:
    json.dump(dict1, file1)
dict_str1 = json.dumps(dict1)
print(dict_str1)

# чтение
with open('data/new.json', 'r') as file2:
    dict2 = json.load(file2)
    print(dict2)

# JSON в виде строки (часто приходит из "интернет" запросов)
dict_str2 = """[
        {"IIN": '14124152452', "age": 24, "Name": "Bogdan1", "married": false},
        {"IIN": '14124152453', "age": 24, "Name": "Bogdan2", "married": false},
        {"IIN": '14124152454', "age": 24, "Name": "Bogdan3", "married": true},
        {"IIN": '14124152455', "age": 24, "Name": "Bogdan4", "married": false},
        {"IIN": '14124152456', "age": 24, "Name": "Bogdan5", "married": false},
    ]"""
dict2 = json.loads(dict_str2)

var_dict1 = dict(Age=24, Name='Ally')  # создание словаря
print(var_dict1)

var_dict2 = {"Age": 24, "Name": 'Ally'}  # создание словаря
print(var_dict2)

var_dict3 = {"key": "value"}  # создание словаря
# var_dict3["Age"] = 24
# var_dict3["Name"] = 'Ally'
print(var_dict3)

var_dict4 = {
    "firstName": "Иван",
    "lastName": "Иванов",
    "address": {
        "streetAddress": "Московское ш., 101, кв.101",
        "city": "Ленинград",
        "postalCode": 101101
    },
    "phoneNumbers": [
        "812 123-1234",
        "916 123-4567"
    ]
}
print(type(var_dict4))

########################################################################################################################

########################################################################################################################
# TODO работа с папками


print(os.getcwd())

# first = os.path.abspath(os.path.dirname(__file__))  # содержит абсолютный путь к текущему скрипту
first = ''  # содержит относительный путь к текущему скрипту
second = "temp\\junk2.txt"  # \ - изоляция символа   \n - перенос строки, \t - табуляция...
path = os.path.join(first, second)
print(f"path: {path}")

try:
    os.remove(path)  # удаление файла
except Exception as error:
    print(error)
finally:
    try:
        os.rmdir('temp')  # удаление пустой папки
    except Exception as error:
        print(error)
        shutil.rmtree('temp')  # удаление не пустой папки

os.mkdir("data")

os.mkdir("data1")
os.rmdir("data1")

for filename in os.listdir(''):
    print(filename)

# os.rename()
# os.path.exists()

# shutil.copy()
# shutil.move()

def get_all_files_in_path(p=os.path.dirname(os.path.abspath('__file__'))):
    files_list = []
    for root, dirs, files in os.walk(p, topdown=True):
        for name in files:
            files_list.append(f"{os.path.join(root, name)}")
    return files_list


print(get_all_files_in_path())


def get_all_dirs_in_path(p=os.path.dirname(os.path.abspath('__file__'))):
    directories_list = []
    for root, dirs, files in os.walk(p, topdown=True):
        for name in dirs:
            directories_list.append(f"{os.path.join(root, name)}")
    return directories_list


print(get_all_dirs_in_path())


def create_folder_in_this_dir(folder_name='new_folder', current_path=os.path.dirname(os.path.abspath('__file__'))):
    full_path = current_path + f'/{folder_name}'
    try:
        os.makedirs(full_path)
    except Exception as err:
        print(f'directory already yet | {err}')
    finally:
        return full_path


create_folder_in_this_dir("temp2")

########################################################################################################################
