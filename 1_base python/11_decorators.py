########################################################################################################################
# TODO декораторы

import time
import datetime


# декоратор для округления результата до 2 знака после запятой
def decorator_rounding(func):  # определение декоратора -> ссылку на функцию
    def decorator(*args, **kwargs):  # передача аргументов к вызову функции
        # BEFORE - корректировка результата перед отработкой функции
        result = func(*args, **kwargs)  # вызов функции
        # AFTER - корректировка результата после отработки функции
        result = round(result, 2)
        return result  # возврат результата функции

    return decorator  # возврат декоратора


@decorator_rounding  # добавление декоратора
def summing(value1, value2, value3):
    res = value1 + value2 + value3
    return res  # возврат результата функции


@decorator_rounding  # добавление декоратора
def divider(value1, value2):
    res = value1 / value2
    return res


print(summing(-12, 17.0006, 1))  # вызов функции и вывод результата

print(divider(12, -17))  # вызов функции и вывод результата


#
def decorator_time_measuring(function):
    def decorator(*args, **kwargs):
        time_start = datetime.datetime.now()

        result = function(*args, **kwargs)

        time_difference = datetime.datetime.now() - time_start
        print(round(time_difference.seconds, 5))

        return result

    return decorator


@decorator_time_measuring
def function_something_write(value: int):
    time.sleep(0.15)  # Ядро функции 1
    return value


@decorator_time_measuring
def function_something_read():
    time.sleep(0.07)  # Ядро функции 2
    return ['12', 124325]


print(function_something_write(6666))
print(function_something_read())

########################################################################################################################

!
import time


def decorator_before(func):  # ссылка на функцию
    def with_before():
        print('start decorator')

        #
        # ядро функции
        func()  # вызов функции
        # ядро функции
        #

        print('end decorator!')

    return with_before


@decorator_before
def write():
    #
    # ядро функции
    print("Write file!")
    # ядро функции
    #


@decorator_before
def read():
    print('start action!')

    #
    # ядро функции
    print("Read file!")
    # ядро функции
    #

    print('Completed!')


# write()


# read()

def decorator_measure_time(function):
    def decorator(*args, **kwargs):  # args - позиционные - tuple(1,2,3,4) | kwargs - {"key_1": 12, "key_2": 13}
        time_start = time.perf_counter()
        result = function(*args, **kwargs)
        print(time.perf_counter() - time_start)
        return result

    return decorator


@decorator_measure_time
def tick(value: float):
    print('start tick')
    time.sleep(value)
    print('end tick')

    return f'completed of {value}'


# result1 = tick(1.5, 2.6)
# print(result1)
# result2 = tick(**{"value": 1.5})
result2 = tick(value=1.6)
# print(result2)

val1 = [12, [12, True, "15"], "15"]


# val1 = [12, "13", 15]
# print(12, True, 15)


# print(type(*val1))


def get_list(a, b, c):
    print(a)
    print(b)
    print(c)
    return a, b, c


# res = get_list(*val1)

val2 = {"title": "Алиса", "surname": "12"}


# print(*val2)


def get_list1(surname: str, title):
    print(f'title: {title}')
    print(f'surname: {surname}')


get_list1(**val2)

########################################################################################################################

import time
import requests
import threadi
import multiprocessing
import asyncio
import aiohttp

# import new
# from api.main import index
from new import Example

print(Example.get_round(10.66))


# print(new.func_1())

# print(func_1())

def measure(func):
    def wrap(*args, **kwargs):
        print('start measure')

        time1 = time.perf_counter()
        res = func(*args, **kwargs)  # ядро декорируемой функции

        print('end measure')
        print(f'функция потратила времени: {time.perf_counter() - time1}')
        return res

    return wrap


def download_image(name):
    response = requests.get(
        url="https://picsum.photos/370/250",
        headers={
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/102.0.0.0 Safari/537.36'
        }
    )

    # print(response)
    # print(type(response))

    #  response.status_code  # 200
    #  response.content  # bytes b""

    with open(f'temp/image_{name}.jpg', 'wb') as file:
        file.write(response.content)


@measure
def sync_f():
    for i in range(1, 100):
        download_image(i)


