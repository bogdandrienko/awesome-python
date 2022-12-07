import threading
import time

import requests
from threading import Thread


# url = "https://www.gismeteo.kz/weather-pavlodar-5174/"
# headers = {
#     "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
#                   'AppleWebKit/537.36 (KHTML, like Gecko) '
#                   'Chrome/102.0.0.0 Safari/537.36'
# }
# response = requests.get(
#     url=url,
#     headers=headers
# )
#
# data = response.content.decode()
# data1 = data.split('''"day">Сегодня''')[1]
# # data2 = data1.split('''Фактические данные''')[0]
# data2 = data1.split('''class="tab-image"''')[0]
#
# day_with_night = data2.split('''<span class="unit unit_temperature_c">''')
# # [1].split('''</span>''')[0]
# day_with_night = day_with_night[1::]  # c первого элемента(не с нулевого) : до конца : с шагом 1
#
# # print(day_with_night)
# # print(type(day_with_night))
# # print(len(day_with_night))
# #
# # for i in day_with_night:
# #     print(i, '\n')
#
# if len(day_with_night[0]) < len(day_with_night[1]):
#     day = day_with_night[1].split('''</span>''')[0]
#     night = day_with_night[0].split('''</span>''')[0]
# else:
#     day = day_with_night[0].split('''</span>''')[0]
#     night = day_with_night[1].split('''</span>''')[0]
#
# print(f'Днём температура: {day}, а ночью: {night}')
#
citys = [
    'https://www.gismeteo.kz/weather-shymkent-5324/',
    'https://www.gismeteo.kz/weather-pavlodar-5174/',
    'https://www.gismeteo.kz/weather-aktobe-5165/',
]


