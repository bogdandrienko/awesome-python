########################################################################################################################
# TODO потоки исполнения

import time
import datetime
import random
import threading
import multiprocessing
import asyncio
import concurrent.futures
import requests
import aiohttp
import aiofiles

# sync VS async VS threading VS multiprocessing

# sync =                1 процесс: 1 поток
# threading =           1 процесс: N поток
# multiprocessing =     N процесс: N поток
# async =               1 процесс: 1 поток

url = "https://picsum.photos/320/240/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/102.0.0.0 Safari/537.36'
}


def sync_download_one_image():
    response = requests.get(url=url, headers=headers)
    with open(f"temp/image{random.randint(1, 10000000)}.jpg", "wb") as opened_file:
        opened_file.write(response.content)


def sync_download_mass_image():
    start_time = time.perf_counter()

    # загрузка одной картинки в этом потоке
    # sync_download_one_image()

    # загрузка 10 картинок в этом потоке
    for i in range(1, 10 + 1):
        sync_download_one_image()

    print(f'Задача закончила работу за {round(time.perf_counter() - start_time, 5)}')


def threading_download_mass_image():
    start_time = time.perf_counter()

    # загрузка одной картинки в дополнительном потоке
    # thread = threading.Thread(target=sync_download_one_image, args=(), kwargs={}) # формирование задачи
    # thread.start()  # запуск задачи
    # thread.join()  # ожидание завершения потока

    # загрузка 10 картинок в дополнительных 10 потоках
    thread_list = []
    for i in range(1, 10 + 1):
        thread_list.append(threading.Thread(target=sync_download_one_image, args=(), kwargs={}))
    for thread in thread_list:
        thread.start()
    for thread in thread_list:
        thread.join()

    # загрузка 10 картинок в дополнительных 10 процессах в 1 потоке, но с ограничением на 10 потоков
    # with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    #     for i in range(1, 10+1):
    #         executor.submit(sync_download_one_image, ())

    # возврат результатов
    # with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    #     futures = []
    #     for url in range(1, 10+1):
    #         futures.append(executor.submit(sync_download_one_image))
    #     for future in concurrent.futures.as_completed(futures):
    #         print(future.result())
    # with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    #     futures = []
    #     for i in range(1, 10+1):
    #         future = executor.submit(sync_download_one_image)
    #         futures.append(future.result())

    print(f'Задача закончила работу за {round(time.perf_counter() - start_time, 5)}')


def processing_download_mass_image():
    start_time = time.perf_counter()

    # загрузка одной картинки в дополнительном процессе в 1 потоке
    # process = multiprocessing.Process(target=sync_download_one_image, args=(), kwargs={}) # формирование задачи
    # process.start()  # запуск задачи
    # process.join()  # ожидание завершения потока

    # загрузка 10 картинок в дополнительных 10 процессах в 1 потоке
    process_list = []
    for i in range(1, 10 + 1):
        process_list.append(multiprocessing.Process(target=sync_download_one_image, args=(), kwargs={}))
    for process in process_list:
        process.start()
    for process in process_list:
        process.join()

    # загрузка 10 картинок в дополнительных 10 процессах в 1 потоке, но с ограничением на 10 процессов
    # with concurrent.futures.ProcessPoolExecutor(max_workers=10) as executor:
    #     for i in range(1, 10+1):
    #         executor.submit(sync_download_one_image, ())

    print(f'Задача закончила работу за {round(time.perf_counter() - start_time, 5)}')


async def async_t():
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url, headers=headers) as response:
            data = await response.read()

            with open(f"temp/image{random.randint(1, 10000000)}.jpg", "wb") as opened_file:
                opened_file.write(data)


def async_task():
    start_time = time.perf_counter()

    async def async_task_asyncio():  # корутина
        await asyncio.gather(
            *[async_t() for x in range(1, 101)]
        )

    asyncio.run(async_task_asyncio())

    print(f'Задача закончила работу за {round(time.perf_counter() - start_time, 5)}')


if __name__ == "__main__":
    sync_download_mass_image()
    threading_download_mass_image()
    processing_download_mass_image()
    async_task()

    pass

