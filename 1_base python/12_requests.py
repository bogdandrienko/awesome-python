import requests

# url = "https://jsonplaceholder.typicode.com/posts/66"
# response = requests.get(url=url)  # HTTP (TCP/IP) - протоколы запросов
# print(response, type(response))  # 200 OK <Response [200]> <class 'requests.models.Response'>
# print('\n\n\n**********\n\n\n')
# status_code = response.status_code
# print(status_code, type(status_code))  # 200 <class 'int'>
# print('\n\n\n**********\n\n\n')
# r_json = response.json()
# print(r_json, type(r_json))  # {'userId': 7, 'id': 66, 'title': 'repudiandae ea animi iusto', 'body': 'officia veritatis tenetur vero qui itaque\nsint non ratione\nsed et ut asperiores iusto eos molestiae nostrum\nveritatis quibusdam et nemo iusto saepe'} <class 'dict'>
# print('\n\n\n**********\n\n\n')
# text = response.text
# print(text, type(text))  # {
# #   "userId": 7,
# #   "id": 66,
# #   "title": "repudiandae ea animi iusto",
# #   "body": "officia veritatis tenetur vero qui itaque\nsint non ratione\nsed et ut asperiores iusto eos molestiae nostrum\nveritatis quibusdam et nemo iusto saepe"
# # } <class 'str'>
# print('\n\n\n**********\n\n\n')
# content = response.content
# print(content, type(content))  # b'{\n  "userId": 7,\n  "id": 66,\n  "title": "repudiandae ea animi iusto",\n  "body": "officia veritatis tenetur vero qui itaque\\nsint non ratione\\nsed et ut asperiores iusto eos molestiae nostrum\\nveritatis quibusdam et nemo iusto saepe"\n}' <class 'bytes'>
# request - запрос / response - ответ

# get - read
# post - create
# put (patch) - update
# delete - delete

url = "https://ru.wikipedia.org/wiki/Python"
result = requests.get(url=url)
substring1 = "Дополнительные возможности,"
source_string = result.text
# print(source_string)
# print(len(source_string))  # 576 465

res1 = source_string.split(sep=substring1)  # сепаратор
# split - "распиливает" исходную строку на массивы по сепаратору
res2 = res1[1].split('.')
res2 = res2[0].split('<sup id="cite_ref')[0]
print(res2)
text = substring1 + res2 + "."
# source = "My ;name is; Bogd,an".split(sep=';')
# print(source, type(source), len(source))

# text = "Diana"
# file = open("", "w")
# # something
# file.close()
with open("temp/Diana.txt", "w", encoding="utf-8") as opened_file:
    opened_file.write(text)

with open("temp/python.html", "w", encoding="utf-8") as opened_file:
    opened_file.write(result.text)

# Выпуск

# текст
# html
# картинки
# валюта - с сайтов банков
# цены - с сайтов маркетплейсов
# погода - с сайтов погоды
# реферат - с википедии
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/102.0.0.0 Safari/537.36'
}

response = requests.get(url="https://www.gismeteo.kz/weather-zhetikara-11043/", headers=headers)
with open("temp/weather.html", "w", encoding="utf-8") as opened_file:
    opened_file.write(response.text)

# for i in range(1, 10+1):
#     # url = "https://picsum.photos/320/240/"
#     url = "https://mirpozitiva.ru/wp-content/uploads/2019/11/1472042719_15.jpg"
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
#                       'Chrome/102.0.0.0 Safari/537.36'
#     }
#     response = requests.get(url=url, headers=headers)
#     print(response.content)
#
#     import random
#     random_int = random.randint(1, 10000000)
#     # image_path = "temp/IMAGE" + str(random_int) + ".jpg"  # конкатенация - сложение строк
#     image_path = f"temp/IMAGE{random_int}.jpg"  # интерполяция
#
#     with open(image_path, "wb") as opened_file:
#         opened_file.write(response.content)

# url = "https://ru.investing.com/currencies/usd-kzt"
url = "https://kurs.kz/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 '
                  'Safari/537.36 '
}