def decorator_vrema(func):
    def obertka(*args, **kwargs):
        time_func_start = time.perf_counter_ns()
        res = func(*args, **kwargs)
        print((time.perf_counter_ns() - time_func_start) // 1000000, 'ms')  # 1 000 000 000 ns 1 000 000 mk 1 000 ms 1 s
        return res

    return obertka


def request(url):
    headers = {
        "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/102.0.0.0 Safari/537.36'
    }
    response = requests.get(
        url=url,
        headers=headers
    )
    data = response.content.decode()
    data1 = data.split('''"day">Сегодня''')[1]
    data2 = data1.split('''class="tab-image"''')[0]
    day_with_night = data2.split('''<span class="unit unit_temperature_c">''')
    day_with_night = day_with_night[1::]
    if len(day_with_night[0]) < len(day_with_night[1]):
        day = day_with_night[1].split('''</span>''')[0]
        night = day_with_night[0].split('''</span>''')[0]
    else:
        day = day_with_night[0].split('''</span>''')[0]
        night = day_with_night[1].split('''</span>''')[0]
    print(f'{url}: Днём температура: {day}, а ночью: {night}')


@decorator_vrema
def sync_request():
    request(url=citys[0])
    request(url=citys[1])
    request(url=citys[2])


@decorator_vrema
def thread_request():
    thread_1 = Thread(target=request, args=(citys[0],))
    thread_2 = Thread(target=request, args=(citys[1],))
    thread_3 = Thread(target=request, args=(citys[2],))

    thread_1.start()
    thread_2.start()
    thread_3.start()

    thread_1.join()
    thread_2.join()
    thread_3.join()


if __name__ == "__main__":
    # sync_request()  # 751 -> три по очереди
    thread_request()  # 264 -> три одновременно 250 * 3 = 750

import requests


def get():
    url = 'https://www.google.com/search?q=%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0&rlz=1C1IXYC_ruKZ978KZ978&oq=gjujlf&aqs=chrome.1.69i57j0i10i131i433l9.1695j1j7&sourceid=chrome&ie=UTF-8'
    response = requests.get(url)
    return response.content.decode()

# print(get())


########################################################################################################################

from random import random

import requests
import json
import time

# params = {
#     'text': 'NAME:Аналитик',  # Текст фильтра. В имени должно быть слово "Аналитик"
#     'area': 1,  # Поиск ощуществляется по вакансиям города Москва
#     'page': 1,  # Индекс страницы поиска на HH
#     'per_page': 100  # Кол-во вакансий на 1 странице
# }

# req = requests.get('https://api.hh.ru/vacancies', params)  # Посылаем запрос к API

vacancy_id = 55508596
url = f'https://api.hh.ru/vacancies/{vacancy_id}'
response = requests.get(url=url)

if response.status_code != 200 and False:
    print("Ошибка: " + str(response.status_code))
else:
    print(response.content)
    data = response.content.decode()

    with open("vacancy.json", "w", encoding='utf8') as file:
        file.write(json.dumps(data, ensure_ascii=False))

    # data
    json_data = json.loads(response.content)
    print(json_data)
    print(type(json_data))
    description = json_data["description"]
    print(description)
    arr = description.split('<strong>')
    arr = arr[-1]
    arr = arr.split('</strong></p>')[0]
    print(arr)

    # ['1', '2', '3']
    # string_find = arr[-1] # [старт:стоп:шаг]
    # print(string_find)
    #
    # description = 'description'
    # print(description[::2])

vacancies = []

for i in range(0, 1):
    time.sleep(0.0001)
    position = "Программист"
    params = {
        'text': f'NAME:{position}',  # Текст фильтра. В имени должно быть слово "Аналитик"
        'area': 40,  # Поиск ощуществляется по вакансиям города Москва
        'page': i,  # Индекс страницы поиска на HH
        'per_page': 100  # Кол-во вакансий на 1 странице
    }
    response = requests.get('https://api.hh.ru/vacancies', params)  # Посылаем запрос к API
    json_data1 = json.loads(response.content.decode())
    # print(json_data1)
    print("len items:", len(json_data1["items"]))
    for j in json_data1["items"]:
        vacancies.append(j)

print(vacancies)
print(len(vacancies))
for i in vacancies:
    # print(i)
    try:
        description = i["name"]
        print()
        arr = description.split('<strong>')[-1].split('</strong></p>')[0]
        print("published_at: ", i["published_at"].split('T')[0], "id: " + i["id"], "name: ", arr)
    except Exception as error:
        print(error)

    print(i["published_at"].split('T'))

# 1 поток выполнения
# синхронные операции - response = requests.get(url=url) # 2.5 * 10 + логика + 0.5 = 30
# aсинхронные операции - response = await requests.get(url=url) # 2.5 * 1.1 + логика + 0.5 = 3

from threading import Thread
from multiprocessing import Process


def increase(thread_name="Thread"):
    index = 1
    while True:
        time.sleep(0.1)
        index += 1
        print(f"{thread_name} :{index}")


for i in range(0, 100):
    Thread(target=increase, args=(f"Thread {i}",)).start()

print("123")

# N поток выполнения
# мультипоточная операции - response = await requests.get(url=url) GIL
# мульпроцессор операции - response = await requests.get(url=url)


########################################################################################################################

import requests
from bs4 import BeautifulSoup

url = f'https://myfin.by/converter.html'
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
response = requests.get(url=url, headers=headers)  # http запрос

soup = BeautifulSoup(response.content, 'html.parser')
data1 = soup.find_all('span', itemprop="text")


print()




# локальное сохранение HTML
with open(file='new.html', mode='w', encoding="utf-8") as file:
    file.write(response.content.decode())
print('1 \n\n\n\n\n')

html_data = response.content.decode()
print(html_data)
print(type(html_data))

print('2 \n\n\n\n\n')

#  0  1
# [A, B]

str1 = 'converter-container converter-container-in-grid'
small_html1 = html_data.split(str1)[-1]  # обрезаем верх ненужных данных и берём последнюю таблицу

str2 = '<a href="'
small_html1 = small_html1.split(str2)[0]  # обрезаем низ ненужных данных

print(small_html1)
print(len(small_html1))

print('3 \n\n\n\n\n')

str3 = 'class="converter-container__item-input-wrapper"'
str4 = 'type="tel"'

# small_html2 = small_html1.split(str3)[-1].split('value="')[-1].split('"')[0]
small_html2 = small_html1.split(sep=str3)  # возвращает массив разделенных объектов по сепаратору

# print(small_html2)

all_list = []
for value in small_html2[1::1]:
    print(value + '\n\n')

    separator1 = 'class="converter-container__item-currency-name">'
    name1 = value.split(separator1)  # разделили предыдущую строку по сепаратору на 2 части
    print(name1)
    name2 = name1[1]  # взяли только вторую часть (нижнюю)
    print(name2)
    separator2 = '</div>'
    name3 = name2.split(separator2)  # разделили предыдущую строку по сепаратору на 2 части
    print(name2)
    name4 = name3[0]  # взяли только первую часть (верхнюю)
    print(name4)
    name5 = name4.strip()  # очистили пробелы и отступы по краям
    print(name5)

    value1 = value.split('value="')[1].split('"/>')[0]

    abbr1 = value.split('<span class="converter-container__item-currency-abbr">')[1].split('<')[0]

    print(f'валюта: {name5}, значение: {value1}, аббреиватура: {abbr1}')
    # all_list.append((value1, name5, abbr1))
    # all_list.append([value1, name5, abbr1])
    all_list.append({"значение": value1, "валюта": name5, "аббреиватура": abbr1})
    # all_list.append(i.split('"')[0])

    # print(value.split('</div>')[0].strip())

print(all_list)
for i in all_list:
    print(type(i))
    print(f'валюта: {i["валюта"]}, значение: {i["значение"]}')

print('3 \n\n\n\n\n')
print('3 \n\n\n\n\n')
print('3 \n\n\n\n\n')
print('3 \n\n\n\n\n')
print('3 \n\n\n\n\n')
print('3 \n\n\n\n\n')
print('3 \n\n\n\n\n')
print('3 \n\n\n\n\n')
print('3 \n\n\n\n\n')
print('3 \n\n\n\n\n')

print(all_list)

print('4 \n\n\n\n\n')

# soup = BeautifulSoup(response.content, 'html.parser')
# print(soup)


word = 'Banana, Apple, Kiwi'
print(word)
print(word.split(', '))
print(type(word.split(', ')))

str1 = """
<div class="converter-container__item-input-wrapper">
    <span class="converter-container__item-currency-abbr">
        uah
    </span>
    <input type="tel" inputmode="decimal" id="bestb_uah" class="input_calc form-control form-input-sum bestb" value="84.9026">
    <span class="converter-container__item-delete" data-js="hide-item" data-del="bestbuah" style="display: none"></span>
</div>
"""

print('5 \n\n\n\n\n')

str6 = str1.split('<span class="converter-container__item-currency-abbr">')[1]
#
print(str6)
print(type(str6))

print('6 \n\n\n\n\n')

str7 = str6.split('</span>')[0].strip()
print(str7)
print(type(str7))



# url = f'https://www.google.com/search?q=google+%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0&rlz=1C1IXYC_ruKZ978KZ978&oq=google+%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0&aqs=chrome..69i57j0i457i512j0i512l8.7400j1j7&sourceid=chrome&ie=UTF-8'
# headers = {
#     'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
# response = requests.get(url=url, headers=headers)  # http запрос
#
# soup = BeautifulSoup(response.content, 'html.parser')
#
# weather = soup.findAll("span")
# print(f"weather: {weather}")

########################################################################################################################

import requests
import json

url = 'http://127.0.0.1:8000/teacher/user_count/'
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
response = requests.get(url=url, headers=headers)  # http запрос
html_data = json.loads(response.content)  # превращает байты в словарь (JSON)
print(html_data)
print(type(html_data))

########################################################################################################################

import requests
from bs4 import BeautifulSoup


url = "https://www.google.com/search?q=%D1%82%D0%B5%D0%BD%D0%B3%D0%B5+%D0%BA+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D1%83&rlz=1C1IXYC_ruKZ978KZ978&oq=%D1%82%D0%B5%D0%BD%D0%B3%D0%B5+%D0%BA+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D1%83&aqs=chrome.0.0i433i512j0i512l9.4659j1j7&sourceid=chrome&ie=UTF-8"
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"
}
response = requests.get(url=url, headers=headers)