########################################################################################################################

!
import multiprocessing
import threading
import time
import asyncio
import requests
import aiohttp


def data_analyse(func):
    def obertka(*args, **kwargs):
        print(args)  # ('Bogdan', 'Saadat')
        print(type(args))
        print(kwargs)  # {'author': 'Bogdan', 'name': 'Saadat'}
        print(type(kwargs))

        kwargs["author"] = kwargs["author"] + " !!!"

        result = func(*args, **kwargs)

        post_result = (result, len(result))  # кортеж из двух элементов, где второй это длина массива

        return post_result

    return obertka


@data_analyse
def get_data(name: str, author):
    return f"Hello {name}, {author}"


val1 = ('Bogdan', 'Saadat')
val2 = {'author': 'Bogdan', 'name': 'Saadat'}


# data = get_data(**val2)
# print(data)

# url = 'https://www.gismeteo.kz/weather-zhetikara-11043/'
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
#                          'Chrome/102.0.0.0 Safari/537.36'}
#
# res = requests.get(
#     url=url,
#     headers=headers
# )
# # print(res)
# # print(type(res))
# #
# # print(res.status_code)
# # print(type(res.status_code))
# #
# # print(res.content)
# # print(type(res.content))
#
# data = res.text
# # print(data)
# # print(type(data))
#
# data1 = data.split('''class="weathertabs day-1"''')[1]
# # print(data1)
# # print(type(data1))
# # print(len(data1))
#
# data2 = data1.split('''Сейчас''')[1].split('''Завтра''')[0].split('''class="unit unit_temperature_c">''')
# print(data2)
# print(type(data2))
# print(len(data2))
#
# # for i in data2:
# #     print(i, '\n\n')
#
# data3 = data2[-2::1]  # [шаг:стоп:шаг] [::] - [идём с нулевого:до последнего:1]
# print(data3)
# print(type(data3))
# print(len(data3))
#
# day = ''
# night = ''
#
# for i in data3:
#     if len(data3[1]) == len(i):
#         day = i.split('''</span>''')[0]
#     else:
#         night = i.split('''</span>''')[0]
# print(f'''темпаратура днём: {day}, а ночью: {night}, город: {'https://www.gismeteo.kz/weather-zhetikara-11043/'.split('weather-')[1].split('-')[0]}''')
#

class Response:
    def __init__(self):
        content, code = self.validate()
        self.status_code = code
        self.content = content
        self.text = b'\xd0\x91\xd0\xb0\xd0\xb9\xd1\x82\xd1\x8b'.decode()

    def validate(self):
        result = (b'\xd0\x91\xd0\xb0\xd0\xb9\xd1\x82\xd1\x8b', 200)
        return result


# res1 = Response()
# print(res1)
# print(type(res1))
#
# print(res1.status_code)
# print(type(res1.status_code))
#
# print(res1.content)
# print(type(res1.content))
#
# print(res1.text)
# print(type(res1.text))

# print("Тлеген".encode().decode())