@measure
def threading_f():
    # thread_1 = threading.Thread(
    #     target=download_image,
    #     args=("thread_1",),
    #     kwargs={}
    # )
    #
    # thread_1.start()
    # thread_1.join()

    thread_list = [threading.Thread(target=download_image, args=(f"thread_{x}",), kwargs={}) for x in range(1, 100)]

    # thread_list = []
    # for x in range(1, 10):
    #     thread_list.append(threading.Thread(target=download_image, args=(f"thread_{x}",), kwargs={}))

    for i in thread_list:
        i.start()

    for i in thread_list:
        i.join()

    # exit


@measure
def processing_f():
    # process_1 = multiprocessing.Process(
    #     target=download_image,
    #     args=("process_1",),
    #     kwargs={}
    # )
    #
    # process_1.start()
    # process_1.join()

    process_list = [multiprocessing.Process(target=download_image, args=(f"process_{x}",), kwargs={}) for x in
                    range(1, 100)]

    for i in process_list:
        i.start()

    for i in process_list:
        i.join()

    # exit


async def async_download_image(name):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/102.0.0.0 Safari/537.36'
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url="https://picsum.photos/370/250", headers=headers) as await_response:
            data = await await_response.read()

    with open(f'temp/image_{name}.jpg', 'wb') as file:
        file.write(data)


@measure
def async_f():
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(async_download_image("async_1"))

    async def tasks_generator():  # корутины - coro  - задачи с задержкой по выполнению и возврату
        await asyncio.gather(
            *[async_download_image(f"async_{x}") for x in range(1, 100)]
        )

    loop = asyncio.get_event_loop()
    loop.run_until_complete(tasks_generator())


def tick(name):
    print(f'tick {name} start\n')
    time.sleep(1.0)
    print(f'tick {name} end\n')


async def tick_a(name):
    print(f'tick {name} start\n')
    await asyncio.sleep(1)
    print(f'tick {name} end\n')


@measure
def start():
    # последовательно
    # tick("sync 1")
    # tick("sync 2")
    # tick("sync 3")

    # thread_1 = threading.Thread(target=tick, args=("thread 1",))
    # thread_1.start()
    #
    # thread_2 = threading.Thread(target=tick, args=("thread 2",))
    # thread_2.start()
    #
    # thread_3 = threading.Thread(target=tick, args=("thread 3",))
    # thread_3.start()
    #
    # thread_1.join()
    # thread_2.join()
    # thread_3.join()

    # process_1 = multiprocessing.Process(target=tick, args=("process 1",))
    # process_1.start()
    #
    # process_2 = multiprocessing.Process(target=tick, args=("process 2",))
    # process_2.start()
    #
    # process_3 = multiprocessing.Process(target=tick, args=("process 3",))
    # process_3.start()
    #
    # process_1.join()
    # process_2.join()
    # process_3.join()

    async def tasks_generator():  # корутины - coro  - задачи с задержкой по выполнению и возврату
        await asyncio.gather(
            *[tick_a(f"async_{x}") for x in range(1, 4)]
        )

    loop = asyncio.get_event_loop()
    loop.run_until_complete(tasks_generator())


if __name__ == '__main__':  # точка входа, т.е. отсюда стартует этот файл при запуске
    # sync_f()  # 59.278442899999995       1 thread * 1 process
    # threading_f()  # 3.6611930999999998  1 * 100
    # processing_f()  # 4.1108648          100 * 1
    # async_f()  # 2.7549684                 1 * 1
    start()
# последовательно - 1 поток, 1 процесс (по очереди)
# многопоточно - N поток, 1 процесс
# мультипроцесс - N поток, N процесс
# асинхронно - 1 поток, 1 процесс (цикл событий)

!
########################################################################################################################


def multiply(function):
    def wrapper(*args, **kwargs):
        kwargs["name"] = kwargs["name"] * 2
        # print(args[0]2)
        # args2 = [args[0]2, args[1:]]
        # print(args2)
        print("multiply")
        print(f"args: {args}")
        print(f"kwargs: {kwargs}")
        resp = function(args, kwargs)
        return resp
    return wrapper


# print(10//2)
# print(int(10/2))
def mydecorator_half(function):
    def wrapper(*args, kwargs):
        print("mydecorator_half")
        print("Что то печатает ДО")
        res = function(*args, **kwargs)
        print("Что то печатает ПОСЛЕ")
        res2 = res[len(res) // 2::]
        return res2
    return wrapper


@multiply
@mydecorator_half
def func1(name):
    return f"Hello, everybody!+{name}"


res = func1(name="python")
print(res)