print(response.content.decode())
print(type(response.content.decode()))

soup = BeautifulSoup(response.content, 'html.parser')
valute = soup.findAll("span", {"class": "UMOHqf EDgFbc"})[0]

print(f"valute: {valute.get_text()}")
print(f"valute type: {type(valute.get_text())}")

kurs = float(str(valute.get_text()).split('отметки')[1].split('тенге')[0].strip())
print(f"kurs: {kurs}")
print(f"kurs type: {type(kurs)}")

tenge = float(input("Введите сколько у Вас есть денег в тенге?"))

dollar = round(tenge / kurs, 2)

print(f'Ваши деньги в долларах: {dollar}')


########################################################################################################################

import bs4
import requests
from bs4 import BeautifulSoup

url = 'https://eda.ru/recepty/supy/borsch-mjasnoj-14622'
headers = {'User-agent': 'Mozilla/5.0'}
response = requests.get(url=url, headers=headers)
print(response.status_code)
# print(response.content.decode())
soup = BeautifulSoup(response.content, 'html.parser')
# print(soup.prettify())
print(type(soup))

data1 = soup.find_all('span', itemprop="text")
# data1 = soup.find_all('span', class_="text")
instructions = []
for i in data1:
    instructions.append(i.text)
    # print(i.text)
    # print(type(i.text))