response = requests.get(url=url, headers=headers)
# print(response.content)
print(response.text)
# substring = 'instrument-price-last'
# step_1 = response.text.split(sep=substring)[1]
# print(step_1)

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
#                   'Chrome/102.0.0.0 Safari/537.36'
# }
# url = input("Введите ссылку")  # "https://picsum.photos/320/240/"
# prefix = input()  # apple
# count = int(input())  # 10
# for i in range(1, count+1):
#     response = requests.get(url=url, headers=headers)
#     with open(f"img/{prefix}{i}.jpg", "wb") as opened_file:  # f"img/apple1.jpg"
#         opened_file.write(response.content)

arr = [
    1,
    2,
    3,
    5,
    7,
    8,
    9,
    19,
    20,
    50]
for j in arr:
    print(j)

########################################################################################################################
import time
import json
import requests  # - библиотека для формирования HTTP - запроса

# грузить картинки
# отправлять запросы
# получать ответ
# парсить данные

# HTTP  - GET POST PUT(PUTCH) DELETE (CRUD)

# response = requests.get(url="https://jsonplaceholder.typicode.com/todos/1")  # фейковая api
# print(response)  # 200 - OK - успешный ответ https://developer.mozilla.org/ru/docs/Web/HTTP/Status
# print(type(response))
# # print(response.json())
# # print(type(response.json()))
# print(response.content)
# print(type(response.content))

# сериализация / десериализация

# with open('new.json', mode='r') as file:
#     dictionary1 = json.load(file)  # позволяет сериализовать файловый - объект в словарь
#     print(dictionary1)
#     print(type(dictionary1))

# response = requests.get(url="https://jsonplaceholder.typicode.com/todos/1")
# print(response.content)
# print(type(response.content))
# dictionary2 = json.loads(response.content)  # позволяет сериализовать строку или байтовую строку в словарь
# print(dictionary2)
# print(type(dictionary2))

# with open('new1.json', mode='w') as file:
#     dict3 = {
#         "userId": 1,
#         "id": 1,
#         "title": "delectus aut autem",
#         "completed": [
#             {
#                 "userId": 1,
#                 "id": 1,
#                 "title": "delectus aut autem",
#                 "completed": False
#             },
#             {
#                 "userId": 1,
#                 "id": 1,
#                 "title": "delectus aut autem",
#                 "completed": False
#             },
#             {
#                 "userId": 1,
#                 "id": 1,
#                 "title": "delectus aut autem",
#                 "completed": False
#             }
#         ]
#     }
#     # json.dump(dict3, file)  # позволяет записать объект JSON в файл
#     ret = json.dumps(dict3)  # сериализует объект JSON в строку, которую можно без потерь записать в файл
#     print(ret)
#     print(type(ret))
#     file.write(ret)

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
#                   'Chrome/102.0.0.0 Safari/537.36'
# }
# response = requests.get(url="https://openweathermap.org/city/1526384", headers=headers)
# print(response.text)
#
# with open('new.html', mode='wb') as file:
#     file.write(response.content)

# while True:
#     url = 'https://picsum.photos/300/300/'
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
#                       'AppleWebKit/537.36 (KHTML, like Gecko) '
#                       'Chrome/102.0.0.0 Safari/537.36'
#     }
#     response = requests.get(url=url, headers=headers, timeout=10)
#     with open('new.jpg', mode='wb') as file:
#         file.write(response.content)
#
#     time.sleep(0.1)

# c = lambda a, b: a + b
# print(c(12, 15))

# response = requests.get(url="https://jsonplaceholder.typicode.com/todos").json()
# print(response)
# list1 = [x.get("title", None) for x in response if x.get("id", None) % 2 == 0]
# print(list1)

# headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
#                       'AppleWebKit/537.36 (KHTML, like Gecko) '
#                       'Chrome/102.0.0.0 Safari/537.36'
#     }
# response = requests.get(url="https://www.gismeteo.kz/weather-shymkent-5324/", headers=headers)
# # print(response.text)
# new_data = response.text.split(sep='<div class="weathertabs day-1">')[1]
# # print(new_data)
# new_data2 = new_data.split(sep='tab-temp')[1].split(sep='tab-image')[0]
# # print(new_data2)
# new_data3 = new_data2.split(sep='<span class="unit unit_temperature_c">')
# # print(new_data3)
# night = new_data3[1].split(sep='<')[0]
# day = new_data3[2].split(sep='<')[0]
# print(f"day: {day} | night: {night}")

