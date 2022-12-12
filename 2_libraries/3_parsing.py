########################################################################################################################
# TODO parse data without bs4

import requests

headers = {
    "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/102.0.0.0 Safari/537.36'
}
urls = [
    'https://www.gismeteo.kz/weather-shymkent-5324/',
    'https://www.gismeteo.kz/weather-pavlodar-5174/',
    'https://www.gismeteo.kz/weather-aktobe-5165/',
]

for url in urls:
    response = requests.get(url=url, headers=headers)
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

########################################################################################################################

########################################################################################################################
# TODO parse data with bs4

from bs4 import BeautifulSoup

url = "https://www.google.com/search?q=%D1%82%D0%B5%D0%BD%D0%B3%D0%B5+%D0%BA+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D1" \
      "%83&rlz=1C1IXYC_ruKZ978KZ978&oq=%D1%82%D0%B5%D0%BD%D0%B3%D0%B5+%D0%BA+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D1" \
      "%83&aqs=chrome.0.0i433i512j0i512l9.4659j1j7&sourceid=chrome&ie=UTF-8 "
headers = {
    "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/102.0.0.0 Safari/537.36'
}
response = requests.get(url=url, headers=headers)

print(response.content.decode(), type(response.content.decode()))

soup = BeautifulSoup(response.content, 'html.parser')
valute = soup.findAll("span", {"class": "UMOHqf EDgFbc"})[0]

print(f"valute: {valute.get_text()}")
print(f"valute type: {type(valute.get_text())}")

kurs = float(str(valute.get_text()).split('отметки')[1].split('тенге')[0].strip())
print(f"kurs: {kurs}")
print(f"kurs type: {type(kurs)}")

tenge = 1200000.500

dollar = round(tenge / kurs, 2)

print(f'Ваши деньги в долларах: {dollar}')

########################################################################################################################

########################################################################################################################
# TODO parse vacancies by api

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

    # Необязательная задержка, но чтобы не нагружать сервисы hh, оставим. 5 сек мы можем подождать
    time.sleep(0.5)

print('Страницы поиска собраны')

########################################################################################################################

########################################################################################################################
# TODO parse valute with bs4

url = "https://myfin.by/converter.html"

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/102.0.0.0 Safari/537.36'}
response = requests.get(url=url, headers=headers)
status = response.status_code
if status == 200:
    content = response.content  # позволяет прочитать html фаил
    with open("temp/hw.html", "wb") as file:  # создаем фаил куда запишем html код
        file.write(content)  # записывае фаил
    soup = BeautifulSoup(response.text, "lxml")  # парсим сайт через BeautifulSoup
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
    cours = [dollar, euro, sterling, uany, zloty, rub]
    value = 450000

    for valute in cours:
        if valute[-1] == "eur":
            result = value * float(valute[0])
            print(valute[0])
            print(result)
else:
    print("Oshibka dannyh")

########################################################################################################################

########################################################################################################################
# TODO parse wheather with bs4

arr_url = []
for year in range(2011, 2012):
    for month in range(1, 2):
        for day in range(1, 32):
            url = f"http://www.pogodaiklimat.ru/weather.php?id=35042&b" \
                  f"day={day}&fday={day}&amonth={month}&ayear={year}&bot=2"
            arr_url.append(url)

arr_responces = []
for url in arr_url:
    headers = {'user-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, "html.parser")
    soup.encoded = 'utf-8'
    rows = soup.find('div', class_='archive-table-wrap')
    arr_responces.append(rows)

all_data = []
for request in arr_responces:
    data_list = []
    for row in request.find_all('tr'):
        local_data = []
        for col in row.find_all('td'):
            local_data.append(col.text)
        data_list.append(local_data)
    all_data.append([''])
    all_data.append(data_list)
for data in all_data:
    print(data)

########################################################################################################################