# print(data1)
# print(type(data1))
print(instructions)

# print("\n \t \\ \"Рита\"")


########################################################################################################################

# Библиотека для работы с HTTP-запросами. Будем использовать ее для обращения к API HH
import requests

# Пакет для удобной работы с данными в формате json
import json

# Модуль для работы со значением времени
import time

# Модуль для работы с операционной системой. Будем использовать для работы с файлами
import os


def getPage(page=0):
    params = {
        'text': 'django',  # Текст фильтра. В имени должно быть слово "Аналитик"
        'area': 40,  # Поиск ощуществляется по вакансиям города Москва
        'page': page,  # Индекс страницы поиска на HH
        'per_page': 100
    }
    req = requests.get('https://api.hh.ru/vacancies', params)  # Посылаем запрос к API
    data = req.content.decode()  # Декодируем его ответ, чтобы Кириллица отображалась корректно
    req.close()
    return data


# Считываем первые 2000 вакансий
for page in range(0, 100):

    # Преобразуем текст ответа запроса в справочник Python
    jsObj = json.loads(getPage(page))

    # Сохраняем файлы в папку {путь до текущего документа со скриптом}\docs\pagination
    # Определяем количество файлов в папке для сохранения документа с ответом запроса
    # Полученное значение используем для формирования имени документа
    nextFileName = './docs/pagination/{}.json'.format(len(os.listdir('./docs/pagination')))

    # Создаем новый документ, записываем в него ответ запроса, после закрываем
    f = open(nextFileName, mode='w', encoding='utf8')
    f.write(json.dumps(jsObj, ensure_ascii=True))
    f.close()

    # Проверка на последнюю страницу, если вакансий меньше 2000
    if (jsObj['pages'] - page) <= 1:
        break

    # Необязательная задержка, но чтобы не нагружать сервисы hh, оставим. 5 сек мы может подождать
    time.sleep(0.5)

print('Страницы поиска собраны')

########################################################################################################################

import json
import time
import requests

details = []
with open("docs/pagination/6.json", "r") as file_r:
    json_data = json.loads(file_r.read())
    for vacancy in json_data["items"]:
        try:
            req = requests.get(f'https://api.hh.ru/vacancies/{vacancy["id"]}')  # Посылаем запрос к API
            data = req.content.decode()  # Декодируем его ответ, чтобы Кириллица отображалась корректно
            req.close()
            details.append(data)
            time.sleep(0.01)
        except Exception as error:
            pass

items = {"items": details}
with open("docs/pagination/6_1.json", "w+") as file_w:
    file_w.write(json.dumps(items, ensure_ascii=True))

with open("docs/pagination/6_1.json", "r") as file_r:
    json_data = json.loads(file_r.read())
    for item in json_data["items"]:
        print(item)
        # print(item["description"])

########################################################################################################################

import json
import requests

url = "https://api.instantwebtools.net/v1/airlines/10"
response = requests.get(url)
# Http - ответ. content - данные, статус код - статус запроса
print(response.status_code)
json_data = response.content.decode()
print(json_data)

url = "https://jsonplaceholder.typicode.com/posts"
# url = "https://api.instantwebtools.net/v1/airlines"
response = requests.get(url)
content = response.content
print(type(content))
json_data = content.decode()
print(type(json_data))
# print(json_data)

# чтобы превратить строку в JSON -объект - сериализация/десериализация
airlines = json.loads(json_data)  # [{}, {}, {}] {}
print(type(airlines))
# print(airlines[1:1:2])
# print(type(json.load(json_data)))

for airline in airlines[1:1:2]:
    # filename = f'temp/data_{airline["id"]}.json'
    # print(airline)
    # менеджер контекста - он открывает файл на чтение и закрывает автоматические после завершения операции
    # with open(f'temp/data_{airline["id"]}.json', 'w') as file:
    #     json.dump(airline, file)
    with open('temp/data_%s.json' % airline["id"], 'w') as file:  # alias - псевдоним
        # записывает объект в файл
        json.dump(obj=airline, fp=file)
        # json.dumps(airline)
    #



# with open('data.json', 'w') as file:
#     json.dump(json_data, file)
# json.dumps()

