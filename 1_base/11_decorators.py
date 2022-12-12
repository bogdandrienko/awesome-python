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


# наслоение декораторов
def twice(function):
    def wrapper(*args, **kwargs):
        result = function(args, kwargs)
        return result * 2
    return wrapper


def rounding(function):
    def wrapper(*args, **kwargs):
        result = function(args, kwargs)
        return round(result, 3)
    return wrapper


@twice
@rounding
def func1(val1, val2):
    result = val1 + val2
    return result


result2 = func1(val1=12, val2=15.95324325)
print(result2)

########################################################################################################################
