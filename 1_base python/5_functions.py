########################################################################################################################
# TODO функции


# код "до" функции
def function1():  # определение функции
    print("Hi")
    # код "внутри" функции (отступы: 2-4 пробела)


# код "после" функции

link1 = function1  # ссылка на функцию
function1()  # вызов функции


# грязная функция
def stepen_value1(val1, val2):  # функция с параметрами (аргументами)
    result = val1 ** val2
    print(result)


stepen_value1(5, 2)


# чистая функция
def stepen_value2(val1, val2):
    result = val1 ** val2
    return result  # возврат значения


result1 = stepen_value2(5, 2)  # позиционные аргументы
print(result1)
result2 = stepen_value2(val2=2, val1=6)  # именные аргументы
print(result2)


def stepen_value3(val1, val2=2):  # функция с стандартным параметром (аргументом)
    result = val1 ** val2
    return result


result3 = stepen_value3(val1=6)
print(result3)


########################################################################################################################

########################################################################################################################
# TODO типизация

# Типизация - строгое задание типов для переменных и параметров (аргументов)
# Python (СPython) - динамическая сильная типизация (+ скорость разработки - скорость работы + к багам)
# JavaScript - динамическая слабая типизация (+ скорость разработки - скорость работы  + к багам)
# C++ - статическая типизация (- скорость разработки + скорость работы - к багам)

def stepen_value4(val1: int | float, val2=2) -> int | float:  # функция с типизацией
    result = val1 ** val2
    return result


result4 = stepen_value4(val1=6) / 10
print(result4)

########################################################################################################################

########################################################################################################################
# TODO стандартные функции

print(sum([1, 2, 3]))
print(round(2.555, 1))
print(int(2.0))
print(type(True))
print(input("Введите: "))
print(abs(-100))
print(len("Привет"))
print(len([1, 2, 3, 4, 5]))


# ...
# https://pythonru.com/osnovy/vstroennye-funkcii-python
# https://letpy.com/handbook/builtins/

########################################################################################################################

########################################################################################################################
# TODO анонимные функции (lambda)

def multiply1(a, b):
    return a ** b


multiply2 = lambda a, b: a ** b

res4 = multiply1(6, 2)
res5 = multiply2(6, 2)
print(res4)
print(res5)

peoples1 = [
    {"name": "Bogdan1", "age": 24},  # dict
    {"name": "Bogdan1", "age": 22},  # dict
    {"name": "Bogdan3", "age": 20},  # dict
]


def sort1(x):
    return x["age"]


print(sorted(peoples1, key=sort1, reverse=True))
print(sorted(peoples1, key=lambda x: x["age"], reverse=True))

peoples2 = [
    [1, 1, 99, 4],  # tuple
    ("Python", 2, 6),  # list
    [99, 1, 3],  # list
]


def sort2(x):
    return x[-1]


print(sorted(peoples2, key=sort2, reverse=True))
print(sorted(peoples2, key=lambda x: x[-1], reverse=True))


########################################################################################################################

########################################################################################################################
# TODO рекурсивные функции (рекурсия)

# вывод всех чисел от нужного до 1
def while_counter(value_from):
    while value_from > 0:
        print(value_from)
        value_from = value_from - 1


while_counter(10)


def recursion_counter(value_from):
    print(value_from)
    if value_from <= 1:
        return 1
    else:
        recursion_counter(value_from - 1)


recursion_counter(10)


# факториал - произведение всех чисел от 1 до нужного
def while_factorial(stop_value: int):
    counter = 1
    while stop_value > 0:
        # counter = counter * stop_value
        counter *= stop_value
        # stop_value = stop_value - 1
        stop_value -= 1
    return counter


print(while_factorial(5))


def recursion_factorial(stop_value: int):
    if stop_value <= 1:
        return 1
    else:
        res = stop_value * recursion_factorial(stop_value - 1)
        return res


print(recursion_factorial(5))


# сумма всех чисел от 1 до нужного
def for_summator(stop_value: int) -> int:
    sum_value = 0
    for i in range(1, stop_value + 1, 1):
        sum_value += i
    return sum_value


print(for_summator(10))


def recursion_summator(stop_value: int):
    if stop_value <= 1:
        return 1
    else:
        res = stop_value + recursion_factorial(stop_value - 1)
        return res


print(recursion_summator(10))

!
def checkpolidrom(value1: str) -> bool:
    # val1, val2 = value1, value1[::-1]
    if value1 == value1[::-1]:
        return True
    else:
        return False


print(checkpolidrom("голод 1долог"))
print("run"[::])  # - пересобирает строку кроме последнего символа
print("run"[-1])  # - берёт последний символ


def recur_sum(max_val: int) -> None:
    if max_val < -100:
        return None
    else:
        print(max_val)
        recur_sum(max_val - 1)  # 9 8 7 6


# recur_sum(10)