file_name = 'temp/data_4.json'
with open(file_name, 'r') as file:
    # читает объект с файла
    json_new_data = json.load(file)

    print(json_new_data)
    print(type(json_new_data))
    # json_data1 = json.loads(file.read())
    # print(json_data1)
    # json.load()
#     json.loads()

########################################################################################################################

import time

import requests
from bs4 import BeautifulSoup

url = "https://myfin.by/converter.html"

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/102.0.0.0 Safari/537.36'}
response = requests.get(url=url, headers=headers)
status = response.status_code
if status == 200:
    content = response.content  # позволяет прочитать html фаил
    with open("temp/hw.html", "wb") as file:  # создаем фаил куда запишем html код
        file.write(content)  # записывае фаил
    soup = BeautifulSoup(response.text, "lxml")  # парсим саит через BeautifulSoup
    # print(type(soup))
    data = soup.findAll("input", class_="input_calc form-control form-input-sum bestmb")  # Ищем по html
    new_data = str(data).split(sep='inputmode="decimal" type="tel" value="')
    new_data = str(new_data).split(sep='<input class="input_calc form-control form-input-sum bestmb" id="bestmb_')
    # print(new_data[6])
    dollar1 = new_data[1].split("""', '""")[0].split('"')[0]
    dollar2 = new_data[1].split("""usd" ', '""")[1].split('"/>')[0]
    dollar = tuple([dollar2, dollar1])
    # print(type(dollar))
    euro1 = new_data[2].split("""', '""")[0].split('"')[0]
    euro2 = new_data[2].split("""eur" ', '""")[1].split('"/>')[0]
    euro = tuple([euro2, euro1])
    # print(euro)
    sterling1 = new_data[3].split("""', '""")[0].split('"')[0]
    sterling2 = new_data[3].split("""gbp" ', '""")[1].split("/>,")[0].split('"')[0]
    sterling = tuple([sterling2, sterling1])
    # print(sterling2)
    uany1 = new_data[4].split("""', '""")[0].split('"')[0]
    uany2 = new_data[4].split("""cny" ', '""")[1].split('"/>')[0]
    uany = tuple([uany2, uany1])
    # print(uany)
    zloty1 = new_data[5].split("""', '""")[0].split('"')[0]
    zloty2 = new_data[5].split("""pln" ', '""")[1].split('"/>')[0]
    zloty = tuple([zloty2, zloty1])
    # print(zloty)
    rub1 = new_data[6].split("""', '""")[0].split('"')[0]
    rub2 = new_data[6].split("""rub" ', '""")[1].split('"/>')[0]
    rub = tuple([rub2, rub1])
    # print(rub)
    cours = [dollar, euro, sterling, uany, zloty, rub]
    # print(cours)
    value = 450000

    for valute in cours:
        # print(valute)
        if valute[-1] == "eur":
            result = value * float(valute[0])
            print(valute[0])
            print(result)

    # data = "23"
    # if (data // 10) % 2 == 1:
    #     time.sleep(1)
    #     update()

        # for i in new_data:
        #     print(i)
        #     print(len(i))
        #     # print('\n')
        # print('\n')
else:
    print("Oshibka dannyh")

########################################################################################################################


import time
from threading import Thread

import sys

from PySide6.QtCore import *
from PySide6.QtGui import *
import requests
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QLabel
from bs4 import BeautifulSoup

value = 420000.6

course_dollar = 0.0
url = 'https://finance.rambler.ru/calculators/converter/1-KZT-USD/'
# url = 'https://www.instagram.com/gazetakm/?hl=ru'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
response = requests.get(url=url, headers=headers)
print(response)
print(response.status_code)