def time_zamer(func):
    def obertka(*args, **kwargs):
        time_start = time.perf_counter_ns()

        result = func(*args, **kwargs)

        time_stop = time.perf_counter_ns()

        print((time_stop - time_start) // 1000000, 'ms')  # 1 424 236 700   - -9 -6 -3

        return result

    return obertka


def get_meteo(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/102.0.0.0 Safari/537.36'}
    res = requests.get(
        url=url,
        headers=headers
    )
    data1 = res.text.split('''class="weathertabs day-1"''')[1]
    data2 = data1.split('''Сейчас''')[1].split('''Завтра''')[0].split('''class="unit unit_temperature_c">''')
    data3 = data2[-2::1]
    day = ''
    night = ''
    for i in data3:
        if len(data3[1]) == len(i):
            day = i.split('''</span>''')[0]
        else:
            night = i.split('''</span>''')[0]
    print(f'''темпаратура днём: {day}, а ночью: {night}, город: {url.split('weather-')[1].split('-')[0]}''')


city_list = [
    'https://www.gismeteo.kz/weather-zhetikara-11043/',
    'https://www.gismeteo.kz/weather-kostanay-4628/',
    'https://www.gismeteo.kz/weather-shymkent-5324/',
    'https://www.gismeteo.kz/weather-nur-sultan-5164/',
    'https://www.gismeteo.kz/weather-almaty-5205/',
    'https://www.gismeteo.kz/weather-zhetikara-11043/',
    'https://www.gismeteo.kz/weather-kostanay-4628/',
    'https://www.gismeteo.kz/weather-shymkent-5324/'
]


@time_zamer
def sync():  # 1 поток, 1 процесс
    for city in city_list:
        get_meteo(url=city)


@time_zamer
def thread():  # несколько потоков, 1 процесс
    # thread1 = threading.Thread(target=get_meteo, args=('https://www.gismeteo.kz/weather-zhetikara-11043/',))
    # thread1.start()
    # thread1.join()

    thread_list = []
    for city in city_list:
        new_thread = threading.Thread(target=get_meteo, args=(city,))
        thread_list.append(new_thread)

    # print(thread_list)
    # print(type(thread_list[0]))

    for new_thread in thread_list:
        new_thread.start()

    for new_thread in thread_list:
        new_thread.join()


@time_zamer
def process():  # 1 поток, несколько процессов
    # name1 = multiprocessing.Process(target=get_meteo, args=('https://www.gismeteo.kz/weather-zhetikara-11043/',))
    # name1.start()
    # name1.join()

    thread_list = []
    for city in city_list:
        new_thread = multiprocessing.Process(target=get_meteo, args=(city,))
        thread_list.append(new_thread)

    # print(thread_list)
    # print(type(thread_list[0]))

    for new_thread in thread_list:
        new_thread.start()

    for new_thread in thread_list:
        new_thread.join()


async def async_get_meteo(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/102.0.0.0 Safari/537.36'}
    async with aiohttp.ClientSession() as ses:
        async with ses.get(
                url=url,
                headers=headers
        ) as response:
            res = await response.read()

    data1 = res.decode().split('''class="weathertabs day-1"''')[1]
    data2 = data1.split('''Сейчас''')[1].split('''Завтра''')[0].split('''class="unit unit_temperature_c">''')
    data3 = data2[-2::1]
    day = ''
    night = ''
    for i in data3:
        if len(data3[1]) == len(i):
            day = i.split('''</span>''')[0]
        else:
            night = i.split('''</span>''')[0]
    print(f'''темпаратура днём: {day}, а ночью: {night}, город: {url.split('weather-')[1].split('-')[0]}''')


@time_zamer
def async_func():  # 1 поток, 1 процесс
    # for city in city_list:
    #     get_meteo(url=city)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(
        asyncio.gather(
            *[async_get_meteo(city) for city in city_list]
        )
    )


if __name__ == '__main__':
    sync()  # 1950 ms         -> 0 ms
    # thread()  # 301 ms        -> 1 ms
    # process()  # 577 ms       -> 262 ms (0,25 s)
    # async_func()  # 248 ms      -> 0 ms
    pass

########################################################################################################################

import time
import threading
import multiprocessing
import asyncio


def decor(func):
    def decor_inline(*args, **kwargs):  # *(12, 15, 6,) - tuple(кортеж) \ **{"name":"Py", 'age': 12} - dict(словарь)
        # ПРЕДОБРАБОТКА
        time_start = time.perf_counter()
        # ПРЕДОБРАБОТКА

        # arg1 = args[1]

        result = func(*args, **kwargs)

        # ПОСТОБРАБОТКА
        print(f'всё действие заняло: {round(time.perf_counter() - time_start, 5)}')
        # ПОСТОБРАБОТКА

        return result

    return decor_inline


def task(name: str) -> None:
    print(f'начало {name}')
    time.sleep(1.0)  # блокирующая операция - обращение в базу данных, загрузка картинки...
    print(f'конец {name}')


async def task_a(name: str) -> None:
    print(f'начало {name}')
    await asyncio.sleep(1.0)  # блокирующая операция - обращение в базу данных, загрузка картинки...
    print(f'конец {name}')


# последовательная
@decor
def synhronus():  # 3.01685
    task(name='Задача 1')
    task(name='Задача 2')
    task(name='Задача 3')


# многопоточность
@decor
def threadings():  # 1.01568

    def task_new():
        new_thread_1 = threading.Thread(target=task, args=('Задача 1',))
        new_thread_1.start()
        new_thread_1.join()

        new_thread_2 = threading.Thread(target=task, args=('Задача 2',))
        new_thread_2.start()
        new_thread_2.join()

    new_thread_4 = threading.Thread(target=task_new, args=('Задача 3',))
    new_thread_4.start()

    new_thread_3 = threading.Thread(target=task, args=('Задача 3',))
    new_thread_3.start()

    new_thread_3.join()
    new_thread_4.join()

    print('я главный поток, я закончил работу, я домой')


# мультипроцессорность
@decor
def processings():  # 1.10279
    new_process_1 = multiprocessing.Process(target=task, args=('Задача 1',))
    new_process_1.start()

    new_process_2 = multiprocessing.Process(target=task, args=('Задача 2',))
    new_process_2.start()

    new_process_3 = multiprocessing.Process(target=task, args=('Задача 3',))
    new_process_3.start()

    new_process_1.join()
    new_process_2.join()
    new_process_3.join()

    print('я главный поток, я закончил работу, я домой')


# асинхронная
@decor
def asynchronus():
    async def task_generator():
        await asyncio.gather(*[
            task_a(name='Задача 1'),
            task_a(name='Задача 2'),
            task_a(name='Задача 3'),
        ])

    loop = asyncio.get_event_loop()
    loop.run_until_complete(task_generator())


if __name__ == "__main__":
    # synhronus()    # 3.016   1 процесс и 1 поток, но блокирующие
    # threadings()   # 1.015   1 процесс и много потоков
    # processings()  # 1.102   много процессов и 1 поток (на самом деле много)
    # asynchronus()    # 1.003   1 процесс и 1 поток, но не блокирующие

    # # *(12, 15, 6,) - tuple(кортеж) \ **{"name": "Py", 'age': 12} - dict(словарь)

    # tup1 = (12, 15, 6,)
    # print(*tup1)

    def tas(name, age):
        print(name, age)

    dict1 = {"name": "Py", 'age': 12}
    # tas(name=dict1["name"], age=dict1['age'])
    tas(**dict1)
    # print(name="Py", age=12) # **dict1

########################################################################################################################

import asyncio

import requests
import os
import concurrent.futures
import aiohttp


class FileAlreadyExists(Exception):
    def __init__(self, text: str):
        self.error_text = text

    def get_error(self) -> str:
        return self.error_text


def get_name(file_name="pic.jpg"):
    response = requests.get(url="https://picsum.photos/600/600/", headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/102.0.0.0 Safari/537.36'
    }

                            )

    try:
        if os.path.exists(file_name):
            raise FileAlreadyExists("File already exists! ")
        file = open(file_name, "wb")
        file.write(response.content)
    except FileAlreadyExists as error:
        os.remove(file_name)
        print(f"Файл уже есть! {error.get_error()}")
        get_name("pic2.jpg")
    except Exception as error:
        print(error)
    finally:
        # file.close()
        pass


def multi():
    current_thread = 16
    with concurrent.futures.ThreadPoolExecutor(max_workers=current_thread * 2 + 1) as executor:
        for x in range(1, 10 + 1):
            executor.submit(get_name, f'img{x}.jpg')


async def multi_async():
    await asyncio.gather(*[get_name_async(f"img{i}.jpg") for i in range(1, 10 + 1)])


async def get_name_async(file_name: str) -> None:
    async with aiohttp.ClientSession() as session:
        async with session.get(url="https://picsum.photos/600/600/", headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/102.0.0.0 Safari/537.36'
        }

                               ) as request:
            response = await request.read()

    with open(file_name, "wb") as file:
        file.write(response)


def async_start():
    asyncio.run(multi_async())


if __name__ == '__main__':
    # get_name()
    # multi()
    async_start()
!


########################################################################################################################