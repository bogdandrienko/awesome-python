########################################################################################################################
# TODO работа с текстовыми файлами

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

import json

# Serialize obj as a JSON formatted (де-факто стандарт для веба)
# сериализация obj (Python) => JSON
# десериализация JSON => obj (Python)

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

# JSON в виде строки (часто приходит из интернет запросов)
dict_str2 = """[
        {"IIN": '14124152452', "age": 24, "Name": "Bogdan1", "married": false},
        {"IIN": '14124152453', "age": 24, "Name": "Bogdan2", "married": false},
        {"IIN": '14124152454', "age": 24, "Name": "Bogdan3", "married": true},
        {"IIN": '14124152455', "age": 24, "Name": "Bogdan4", "married": false},
        {"IIN": '14124152456', "age": 24, "Name": "Bogdan5", "married": false},
    ]"""
dict2 = json.loads(dict_str2)

!
import requests
import json

var_dict1 = dict(Age=24, Name='Ally')  # создание словаря
print(var_dict1)

var_dict2 = {"Age": 24, "Name": 'Ally'}  # создание словаря
print(var_dict2)

var_dict3 = {}  # создание словаря
var_dict3["Age"] = 24
var_dict3["Name"] = 'Ally'
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


print("\n\n\n\n\n")

url = "https://jsonplaceholder.typicode.com/posts/"
response = requests.get(url)  # Объект библиотеки
json_data = response.content.decode()  # строка
print(json_data)

with open('data.json', 'w') as file:
    json.dump(json_data, file)
    # json.dumps()

# with open('src/dist/new_file.json', 'r') as file:
#     json_data1 = json.loads(file.read())
#     print(json_data1)
#     json.load()
#     json.loads()


url = "https://jsonplaceholder.typicode.com/posts/"
response = requests.get(url)  # Объект библиотеки
# response.status_code  # 200
# response.content  # [...]
print(response.content.decode())
print(type(response.content.decode()))
json_data1 = json.loads(response.content.decode())
print(json_data1[7])
print(type(json_data1[7]))

for i in json_data1:
    print(i["title"])
    with open(f'hello/data_{i["id"]}_new_new.json', 'w') as file:
        json.dump(json_data, file)

########################################################################################################################

########################################################################################################################
# TODO работа с папками

import os
import shutil

print(os.getcwd())

os.mkdir("data")

os.mkdir("data1")
os.rmdir("data1")


# os.rename()
# os.path.exists()

# shutil.copy()
# shutil.move()

def get_all_files_in_path(path=os.path.dirname(os.path.abspath('__file__'))):
    files_list = []
    for root, dirs, files in os.walk(path, topdown=True):
        for name in files:
            files_list.append(f"{os.path.join(root, name)}")
    return files_list


print(get_all_files_in_path())


def get_all_dirs_in_path(path=os.path.dirname(os.path.abspath('__file__'))):
    directories_list = []
    for root, dirs, files in os.walk(path, topdown=True):
        for name in dirs:
            directories_list.append(f"{os.path.join(root, name)}")
    return directories_list


print(get_all_dirs_in_path())


def create_folder_in_this_dir(folder_name='new_folder', current_path=os.path.dirname(os.path.abspath('__file__'))):
    full_path = current_path + f'/{folder_name}'
    try:
        os.makedirs(full_path)
    except Exception as error:
        print(f'directory already yet | {error}')
    finally:
        return full_path


create_folder_in_this_dir("temp2")

########################################################################################################################

!
import os
import shutil

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

!
import os

file_src = 'folder/file.txt'

with open(file_src, 'r') as file:
    text = file.readlines()
    print(text)
    clear_text = []
    for i in text:
        if len(i) > 1:
            clear_text.append(i)
    print(f"clear_text: {clear_text}")

    clear_text1 = [x for x in text if len(x) > 1]
    print(f"clear_text1: {clear_text1}")

current_path = 'folder/new_folder'
try:
    os.mkdir(current_path)
except:
    pass

for text in clear_text:
    file_name = f"file_{clear_text.index(text)+1}"
    with open(f"{current_path}/{file_name}", 'w') as file:
        text = file.write(text)

os.remove(file_src)

!
import openpyxl
print(openpyxl.__version__)

from docx import Document
from docx.shared import Inches

document = Document()

#  (чем запускаем)   флаг    каким модулем      имя папки
#     python         -m         venv              env  # создание виртуального окружения
# python -m venv env

# cd env       cd Scripts     call activate.bat
# call env/Scripts/activate.bat  # активация виртуального окружения

# pip install --upgrade pip  # обновление pip внутри виртуального окружения

# pip install openpyxl==3.0.9  # установка специфичной версии
# pip install openpyxl  # установка последней версии
# pip uninstall openpyxl -y  # удаление библиотеки

# pip freeze > requirement.txt  # заморозка(сохранение) библиотек и модулей в текстовый файл
# pip install -r requirement.txt  # установка построчно каждой библиотеки с версией из файла