def get_course():
    global course_dollar
    while True:
        if response.status_code == 200:  # 200 - удачный ответ
            soup = BeautifulSoup(response.text, 'lxml')
            # print(soup)
            print(type(soup))

            data = soup.find_all('div', class_='converter-display__cross-block')[0]
            new_data = str(data).split(sep='__value">')[1:]

            # [(1, 'KZT'), (0.0023, 'USD')]
            tenge = tuple(
                [
                    new_data[0].split('</div>\n<div class="converter-display__currency">')[0],
                    new_data[0].split('</div>\n<div class="converter-display__currency">')[1].split('</div>')[0]
                ]
            )
            print(tenge)
            print(type(tenge))

            dollar = tuple(
                [
                    new_data[1].split('</div>')[0],
                    new_data[1].split('</div>')[-3].split('>')[-1]
                ]
            )
            print(dollar)
            print(type(dollar))

            course = [tenge, dollar]
            print(course)
            print(type(course))

            # value
            index = 0

            for valute in course:
                index += 1
                print(f'Объект №{index}: {valute}')
                if valute[-1] == 'USD':
                    course_dollar = float(valute[0])
                    result = round(value * float(valute[0]), 3)
                    print(str(result) + " $")

            # print(new_data)
            # print(len(new_data))

            # content = response.content
            # with open(file='temp/new2.html', mode='wb') as file:
            #     file.write(content)

            # data = content.decode(encoding='ISO-8859-1')
            # print(type(data))
            # print(data)

            # new_data = data.split('value="')
            # print(len(new_data))
            # for i in new_data:
            #     print(i + '\n')
            # print(new_data)
        else:
            print("ошибка получения данных!")
        time.sleep(5.0)
        print('Курс обновлён')


Thread(target=get_course).start()


# import sys
# import random
# from PySide6 import QtCore, QtWidgets, QtGui
#
#
# class MyWidget(QtWidgets.QWidget):
#     def __init__(self):
#         super().__init__()
#         self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]
#         self.button = QtWidgets.QPushButton("File")
#         self.text = QtWidgets.QLabel("Hello World")
#         self.layout = QtWidgets.QVBoxLayout(self)
#         self.layout.addWidget(self.text)
#         self.layout.addWidget(self.button)
#
#         self.button.clicked.connect(self.magic)
#
#     @QtCore.Slot()
#     def magic(self):
#         self.text.setText(random.choice(self.hello))
#
# if __name__ == "__main__":
#     app = QtWidgets.QApplication([])
#
#     widget = MyWidget()
#     widget.resize(800, 600)
#     widget.show()
#
#     sys.exit(app.exec())


class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.line_edit = QLineEdit()
        layout.addWidget(self.line_edit)

        self.label = QLabel()
        layout.addWidget(self.label)

        self.line_edit.textChanged.connect(self.line_edit_text_changed)

        self.show()

    def line_edit_text_changed(self, text):
        try:
            text = round(course_dollar * float(text), 3)
            self.label.setText("Ваша сумма: " + str(text) + " $")
        except Exception as error:
            self.label.setText('ошибка ввода данных')


app = QApplication(sys.argv)
mw = MainWindow()
app.exec()


########################################################################################################################

import requests
from bs4 import BeautifulSoup

url = 'https://www.instagram.com/gazetakm/?hl=ru'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
response = requests.get(url=url, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')
print(soup)
data = soup.find_all('article')
print(data)
print(len(data))

########################################################################################################################

import requests
from bs4 import BeautifulSoup

url = f'https://myfin.by/converter.html'
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
response = requests.get(url=url, headers=headers)  # http запрос

soup = BeautifulSoup(response.content, 'html.parser')
data1 = soup.find_all('div', class_='converter-containers converter-containers--tablet-col-2')
print(data1)
print(len(data1))

print('\n\n\n\n********\n\n\n\n')

data2 = data1[0].text.split('converter-container__inputs')
print(data2)
print(len(data2))

# data2 = data1[0].find_all('div', class_='converter-container__item')
# print(data2)
# print(len(data2))
# for i in data2:
#     print(i.text)

########################################################################################################################

import datetime
import sys
import time

import requests
from bs4 import BeautifulSoup
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QLabel, QComboBox
import threading

values = [{"name": "", "value": 0}]


def get_fresh_values():
    while True:

        current_time = datetime.datetime.now().strftime("%S")

        if int(current_time) // 10 % 2:
            print('задержка')
            time.sleep(10)

        print(f"Seconds: {current_time}")

        # time.sleep(1)

        url = 'https://myfin.by/converter.html'
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/102.0.0.0 Safari/537.36'
        }
        response = requests.get(url=url, headers=headers)

        with open('new_html.html', 'wb') as file:
            file.write(response.content)

        soup = BeautifulSoup(response.text, 'lxml')

        print(soup)
        # print(soup.text)

        # data = soup.find_all('div', class_="converter-container__item")

        data = soup.findAll("input", class_="input_calc form-control form-input-sum bestmb")

        print(data)

        values = []
        for i in data:
            print(i, '\n')

            sep_name_left = 'id="bestmb_'
            sep_name_right = '" inputmode'

            val_name_1 = str(i).split(sep=sep_name_left)[1]
            val_name_2 = val_name_1.split(sep=sep_name_right)[0]

            print(val_name_2, '\n')

            sep_value_left = 'value="'
            sep_value_right = '"/>'

            val_value_1 = str(i).split(sep=sep_value_left)[1]
            val_value_2 = val_value_1.split(sep=sep_value_right)[0]

            print(val_value_2, '\n')

            dict_value = {
                "name": val_name_2,
                "value": val_value_2,
            }
            values.append(dict_value)

        print(values)