def getfactorial(n: int) -> int:
    res = 1
    for i in range(1, n + 1):  # [1, 2, 3, 4, 5]
        res *= i
    return res


print(getfactorial(3))  # 3 628 800


def getfactorial1(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * getfactorial1(n - 1)  # (4, 5)


print(getfactorial1(4))  # 3 628 800

########################################################################################################################


!
value = len("12")  # built-in Python
value1 = abs(-10)
# abs = 10

# print(local_var)
local_var = 12  # глобальная область видимости
print(local_var)


# __main__ local_var -> func1 global local_var -> func2(local_var)

def func1(local_var):
    # global local_var  # использование переменной из глобальной области видимости

    # print(local_var)
    # local_var = 10  # локальная область видимости func1
    print(local_var)

    def func2(local_var):
        # global local_var

        print(local_var)  # локальная область видимости func2
        # local_var = 11
        print(abs)

    func2(local_var)


func1(local_var)

func1(local_var)
print(local_var)


def clear_func(value1, sep):
    # do something
    return "123"


is_commit = False  # можно изменить
COMMIT = False  # можно изменить, но не желательно (IDE подскажет)


def func_1():
    global is_commit
    global COMMIT
    is_commit = True
    COMMIT = True
    # many code
    # ...
    # value1 = 18


print(is_commit)
func_1()
print(is_commit)

########################################################################################################################

!
# def calc1():
#     return 2 * 2
#
#
# res1 = calc1()
# print(res1)
#
#
# def calc2(value):
#     return 2 * value
#
#
# res2 = calc2(3)
# print(res2)
#
# calc3 = lambda x: x * 2
#
# value = [
#     {"title": }
# ]

# Нахождение факториала числа
# Палиндром  -  "мадам"  - "анна"  - "роза упала на лапу азора"  # "{([)}"

b = """
А муза рада музе без ума да разума
или
"""

a = """
голод долог
"""


# def get_value(val1):
#     if val1 < 10:
#         return True
#     else:
#         get_value(val1-1)

def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res
print(factorial(5))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))

for i in range(1, 6):
    print(i, '! = ', factorial(i), sep='')


def get_factorial(num: int):
    start = 1
    if num <= 0:
        return True
    else:
        print(num * 2)
        get_factorial(num - 1)


get_factorial(2)


def is_palindrome(s):
    if len(s) < 1:
        return True
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False


def is_palindrom(text: str):  # return True if text is palindrom bla-bla
    if len(text) < 1:
        return True
        # continue break
    if text[0] == text[-1]:  # text[-1]: - предпоследний           text[len(text)]: - последний
        return is_palindrom(text[1:-1])  # ада   [0:len(new_text):1]
    else:
        return False


# is_palindrom(s: str) -> True/False  -> is_palindrom(s: str) -> True/False -> is_palindrom(s: str) -> True/False ...
# is_palindrom(s: str) -> True/False  -> is_palindrom(s: str) -> True/False <- is_palindrom(s: str) <- True

def is_palindrom2(text1: str):
    text2 = text1[::-1]
    print(text1)
    print(text2)
    if text1 == text2:  # t "158" <=> t "158"
        # ord()
        return True
    else:
        return False


res = is_palindrom2("Мадам")
print(res)
print(type(res))
if res:
    print("Да, это палиндром")
else:
    print("Нет, это  не палиндром")

# callback


exprs1 = lambda val1, val2: val1 * val2  # лямбда выражение


def calc1(val1, val2):
    return val1 * val2


exprs2 = calc1  # ссылка на функцию

print(exprs1(2, 7))
print(exprs2(2, 7))

arr1 = []
for i in range(1, 5):
    if i % 2 == 0:
        # result = calc1(12, i)
        arr1.append(exprs1)
    else:
        arr1.append(calc1)

print(arr1)
print(type(arr1))

print(arr1[0])
print(type(arr1[0]))

for i in arr1:
    print(i(1, 2))


# lam1 = lambda character: ord(character)

# print(lam1())

def lam2(character):
    return ord(character)


lam1 = lambda character: ord(character)

arrrr1 = [lam1(x) for x in 'Привет мир!']  # lazy computing
print(arrrr1)

arrrr1 = [8, *arrrr1, 8]  # *args - позиционные аргументы

for i in arrrr1:
    print(i)

print(arrrr1)
# arrrr1.sort(key=lambda item: str(item).find("8"), reverse=True)
arrrr1.sort(key=lambda item: item % 2 == 0, reverse=False)  # от меньшего к большему 0....9...100

#    2    2      2    2     2    0  0     -1    -1     -1    -1  -1  -1
# '1088'
# [1088, 1080, 1084, 1080, 1088, "8", 8, 1055, 1074, 1077, 1090, 32, 33]
print(arrrr1)

########################################################################################################################

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a = 10

    print_hi('PyCharmcccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc'
             'cccccccccccccc')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

########################################################################################################################