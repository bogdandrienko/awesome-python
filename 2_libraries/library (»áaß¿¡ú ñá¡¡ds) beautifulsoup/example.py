import bs4
import requests
from bs4 import BeautifulSoup






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




#############################################################################################################################################################


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


#################################################################################################################################################################


class ParserBeautifulSoupClass:
    @staticmethod
    def get_url():
        pass

    @staticmethod
    def parse_local_html():
        pass

    class Example:
        @staticmethod
        def example_parse_weather():
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

        @staticmethod
        def example_perser_exams_kiney():
            version = 3
            with open(f'{version}_data.html', 'r+', encoding='utf-8') as file:
                questions = []
                index = 1
                for lines in file:
                    c1 = f"""
                    <div id="content_test"><br><div class="workspace-header"><i>Самопроверка промежуточного рейтинга 1</i></div><p><b class="question" id="1">Сұрақ № 1 / Вопрос № 1 </b>АСУ из регулятора и объекта управления, называется:</p><p><input type="radio" name="variant" value="1" id="ans1"><label for="ans1">автоматической системой регулирования АСР</label></p><p><input type="radio" name="variant" value="2" id="ans2"><label for="ans2">дистанционным управлением</label></p><p><input type="radio" name="variant" value="3" id="ans3"><label for="ans3">автоматической системой управления АСУ</label></p><p><input type="radio" name="variant" value="4" id="ans4"><label for="ans4">автоматическим управлением</label></p><p><input type="radio" name="variant" value="5" id="ans5"><label for="ans5">комплексной автоматизацией</label></p><button class="btn btn-number" number="1" style="width:40px;margin:5px;border: 2px solid #e34761;">1</button><button class="btn btn-number" number="2" style="width:40px;margin:5px;">2</button><button class="btn btn-number" number="3" style="width:40px;margin:5px;">3</button><button class="btn btn-number" number="4" style="width:40px;margin:5px;">4</button><button class="btn btn-number" number="5" style="width:40px;margin:5px;">5</button><button class="btn btn-number" number="6" style="width:40px;margin:5px;">6</button><button class="btn btn-number" number="7" style="width:40px;margin:5px;">7</button><button class="btn btn-number" number="8" style="width:40px;margin:5px;">8</button><button class="btn btn-number" number="9" style="width:40px;margin:5px;">9</button><button class="btn btn-number" number="10" style="width:40px;margin:5px;">10</button><button class="btn btn-number" number="11" style="width:40px;margin:5px;">11</button><button class="btn btn-number" number="12" style="width:40px;margin:5px;">12</button><button class="btn btn-number" number="13" style="width:40px;margin:5px;">13</button><button class="btn btn-number" number="14" style="width:40px;margin:5px;">14</button><button class="btn btn-number" number="15" style="width:40px;margin:5px;">15</button><button class="btn btn-number" number="16" style="width:40px;margin:5px;">16</button><button class="btn btn-number" number="17" style="width:40px;margin:5px;">17</button><button class="btn btn-number" number="18" style="width:40px;margin:5px;">18</button><button class="btn btn-number" number="19" style="width:40px;margin:5px;">19</button><button class="btn btn-number" number="20" style="width:40px;margin:5px;">20</button><button class="btn btn-number" number="21" style="width:40px;margin:5px;">21</button><button class="btn btn-number" number="22" style="width:40px;margin:5px;">22</button><button class="btn btn-number" number="23" style="width:40px;margin:5px;">23</button><button class="btn btn-number" number="24" style="width:40px;margin:5px;">24</button><button class="btn btn-number" number="25" style="width:40px;margin:5px;">25</button><button class="btn btn-number" number="26" style="width:40px;margin:5px;">26</button><button class="btn btn-number" number="27" style="width:40px;margin:5px;">27</button><button class="btn btn-number" number="28" style="width:40px;margin:5px;">28</button><button class="btn btn-number" number="29" style="width:40px;margin:5px;">29</button><button class="btn btn-number" number="30" style="width:40px;margin:5px;">30</button><button class="btn btn-number" number="31" style="width:40px;margin:5px;">31</button><button class="btn btn-number" number="32" style="width:40px;margin:5px;">32</button><button class="btn btn-number" number="33" style="width:40px;margin:5px;">33</button><button class="btn btn-number" number="34" style="width:40px;margin:5px;">34</button><button class="btn btn-number" number="35" style="width:40px;margin:5px;">35</button><button class="btn btn-number" number="36" style="width:40px;margin:5px;">36</button><button class="btn btn-number" number="37" style="width:40px;margin:5px;">37</button><button class="btn btn-number" number="38" style="width:40px;margin:5px;">38</button><button class="btn btn-number" number="39" style="width:40px;margin:5px;">39</button><button class="btn btn-number" number="40" style="width:40px;margin:5px;">40</button><hr></div>
<div id="content_test"><br><div class="w
                    """
                    final_data = f"<strong>{index}</strong><br><hr><br>"
                    data = lines.split(" </b>")[1].split("<button class=")[0]
                    try:
                        new_data = data.split('<img src="')
                        if len(new_data) > 2:
                            final_data += data
                        else:
                            final_data += data.split('<img src="')[0] + """<img src="https://sdo.kineu.kz""" + \
                                          data.split('<img src="')[1]
                    except Exception as ex:
                        final_data += data
                    final_data += "<br><hr><br>"
                    reverse = False
                    for question in questions:
                        if question.split("</strong>")[1] == final_data.split("</strong>")[1]:
                            print('повторение!')
                            reverse = True
                            break
                    if reverse is False:
                        questions.append(final_data)
                        index += 1
            with open(f'{version}_new_data.html', 'w', encoding='utf-8') as file:
                title = """<!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>TitleComponent</title>
            </head>
            <body>
                """
                footer = """
                </body>
            </html>"""
                file.write(title)
                for line in questions:
                    file.write(line)
                file.write(footer)