class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.line_edit = QLineEdit()
        layout.addWidget(self.line_edit)

        self.label = QLabel()
        layout.addWidget(self.label)

        self.line_edit.textChanged.connect(self.line_edit_text_changed)

        self.combo_box_filter = QComboBox()
        self.combo_box_filter.addItem("usd")
        self.combo_box_filter.addItem("eur")
        self.combo_box_filter.addItems(["gbp", "cny", "pln", "rub"])

        layout.addWidget(self.combo_box_filter)  # вкладываем QComboBox -> QGridLayout

        self.show()

    def line_edit_text_changed(self, text):
        try:
            combo = self.combo_box_filter.currentText()
            print(combo)

            for dictionary in values:  # массив со словарями
                keys1 = dictionary.keys()

                print(keys1)

                values1 = dictionary.values()

                print(values1)

                item1 = dictionary.items()

                print(item1)

                # if combo in values1:
                #     print('валюта есть')
                #     text = round(float(dictionary["value"]) * float(text), 3)
                #     self.label.setText("Ваша сумма: " + str(text) + " единиц")
                # else:
                #     print('валюты нет')

                if dictionary["name"] == combo:
                    print('валюта есть')
                    text = round(float(dictionary["value"]) * float(text), 3)
                    self.label.setText("Ваша сумма: " + str(text) + " единиц")

        except Exception as error:
            self.label.setText('ошибка ввода данных')


threading.Thread(target=get_fresh_values).start()

app = QApplication(sys.argv)
mw = MainWindow()
app.exec()

########################################################################################################################

import asyncio
import concurrent.futures
import multiprocessing
import threading
import time

import requests
import aiohttp
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/102.0.0.0 Safari/537.36'
}


def get_temp_string(url: str, city_name: str):
    time.sleep(20)

    response1 = requests.get(url=url, headers=headers)
    soup2 = BeautifulSoup(response1.text, 'html.parser')
    objs3 = soup2.find_all('span', {'class': 'unit unit_temperature_c'})
    objs4 = [x.text.strip() for x in objs3]
    print(f"{city_name}: day: {objs4[3]} | night: {objs4[2]}\n")
    return f"{city_name}: day: {objs4[3]} | night: {objs4[2]}"


def write_image_from_url(image_name: str) -> None:
    with open(f'images/{image_name}.jpg', mode='wb') as file:
        file.write(requests.get(url='https://picsum.photos/600/600/', headers=headers).content)


def sync_download_image():
    for i in range(1, 10 + 1):
        write_image_from_url(image_name=f'img{i}')


def multithread_download_image():
    # tasks = []
    # for x in range(1, 10+1):
    #     tasks.append(threading.Thread(target=write_image_from_url, kwargs={"image_name": f'img{x}'}))
    # for task in tasks:
    #     task.start()
    # for task in tasks:
    #     task.join()

    current_thread = 16
    with concurrent.futures.ThreadPoolExecutor(max_workers=current_thread * 2 + 1) as executor:
        for x in range(1, 10 + 1):
            executor.submit(write_image_from_url, f'img{x}')


def multiprocess_download_image():
    # tasks = []
    # for x in range(1, 10 + 1):
    #     tasks.append(multiprocessing.Process(target=write_image_from_url, kwargs={"image_name": f'img{x}'}))
    # for task in tasks:
    #     task.start()
    # for task in tasks:
    #     task.join()

    current_thread = 16
    with concurrent.futures.ProcessPoolExecutor(max_workers=current_thread * 2 + 1) as executor:
        for x in range(1, 10 + 1):
            executor.submit(write_image_from_url, f'img{x}')


async def as_write_image_from_url(image_name: str) -> None:
    async with aiohttp.ClientSession() as session:
        async with session.get('https://picsum.photos/600/600/') as clien_response:
            response = await clien_response.read()

    with open(f'images/{image_name}.jpg', mode='wb') as file:
        file.write(response)


async def async_download():
    await asyncio.gather(*[as_write_image_from_url(f'img{i}') for i in range(1, 10 + 1)])


def async_download_image():
    asyncio.run(async_download())


def threadings():
    citys = [
        {"url": 'https://www.gismeteo.kz/weather-shymkent-5324/', "city_name": "shymkent"},
        {"url": 'https://www.gismeteo.kz/weather-nur-sultan-5164/', "city_name": "nur-sultan"},
        {"url": 'https://www.gismeteo.kz/weather-almaty-5205/',
         "city_name": "almaty"},
        {"url": 'https://www.gismeteo.kz/weather-shymkent-5324/',
         "city_name": "shymkent"},
        {"url": 'https://www.gismeteo.kz/weather-shymkent-5324/',
         "city_name": "shymkent"},
        {"url": 'https://www.gismeteo.kz/weather-nur-sultan-5164/',
         "city_name": "nur-sultan"},
        {"url": 'https://www.gismeteo.kz/weather-almaty-5205/',
         "city_name": "almaty"},
        {"url": 'https://www.gismeteo.kz/weather-shymkent-5324/',
         "city_name": "shymkent"},
        {"url": 'https://www.gismeteo.kz/weather-shymkent-5324/',
         "city_name": "shymkent"},
        {"url": 'https://www.gismeteo.kz/weather-nur-sultan-5164/',
         "city_name": "nur-sultan"},
        {"url": 'https://www.gismeteo.kz/weather-almaty-5205/',
         "city_name": "almaty"},
        {"url": 'https://www.gismeteo.kz/weather-shymkent-5324/',
         "city_name": "shymkent"},
        {"url": 'https://www.gismeteo.kz/weather-shymkent-5324/',
         "city_name": "shymkent"},
        {"url": 'https://www.gismeteo.kz/weather-nur-sultan-5164/',
         "city_name": "nur-sultan"},
        {"url": 'https://www.gismeteo.kz/weather-almaty-5205/',
         "city_name": "almaty"},
        {"url": 'https://www.gismeteo.kz/weather-shymkent-5324/',
         "city_name": "shymkent"},
    ]

    # for city in citys:
    #     get_temp_string(url=city["url"], city_name=city.get("city_name"))

    # citys_tasks = []
    # for city in citys:
    #     new_thread = threading.Thread(
    #         target=get_temp_string, kwargs={
    #             "url": city.get("url"),
    #             "city_name": city.get("city_name")
    #         }
    #     )
    #     citys_tasks.append(new_thread)
    #
    # for task in citys_tasks:
    #     task.start()
    #
    # for task in citys_tasks:
    #     task.join()
    # current_thread = 8
    #
    # with concurrent.futures.ThreadPoolExecutor(max_workers=current_thread * 2 + 1) as executor:
    #     for city in citys:
    #         future = executor.submit(get_temp_string, city.get("url"), city.get("city_name"))
    #         # result = future.result()

    # with concurrent.futures.ProcessPoolExecutor(max_workers=10) as executor:
    #     for city in citys:
    #         future = executor.submit(get_temp_string, city.get("url"), city.get("city_name"))
    #         # result = future.result()


if __name__ == "__main__":
    time1 = time.perf_counter()

    # threadings()
    # sync_download_image()  # 7.3
    # multithread_download_image()  # 0.9 | 1.0
    # multiprocess_download_image()  # 1.5 | 1.7
    async_download_image()  # 1.3

    print(round(time.perf_counter() - time1, 1))

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
#                   'AppleWebKit/537.36 (KHTML, like Gecko) '
#                   'Chrome/102.0.0.0 Safari/537.36'
# }
# response = requests.get(url="", headers=headers)
# # print(response.text)
# soup = BeautifulSoup(response.text, 'html.parser')
# objs = soup.find_all('span', {'class': 'unit unit_temperature_c'})
# objs2 = [x.text.strip() for x in objs]
# print(f"Нур-Султан: day: {objs2[3]} | night: {objs2[2]}")
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
#                   'AppleWebKit/537.36 (KHTML, like Gecko) '
#                   'Chrome/102.0.0.0 Safari/537.36'
# }
# response = requests.get(url="", headers=headers)
# # print(response.text)
# soup = BeautifulSoup(response.text, 'html.parser')
# objs = soup.find_all('span', {'class': 'unit unit_temperature_c'})
# objs2 = [x.text.strip() for x in objs]
# print(f"Алматы: day: {objs2[3]} | night: {objs2[2]}")

########################################################################################################################
!